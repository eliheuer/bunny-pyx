# Bunny Pyx
import pyxel

# Woskspace constants
CANVAS_WIDTH   = 256
CANVAS_HEIGHT  = 128
TOOLBAR_HEIGHT = 32


# Tool constants
TOOL_PENCIL = 0
TOOL_BRUSH  = 1
TOOL_ERASER = 2
TOOL_FILL   = 3
TOOL_LINE   = 4
TOOL_RECT   = 5
TOOL_CIRCLE = 6
TOOL_CLEAR  = 7
TOOL_STAMP  = 8

# Number of tools in toolbar
NUM_TOOLS = 9

# Brush sizes
SIZES = [1, 3, 6, 12]

# Color palette layers
# Each layer has 14 colors (to leave room for navigation buttons)
COLOR_PALETTES = [
    # Layer 1: Default Pyxel colors (minus the last two)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    # Layer 2: Last two colors from layer 1 + rainbow colors
    [14, 15, 8, 9, 10, 11, 12, 3, 1, 2, 4, 5, 6, 7],
    # Layer 3: Grayscale (using default Pyxel colors for now)
    [0, 0, 5, 5, 6, 6, 7, 7, 7, 6, 6, 5, 5, 0],
]

# Stamp images
# Array of (x, y) coordinates for the stamps in the resource file
STAMPS = [
    (0, 0),  # Pencil icon
    (16, 0),  # Brush icon
    (32, 0),  # Eraser icon
    (48, 0),  # Fill icon
    (64, 0),  # Line icon
    (80, 0),  # Rectangle icon
    (96, 0),  # Circle icon
    (112, 0),  # Clear icon
    (128, 0),  # Stamp icon
    (144, 0),  # Will be additional stamps
    (160, 0),
    (176, 0),
    (192, 0),
    (208, 0),
]


class BunnyPyx:
    def __init__(self):
        pyxel.init(256, 160, title="Bunny Pyx")
        pyxel.load("assets/bunny-pyx.pyxres")
        pyxel.mouse(True)

        # Initialize canvas
        self.current_tool = TOOL_PENCIL
        self.current_color = 7  # White
        self.current_size = 1
        self.old_x = 0
        self.old_y = 0
        self.drawing = False
        self.start_x = 0
        self.start_y = 0

        # Initialize palette layer
        self.current_palette = 0
        self.num_palettes = len(COLOR_PALETTES)

        # Initialize stamp
        self.current_stamp = 0
        self.num_stamps = len(STAMPS)

        # Create a second image for the canvas
        pyxel.image(1).cls(0)

        # Run the application
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        toolbar_y = 160 - TOOLBAR_HEIGHT  # Position at bottom of window

        # Toolbar interaction
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            # Color/Stamp palette row interaction
            if pyxel.mouse_y > toolbar_y + 16 and pyxel.mouse_y < toolbar_y + 32:
                if self.current_tool == TOOL_STAMP:
                    # Stamp selection mode
                    # Left arrow button (first position)
                    if 0 <= pyxel.mouse_x < 16:
                        self.current_stamp = (self.current_stamp - 1) % self.num_stamps
                    # Right arrow button (last position)
                    elif 240 <= pyxel.mouse_x < 256:
                        self.current_stamp = (self.current_stamp + 1) % self.num_stamps
                    # Stamp selection (positions 1-14)
                    else:
                        stamp_idx = (pyxel.mouse_x - 16) // 16
                        if 0 <= stamp_idx < 14:  # Only 14 visible stamps at once
                            self.current_stamp = stamp_idx
                else:
                    # Color selection mode
                    # Left arrow button (first position)
                    if 0 <= pyxel.mouse_x < 16:
                        self.current_palette = (
                            self.current_palette - 1
                        ) % self.num_palettes
                    # Right arrow button (last position)
                    elif 240 <= pyxel.mouse_x < 256:
                        self.current_palette = (
                            self.current_palette + 1
                        ) % self.num_palettes
                    # Color selection (positions 1-14)
                    else:
                        col_idx = (pyxel.mouse_x - 16) // 16
                        if 0 <= col_idx < 14:
                            self.current_color = COLOR_PALETTES[self.current_palette][
                                col_idx
                            ]

            # Tool selection (top row of toolbar)
            elif pyxel.mouse_y > toolbar_y and pyxel.mouse_y < toolbar_y + 16:
                col = pyxel.mouse_x // 16
                if 0 <= col < NUM_TOOLS:
                    self.current_tool = col

                # Size selection (right side)
                size_idx = (pyxel.mouse_x - (256 - len(SIZES) * 16)) // 16
                if (
                    256 - len(SIZES) * 16
                ) <= pyxel.mouse_x < 256 and 0 <= size_idx < len(SIZES):
                    self.current_size = SIZES[size_idx]

                # Clear canvas if clear tool selected
                if self.current_tool == TOOL_CLEAR:
                    pyxel.image(1).cls(0)

        # Canvas drawing
        if pyxel.mouse_y < CANVAS_HEIGHT:
            # Start drawing
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.drawing = True
                self.start_x = pyxel.mouse_x
                self.start_y = pyxel.mouse_y

                # For pencil and brush, draw immediately
                if self.current_tool in (TOOL_PENCIL, TOOL_BRUSH, TOOL_ERASER):
                    self.draw_point(pyxel.mouse_x, pyxel.mouse_y)

                # Fill bucket tool
                elif self.current_tool == TOOL_FILL:
                    pyxel.image(1).cls(self.current_color)

                # Stamp tool - stamp immediately
                elif self.current_tool == TOOL_STAMP:
                    self.stamp_image(pyxel.mouse_x, pyxel.mouse_y)

            # Continue drawing
            elif pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and self.drawing:
                if self.current_tool in (TOOL_PENCIL, TOOL_BRUSH, TOOL_ERASER):
                    color = (
                        0 if self.current_tool == TOOL_ERASER else self.current_color
                    )
                    size = (
                        self.current_size * 2
                        if self.current_tool == TOOL_BRUSH
                        else self.current_size
                    )

                    # Draw line between old position and new position
                    pyxel.image(1).line(
                        self.old_x, self.old_y, pyxel.mouse_x, pyxel.mouse_y, color
                    )

                    # For brush, make thicker line
                    if self.current_tool == TOOL_BRUSH:
                        for dx in range(-size // 2, size // 2 + 1):
                            for dy in range(-size // 2, size // 2 + 1):
                                if dx * dx + dy * dy <= (size // 2) * (size // 2):
                                    pyxel.image(1).line(
                                        self.old_x + dx,
                                        self.old_y + dy,
                                        pyxel.mouse_x + dx,
                                        pyxel.mouse_y + dy,
                                        color,
                                    )
                elif self.current_tool == TOOL_STAMP:
                    # Allow continuous stamping while dragging, with minimal delay
                    if pyxel.frame_count % 2 == 0:  # Reduced from 8 to 2 frames
                        self.stamp_image(pyxel.mouse_x, pyxel.mouse_y)

            # End drawing
            elif pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) and self.drawing:
                self.drawing = False

                # Line, rectangle and circle shapes finalize when mouse is released
                if self.current_tool == TOOL_LINE:
                    pyxel.image(1).line(
                        self.start_x,
                        self.start_y,
                        pyxel.mouse_x,
                        pyxel.mouse_y,
                        self.current_color,
                    )
                elif self.current_tool == TOOL_RECT:
                    x1, y1 = self.start_x, self.start_y
                    x2, y2 = pyxel.mouse_x, pyxel.mouse_y

                    # Make sure x1,y1 is top-left and x2,y2 is bottom-right
                    if x1 > x2:
                        x1, x2 = x2, x1
                    if y1 > y2:
                        y1, y2 = y2, y1

                    pyxel.image(1).rect(
                        x1, y1, x2 - x1 + 1, y2 - y1 + 1, self.current_color
                    )
                elif self.current_tool == TOOL_CIRCLE:
                    x1, y1 = self.start_x, self.start_y
                    x2, y2 = pyxel.mouse_x, pyxel.mouse_y
                    radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
                    pyxel.image(1).circ(x1, y1, radius, self.current_color)

        # Update old position for next frame
        self.old_x = pyxel.mouse_x
        self.old_y = pyxel.mouse_y

    def draw_point(self, x, y):
        color = 0 if self.current_tool == TOOL_ERASER else self.current_color
        size = (
            self.current_size * 2
            if self.current_tool == TOOL_BRUSH
            else self.current_size
        )

        if self.current_tool == TOOL_BRUSH:
            pyxel.image(1).circ(x, y, size // 2, color)
        else:
            pyxel.image(1).rect(x - size // 2, y - size // 2, size, size, color)

    def stamp_image(self, x, y):
        # Get stamp coordinates
        sx, sy = STAMPS[self.current_stamp]

        # Center the stamp on the mouse position
        dest_x = x - 8
        dest_y = y - 8

        # Copy the stamp to the canvas with transparency (color 0)
        pyxel.image(1).blt(dest_x, dest_y, 0, sx, sy, 16, 16, 0)

    def draw(self):
        pyxel.cls(5)  # Background color

        # Draw the canvas
        pyxel.blt(0, 0, 1, 0, 0, CANVAS_WIDTH, CANVAS_HEIGHT)

        # Draw toolbar background
        toolbar_y = 160 - TOOLBAR_HEIGHT  # Position at bottom of window
        pyxel.rect(0, toolbar_y, CANVAS_WIDTH, TOOLBAR_HEIGHT, 13)

        # Draw tool icons (16x16 each)
        for i in range(NUM_TOOLS):
            x = i * 16
            y = toolbar_y

            # Highlight selected tool with 15x15 indicator
            if i == self.current_tool:
                pyxel.rectb(x + 1, y + 1, 14, 14, 7)

            # Draw the icon from sprite sheet (image 0)
            pyxel.blt(x, y, 0, i * 16, 0, 16, 16, 0)

        # Draw brush size selectors
        for i, size in enumerate(SIZES):
            # Calculate the base position for this brush size selector (top-left corner)
            x = 256 - (len(SIZES) - i) * 16
            y = toolbar_y

            # Calculate the center of the 16x16 area
            center_x = x + 8
            center_y = y + 8

            # Only highlight the selected size with 15x15 indicator
            if size == self.current_size:
                # Draw selection box (15x15)
                pyxel.rectb(x + 1, y + 1, 14, 14, 7)

            # Make sure circles are perfectly centered within the 15x15 selection box
            # For a circle with radius r, the diameter is 2r+1 pixels
            # The selection box is 15x15, so the max diameter should be 13 (leaving 1px on each side)
            # Therefore max radius is 6 (for a 13 pixel diameter)
            display_sizes = [1, 2, 4, 6]  # Adjusted for perfect centering
            display_size = display_sizes[i]

            # Draw filled circle with current color (perfectly centered)
            pyxel.circ(center_x, center_y, display_size, self.current_color)

            # Draw black outline around the circle
            pyxel.circb(center_x, center_y, display_size, 0)

        # Draw either color palette or stamp palette based on current tool
        if self.current_tool == TOOL_STAMP:
            self.draw_stamp_palette(toolbar_y + 16)
        else:
            self.draw_color_palette(toolbar_y + 16)

        # Preview for shape tools
        if self.drawing and pyxel.mouse_y < CANVAS_HEIGHT:
            if self.current_tool == TOOL_LINE:
                pyxel.line(
                    self.start_x,
                    self.start_y,
                    pyxel.mouse_x,
                    pyxel.mouse_y,
                    self.current_color,
                )
            elif self.current_tool == TOOL_RECT:
                x1, y1 = self.start_x, self.start_y
                x2, y2 = pyxel.mouse_x, pyxel.mouse_y

                # Make sure x1,y1 is top-left and x2,y2 is bottom-right
                if x1 > x2:
                    x1, x2 = x2, x1
                if y1 > y2:
                    y1, y2 = y2, y1

                pyxel.rectb(x1, y1, x2 - x1 + 1, y2 - y1 + 1, self.current_color)
            elif self.current_tool == TOOL_CIRCLE:
                x1, y1 = self.start_x, self.start_y
                x2, y2 = pyxel.mouse_x, pyxel.mouse_y
                radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
                pyxel.circb(x1, y1, radius, self.current_color)
            elif self.current_tool == TOOL_STAMP:
                # Show stamp preview at cursor position
                sx, sy = STAMPS[self.current_stamp]
                pyxel.blt(pyxel.mouse_x - 8, pyxel.mouse_y - 8, 0, sx, sy, 16, 16, 0)

    def draw_color_palette(self, y):
        # Draw left arrow button
        pyxel.rectb(1, y + 1, 14, 14, 0)  # Black outline
        pyxel.line(10, y + 8, 5, y + 8, 7)  # Arrow horizontal
        pyxel.line(5, y + 8, 8, y + 5, 7)  # Arrow top
        pyxel.line(5, y + 8, 8, y + 11, 7)  # Arrow bottom

        # Draw right arrow button
        pyxel.rectb(241, y + 1, 14, 14, 0)  # Black outline
        pyxel.line(246, y + 8, 251, y + 8, 7)  # Arrow horizontal
        pyxel.line(251, y + 8, 248, y + 5, 7)  # Arrow top
        pyxel.line(251, y + 8, 248, y + 11, 7)  # Arrow bottom

        # Draw palette layer indicator (small dots at the bottom)
        for i in range(self.num_palettes):
            dot_x = 128 - (self.num_palettes * 4) + i * 8
            dot_color = 7 if i == self.current_palette else 5
            pyxel.rect(dot_x, y + 13, 3, 2, dot_color)

        # Draw color palette (14 colors between the arrows)
        colors = COLOR_PALETTES[self.current_palette]
        for i, color in enumerate(colors):
            x = 16 + i * 16

            # Draw border (black by default, white if selected)
            outline_color = 7 if color == self.current_color else 0
            pyxel.rectb(x + 1, y + 1, 14, 14, outline_color)

            # Draw color sample (14x14)
            pyxel.rect(x + 2, y + 2, 12, 12, color)

    def draw_stamp_palette(self, y):
        # Draw left arrow button
        pyxel.rectb(1, y + 1, 14, 14, 0)  # Black outline
        pyxel.line(10, y + 8, 5, y + 8, 7)  # Arrow horizontal
        pyxel.line(5, y + 8, 8, y + 5, 7)  # Arrow top
        pyxel.line(5, y + 8, 8, y + 11, 7)  # Arrow bottom

        # Draw right arrow button
        pyxel.rectb(241, y + 1, 14, 14, 0)  # Black outline
        pyxel.line(246, y + 8, 251, y + 8, 7)  # Arrow horizontal
        pyxel.line(251, y + 8, 248, y + 5, 7)  # Arrow top
        pyxel.line(251, y + 8, 248, y + 11, 7)  # Arrow bottom

        # Draw stamps between the arrows
        for i in range(14):  # Show 14 stamps at a time
            stamp_idx = i
            if stamp_idx < len(STAMPS):
                x = 16 + i * 16
                sx, sy = STAMPS[stamp_idx]

                # Draw border (white if selected)
                outline_color = 7 if stamp_idx == self.current_stamp else 0
                pyxel.rectb(x + 1, y + 1, 14, 14, outline_color)

                # Draw stamp
                pyxel.blt(x + 1, y + 1, 0, sx, sy, 14, 14, 0)


BunnyPyx()
