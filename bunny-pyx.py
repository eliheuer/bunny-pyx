# Bunny Pyx
# (\(\
# ( -.-)
# o_(")(")
import pyxel

# Woskspace widths & heights
CANVAS_WIDTH = 256
CANVAS_HEIGHT = 128
TOOLBAR_HEIGHT = 32

# Tool numbers
TOOL_PENCIL = 0
TOOL_BRUSH = 1
TOOL_ERASER = 2
TOOL_FILL = 3
TOOL_LINE = 4
TOOL_RECT = 5
TOOL_CIRCLE = 6
TOOL_CLEAR = 7
TOOL_STAMP = 8
TOOL_ALGO_BRUSH = 9
TOOL_TYPE = 10
TOOL_FILTER = 11

# Number of tools in toolbar
NUM_TOOLS = 12

# Brush sizes
SIZES = [2, 4, 8, 14]

# Brush size icons - coordinates in the resource file (image 0)
# These should be created in the pyxres file with a purple center (color 2)
BRUSH_SIZE_ICONS = [
    (0, 32),   # Small brush icon
    (16, 32),  # Medium brush icon
    (32, 32),  # Large brush icon
    (48, 32),  # Extra large brush icon
]

# Color palette layers.
# Each layer has 14 colors,
# to leave room for two navigation buttons.
COLOR_PALETTES = [
    # Layer 1: Default Pyxel colors (minus the last two)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    # Layer 2: Last two colors from layer 1 + rainbow colors
    [14, 15, 8, 9, 10, 11, 12, 3, 1, 2, 4, 5, 6, 7],
    # Layer 3: Grayscale
    [0, 0, 5, 5, 6, 6, 7, 7, 7, 6, 6, 5, 5, 0],
]

# Stamp images
# Array of (x, y) coordinates for the stamps in the resource file
STAMPS = [
    (0, 240),
    (16, 240),
    (32, 240),
    (48, 240),
    (64, 240),
    (80, 240),
    (96, 240),
]

# Algorithmic brush types
ALGO_RANDOM_CIRCLES = 0
ALGO_ROTATING_LINES = 1
ALGO_LOOPS = 2
ALGO_SPIRALS = 3
ALGO_SQUARES = 4
ALGO_STARS = 5
ALGO_CONFETTI = 6
ALGO_WAVES = 7

# Algorithmic brush icons (x, y) coordinates in resource file
# For now they are placeholders until proper icons are added
ALGO_BRUSH_ICONS = [
    (0, 16),  # Random Circles
    (0, 16),  # Rotating Lines
    (0, 16),  # Loops
    (0, 16),  # Spirals
    (0, 16),  # Squares
    (0, 16),  # Stars
    (0, 16),  # Confetti
    (0, 16),   # Waves
]

# Character icons for the type tool
# These are placeholder coordinates for now
# Will be replaced with actual character graphics
CHARS = [
    # Latin uppercase alphabet
    (0, 48),  # A
    (16, 48),  # B
    (32, 48),  # C
    (48, 48),  # D
    (64, 48),  # E
    (80, 32),  # F
    (96, 32),  # G
    (112, 32),  # H
    (128, 32),  # I
    (144, 32),  # J
    (160, 32),  # K
    (176, 32),  # L
    (192, 32),  # M
    (208, 32),  # N
    (224, 32),  # O
    (240, 32),  # P
    (0, 48),  # Q
    (16, 48),  # R
    (32, 48),  # S
    (48, 48),  # T
    (64, 48),  # U
    (80, 48),  # V
    (96, 48),  # W
    (112, 48),  # X
    (128, 48),  # Y
    (144, 48),  # Z
    
    # Numbers
    (160, 48),  # 0
    (176, 48),  # 1
    (192, 48),  # 2
    (208, 48),  # 3
    (224, 48),  # 4
    (240, 48),  # 5
    (0, 64),  # 6
    (16, 64),  # 7
    (32, 64),  # 8
    (48, 64),  # 9
    
    # Symbols
    (64, 64),  # .
    (80, 64),  # ,
    (96, 64),  # !
    (112, 64),  # ?
    (128, 64),  # :
    (144, 64),  # ;
    (160, 64),  # (
    (176, 64),  # )
    (192, 64),  # [
    (208, 64),  # ]
    (224, 64),  # {
    (240, 64),  # }
    (0, 80),  # +
    (16, 80),  # -
    (32, 80),  # *
    (48, 80),  # /
]

# Filter types
FILTER_INVERT = 0
FILTER_GRAYSCALE = 1
FILTER_FLIP_X = 2
FILTER_FLIP_Y = 3
FILTER_ROTATE_90 = 4
FILTER_WAVE = 5
FILTER_PIXELATE = 6
FILTER_BLUR = 7

# Filter icons (x, y) coordinates in resource file
# For now they are placeholders until proper icons are added
FILTER_ICONS = [
    (0, 16),  # Invert
    (0, 16),  # Grayscale
    (0, 16),  # Flip X
    (0, 16),  # Flip Y
    (0, 16),  # Rotate 90
    (0, 16),  # Wave
    (0, 16),  # Pixelate
    (0, 16),  # Blur
]


class BunnyPyx:
    def __init__(self):
        pyxel.init(256, 160, title="Bunny Pyx")
        pyxel.load("assets/bunny-pyx.pyxres")
        pyxel.mouse(False)  # Hide the system mouse cursor

        # Initialize canvas
        self.current_tool = TOOL_PENCIL
        self.current_color = 7  # White3333
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
        
        # Initialize algorithmic brush
        self.current_algo_brush = 0
        self.num_algo_brushes = len(ALGO_BRUSH_ICONS)
        self.algo_brush_angle = 0  # For rotating brushes
        self.algo_brush_step = 0   # For incremental patterns
        
        # Initialize type tool
        self.current_char = 0
        self.num_chars = len(CHARS)
        
        # Initialize filter tool
        self.current_filter = 0
        self.num_filters = len(FILTER_ICONS)
        
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
            # Color/Stamp/Algo palette row interaction
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
                elif self.current_tool == TOOL_ALGO_BRUSH:
                    # Algorithmic brush selection mode
                    # Left arrow button (first position)
                    if 0 <= pyxel.mouse_x < 16:
                        self.current_algo_brush = (self.current_algo_brush - 1) % self.num_algo_brushes
                    # Right arrow button (last position)
                    elif 240 <= pyxel.mouse_x < 256:
                        self.current_algo_brush = (self.current_algo_brush + 1) % self.num_algo_brushes
                    # Brush selection (positions 1-14)
                    else:
                        brush_idx = (pyxel.mouse_x - 16) // 16
                        if 0 <= brush_idx < self.num_algo_brushes:  # Only select valid brushes
                            self.current_algo_brush = brush_idx
                elif self.current_tool == TOOL_TYPE:
                    # Character selection mode
                    # Left arrow button (first position)
                    if 0 <= pyxel.mouse_x < 16:
                        self.current_char = (self.current_char - 1) % self.num_chars
                    # Right arrow button (last position)
                    elif 240 <= pyxel.mouse_x < 256:
                        self.current_char = (self.current_char + 1) % self.num_chars
                    # Character selection (positions 1-14)
                    else:
                        char_idx = (pyxel.mouse_x - 16) // 16
                        if 0 <= char_idx < 14:  # Only 14 visible chars at once
                            # Calculate the actual index based on potential multiple pages
                            actual_idx = char_idx
                            if actual_idx < self.num_chars:
                                self.current_char = actual_idx
                elif self.current_tool == TOOL_FILTER:
                    # Filter selection mode
                    # Left arrow button (first position)
                    if 0 <= pyxel.mouse_x < 16:
                        self.current_filter = (self.current_filter - 1) % self.num_filters
                    # Right arrow button (last position)
                    elif 240 <= pyxel.mouse_x < 256:
                        self.current_filter = (self.current_filter + 1) % self.num_filters
                    # Filter selection (positions 1-14)
                    else:
                        filter_idx = (pyxel.mouse_x - 16) // 16
                        if 0 <= filter_idx < self.num_filters:
                            self.current_filter = filter_idx
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
                    # Play sound when changing tools
                    if self.current_tool != col:
                        pyxel.play(0, 4)  # Play sound 4 on channel 0
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
                    if self.current_tool == TOOL_PENCIL:
                        pyxel.play(0, 0)  # Play sound 1 on channel 0
                
                # Fill bucket tool
                elif self.current_tool == TOOL_FILL:
                    pyxel.image(1).cls(self.current_color)
                    pyxel.play(0, 0)  # Play sound 1 on channel 0
                
                # Stamp tool - stamp immediately
                elif self.current_tool == TOOL_STAMP:
                    self.stamp_image(pyxel.mouse_x, pyxel.mouse_y)
                
                # Algorithmic brush - apply immediately
                elif self.current_tool == TOOL_ALGO_BRUSH:
                    self.apply_algo_brush(pyxel.mouse_x, pyxel.mouse_y)
                
                # Type tool - place character immediately
                elif self.current_tool == TOOL_TYPE:
                    self.place_char(pyxel.mouse_x, pyxel.mouse_y)
                
                # Filter tool - apply filter immediately
                elif self.current_tool == TOOL_FILTER:
                    self.apply_filter(pyxel.mouse_x, pyxel.mouse_y)
            
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
                    
                    # Play sound for pencil tool, but not continuously - only every few frames
                    if self.current_tool == TOOL_PENCIL and pyxel.frame_count % 6 == 0:
                        pyxel.play(0, 1)  # Play sound 1 on channel 0
                elif self.current_tool == TOOL_STAMP:
                    # Allow continuous stamping while dragging, with minimal delay
                    if pyxel.frame_count % 2 == 0:  # Reduced from 8 to 2 frames
                        self.stamp_image(pyxel.mouse_x, pyxel.mouse_y)
                elif self.current_tool == TOOL_ALGO_BRUSH:
                    # Apply algorithmic brush with each movement
                    self.apply_algo_brush(pyxel.mouse_x, pyxel.mouse_y)
                elif self.current_tool == TOOL_TYPE:
                    # Allow continuous character placement while dragging, with delay
                    if pyxel.frame_count % 6 == 0:  # Slightly slower than stamps
                        self.place_char(pyxel.mouse_x, pyxel.mouse_y)
                # Note: Filter tool only applies on initial click, not during drag
            
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
            # Use the brush size as the diameter (radius = size/2)
            pyxel.image(1).circ(x, y, size // 2, color)
        else:
            # For other tools like pencil, center the square properly
            # For even-numbered sizes, we need to offset by size/2
            offset = size // 2
            pyxel.image(1).rect(x - offset, y - offset, size, size, color)

    def stamp_image(self, x, y):
        # Get stamp coordinates
        sx, sy = STAMPS[self.current_stamp]

        # Center the stamp on the mouse position
        dest_x = x - 8
        dest_y = y - 8

        # Copy the stamp to the canvas with transparency (color 0)
        pyxel.image(1).blt(dest_x, dest_y, 0, sx, sy, 16, 16, 0)
        
        # Play sound effect when stamping
        pyxel.play(0, 0)  # Play sound 0 on channel 0
    
    def place_char(self, x, y):
        # Get character coordinates
        sx, sy = CHARS[self.current_char]

        # Center the character on the mouse position
        dest_x = x - 8
        dest_y = y - 8

        # Copy the character to the canvas with transparency (color 0)
        pyxel.image(1).blt(dest_x, dest_y, 0, sx, sy, 16, 16, 0)
        
        # Play sound effect when placing a character
        pyxel.play(0, 0)  # Play sound 0 on channel 0
    
    def apply_filter(self, x, y):
        # Apply the selected filter to the entire canvas
        if self.current_filter == FILTER_INVERT:
            self.filter_invert()
        elif self.current_filter == FILTER_GRAYSCALE:
            self.filter_grayscale()
        elif self.current_filter == FILTER_FLIP_X:
            self.filter_flip_x()
        elif self.current_filter == FILTER_FLIP_Y:
            self.filter_flip_y()
        elif self.current_filter == FILTER_ROTATE_90:
            self.filter_rotate_90()
        elif self.current_filter == FILTER_WAVE:
            self.filter_wave()
        elif self.current_filter == FILTER_PIXELATE:
            self.filter_pixelate()
        elif self.current_filter == FILTER_BLUR:
            self.filter_blur()
            
        # Play sound when a filter is applied
        pyxel.play(0, 2)  # Play sound 2 on channel 0
    
    def filter_invert(self):
        # Create a temporary image to store the inverted result
        temp_img = pyxel.Image(CANVAS_WIDTH, CANVAS_HEIGHT)
        
        # Invert each pixel color
        for y in range(CANVAS_HEIGHT):
            for x in range(CANVAS_WIDTH):
                col = pyxel.image(1).pget(x, y)
                if col != 0:  # Don't invert transparent pixels
                    # Simple inversion - this could be improved with a proper color map
                    temp_img.pset(x, y, 15 - col)
                else:
                    temp_img.pset(x, y, 0)
        
        # Copy the result back to the canvas
        for y in range(CANVAS_HEIGHT):
            for x in range(CANVAS_WIDTH):
                pyxel.image(1).pset(x, y, temp_img.pget(x, y))
    
    def filter_grayscale(self):
        # Create a grayscale mapping for the Pyxel color palette
        # This is a simplified mapping - could be improved with actual luminance values
        gray_map = [0, 5, 5, 6, 5, 5, 6, 7, 5, 6, 5, 6, 6, 7, 13, 7]
        
        # Apply grayscale to each pixel
        for y in range(CANVAS_HEIGHT):
            for x in range(CANVAS_WIDTH):
                col = pyxel.image(1).pget(x, y)
                if col != 0:  # Don't convert transparent pixels
                    pyxel.image(1).pset(x, y, gray_map[col])
    
    def filter_flip_x(self):
        # Create a temporary image to store the flipped result
        temp_img = pyxel.Image(CANVAS_WIDTH, CANVAS_HEIGHT)
        
        # Copy pixels in horizontally flipped order
        for y in range(CANVAS_HEIGHT):
            for x in range(CANVAS_WIDTH):
                temp_img.pset(CANVAS_WIDTH - 1 - x, y, pyxel.image(1).pget(x, y))
        
        # Copy the result back to the canvas
        for y in range(CANVAS_HEIGHT):
            for x in range(CANVAS_WIDTH):
                pyxel.image(1).pset(x, y, temp_img.pget(x, y))
    
    def filter_flip_y(self):
        # Create a temporary image to store the flipped result
        temp_img = pyxel.Image(CANVAS_WIDTH, CANVAS_HEIGHT)
        
        # Copy pixels in vertically flipped order
        for y in range(CANVAS_HEIGHT):
            for x in range(CANVAS_WIDTH):
                temp_img.pset(x, CANVAS_HEIGHT - 1 - y, pyxel.image(1).pget(x, y))
        
        # Copy the result back to the canvas
        for y in range(CANVAS_HEIGHT):
            for x in range(CANVAS_WIDTH):
                pyxel.image(1).pset(x, y, temp_img.pget(x, y))
    
    def filter_rotate_90(self):
        # Create a temporary image to store the rotated result
        temp_img = pyxel.Image(CANVAS_HEIGHT, CANVAS_WIDTH)  # Note the swapped dimensions
        
        # Copy pixels in rotated order (90 degrees clockwise)
        for y in range(CANVAS_HEIGHT):
            for x in range(CANVAS_WIDTH):
                temp_img.pset(CANVAS_HEIGHT - 1 - y, x, pyxel.image(1).pget(x, y))
        
        # The rotated image might be larger than our canvas due to aspect ratio
        # We'll center it and crop to fit
        offset_x = (CANVAS_WIDTH - CANVAS_HEIGHT) // 2
        offset_y = (CANVAS_HEIGHT - CANVAS_WIDTH) // 2
        
        # Clear the original image
        pyxel.image(1).cls(0)
        
        # Copy the rotated content back, centered
        for y in range(min(CANVAS_WIDTH, CANVAS_HEIGHT)):
            for x in range(min(CANVAS_WIDTH, CANVAS_HEIGHT)):
                if 0 <= x + offset_x < CANVAS_WIDTH and 0 <= y + offset_y < CANVAS_HEIGHT:
                    pyxel.image(1).pset(x + offset_x, y + offset_y, temp_img.pget(x, y))
    
    def filter_wave(self):
        # Create a temporary image to store the wave result
        temp_img = pyxel.Image(CANVAS_WIDTH, CANVAS_HEIGHT)
        
        # Copy the original image to the temporary image
        for y in range(CANVAS_HEIGHT):
            for x in range(CANVAS_WIDTH):
                temp_img.pset(x, y, pyxel.image(1).pget(x, y))
        
        # Apply a sine wave distortion to the vertical position
        amplitude = 4  # Wave amplitude
        frequency = 0.05  # Wave frequency
        
        # Clear the original image
        pyxel.image(1).cls(0)
        
        # Apply the wave effect
        for y in range(CANVAS_HEIGHT):
            for x in range(CANVAS_WIDTH):
                # Calculate the wave offset for this column
                offset = int(amplitude * pyxel.sin(x * frequency * 360))
                
                # Get y position with wave effect (and wrap around)
                wave_y = (y + offset) % CANVAS_HEIGHT
                
                # Copy the pixel with the wave effect applied
                pyxel.image(1).pset(x, y, temp_img.pget(x, wave_y))
    
    def filter_pixelate(self):
        # Create a temporary image to store the original
        temp_img = pyxel.Image(CANVAS_WIDTH, CANVAS_HEIGHT)
        
        # Copy the original image to the temporary image
        for y in range(CANVAS_HEIGHT):
            for x in range(CANVAS_WIDTH):
                temp_img.pset(x, y, pyxel.image(1).pget(x, y))
        
        # Pixelation block size
        block_size = 4
        
        # Apply pixelation effect
        for block_y in range(0, CANVAS_HEIGHT, block_size):
            for block_x in range(0, CANVAS_WIDTH, block_size):
                # Determine the dominant color in this block
                colors = {}
                for y in range(block_size):
                    for x in range(block_size):
                        px = block_x + x
                        py = block_y + y
                        if px < CANVAS_WIDTH and py < CANVAS_HEIGHT:
                            color = temp_img.pget(px, py)
                            if color != 0:  # Ignore transparent pixels
                                colors[color] = colors.get(color, 0) + 1
                
                # Find the most common color
                dominant_color = 0
                if colors:
                    dominant_color = max(colors, key=colors.get)
                
                # Set the entire block to the dominant color
                for y in range(block_size):
                    for x in range(block_size):
                        px = block_x + x
                        py = block_y + y
                        if px < CANVAS_WIDTH and py < CANVAS_HEIGHT:
                            if temp_img.pget(px, py) != 0:  # Only change non-transparent pixels
                                pyxel.image(1).pset(px, py, dominant_color)
    
    def filter_blur(self):
        # Create a temporary image to store the original
        temp_img = pyxel.Image(CANVAS_WIDTH, CANVAS_HEIGHT)
        
        # Copy the original image to the temporary image
        for y in range(CANVAS_HEIGHT):
            for x in range(CANVAS_WIDTH):
                temp_img.pset(x, y, pyxel.image(1).pget(x, y))
        
        # Apply a simple box blur
        kernel_size = 3
        half_kernel = kernel_size // 2
        
        for y in range(CANVAS_HEIGHT):
            for x in range(CANVAS_WIDTH):
                # Skip transparent pixels
                if temp_img.pget(x, y) == 0:
                    continue
                
                # Count colors in the kernel
                colors = {}
                for ky in range(-half_kernel, half_kernel + 1):
                    for kx in range(-half_kernel, half_kernel + 1):
                        nx, ny = x + kx, y + ky
                        if 0 <= nx < CANVAS_WIDTH and 0 <= ny < CANVAS_HEIGHT:
                            col = temp_img.pget(nx, ny)
                            if col != 0:  # Ignore transparent pixels
                                colors[col] = colors.get(col, 0) + 1
                
                # Find the average color (or most common)
                if colors:
                    avg_color = max(colors, key=colors.get)
                    pyxel.image(1).pset(x, y, avg_color)

    def apply_algo_brush(self, x, y):
        # Apply the selected algorithmic brush pattern
        if self.current_algo_brush == ALGO_RANDOM_CIRCLES:
            self.draw_random_circles(x, y)
        elif self.current_algo_brush == ALGO_ROTATING_LINES:
            self.draw_rotating_lines(x, y)
        elif self.current_algo_brush == ALGO_LOOPS:
            self.draw_loops(x, y, self.old_x, self.old_y)
        elif self.current_algo_brush == ALGO_SPIRALS:
            self.draw_spirals(x, y)
        elif self.current_algo_brush == ALGO_SQUARES:
            self.draw_squares(x, y)
        elif self.current_algo_brush == ALGO_STARS:
            self.draw_stars(x, y)
        elif self.current_algo_brush == ALGO_CONFETTI:
            self.draw_confetti(x, y)
        elif self.current_algo_brush == ALGO_WAVES:
            self.draw_waves(x, y, self.old_x, self.old_y)
        
        # Update the brush state
        self.algo_brush_angle = (self.algo_brush_angle + 10) % 360
        self.algo_brush_step += 1
    
    def draw_random_circles(self, x, y):
        # Draw 3-5 circles of random sizes and colors
        for _ in range(pyxel.rndi(3, 5)):
            # Random position near the cursor
            cx = x + pyxel.rndi(-10, 10)
            cy = y + pyxel.rndi(-10, 10)
            # Random radius
            radius = pyxel.rndi(1, 8)
            # Random color from the current palette
            color = COLOR_PALETTES[self.current_palette][pyxel.rndi(0, 13)]
            # Random filled or outlined
            if pyxel.rndi(0, 1) == 0:
                pyxel.image(1).circ(cx, cy, radius, color)
            else:
                pyxel.image(1).circb(cx, cy, radius, color)
    
    def draw_rotating_lines(self, x, y):
        # Draw lines radiating from the center with rotation
        num_lines = 8
        length = 12
        for i in range(num_lines):
            angle = self.algo_brush_angle + (i * 360 / num_lines)
            angle_rad = angle * 3.14159 / 180
            ex = x + length * pyxel.cos(angle_rad)
            ey = y + length * pyxel.sin(angle_rad)
            color = COLOR_PALETTES[self.current_palette][(i + self.algo_brush_step) % 14]
            pyxel.image(1).line(x, y, ex, ey, color)
    
    def draw_loops(self, x, y, old_x, old_y):
        # Draw loopy patterns following the mouse path
        if old_x == 0 and old_y == 0:
            return
            
        # Calculate the midpoint between current and previous position
        mid_x = (x + old_x) // 2
        mid_y = (y + old_y) // 2
        
        # Add some controlled randomness
        offset_x = pyxel.rndi(-5, 5)
        offset_y = pyxel.rndi(-5, 5)
        
        # Draw a bezier-like curve
        color = COLOR_PALETTES[self.current_palette][self.algo_brush_step % 14]
        pyxel.image(1).line(old_x, old_y, mid_x + offset_x, mid_y + offset_y, color)
        pyxel.image(1).line(mid_x + offset_x, mid_y + offset_y, x, y, color)
    
    def draw_spirals(self, x, y):
        # Draw spiral shapes
        turns = 3
        points = 20
        radius_step = 0.3
        start_angle = self.algo_brush_angle
        
        color = COLOR_PALETTES[self.current_palette][self.algo_brush_step % 14]
        
        for i in range(points):
            angle = start_angle + (i * turns * 360 / points)
            angle_rad = angle * 3.14159 / 180
            radius = i * radius_step
            px = x + radius * pyxel.cos(angle_rad)
            py = y + radius * pyxel.sin(angle_rad)
            
            if i > 0:
                pyxel.image(1).line(prev_x, prev_y, px, py, color)
                
            prev_x, prev_y = px, py
    
    def draw_squares(self, x, y):
        # Draw nested squares
        max_size = 16
        min_size = 2
        step = 2
        
        for i in range(0, max_size, step):
            size = max_size - i
            if size < min_size:
                break
                
            color = COLOR_PALETTES[self.current_palette][(i + self.algo_brush_step) % 14]
            half_size = size // 2
            pyxel.image(1).rectb(
                x - half_size, 
                y - half_size, 
                size, 
                size, 
                color
            )
    
    def draw_stars(self, x, y):
        # Draw a star shape
        num_points = 5
        inner_radius = 3
        outer_radius = 8
        color = COLOR_PALETTES[self.current_palette][self.algo_brush_step % 14]
        
        # Calculate star points
        points = []
        for i in range(num_points * 2):
            angle = self.algo_brush_angle + (i * 360 / (num_points * 2))
            angle_rad = angle * 3.14159 / 180
            radius = outer_radius if i % 2 == 0 else inner_radius
            px = x + radius * pyxel.cos(angle_rad)
            py = y + radius * pyxel.sin(angle_rad)
            points.append((px, py))
        
        # Connect the points
        for i in range(len(points)):
            j = (i + 1) % len(points)
            pyxel.image(1).line(points[i][0], points[i][1], points[j][0], points[j][1], color)
    
    def draw_confetti(self, x, y):
        # Draw tiny colored squares like confetti
        for _ in range(20):
            # Random position near the cursor
            cx = x + pyxel.rndi(-15, 15)
            cy = y + pyxel.rndi(-15, 15)
            # Random size
            size = pyxel.rndi(1, 3)
            # Random color
            color = COLOR_PALETTES[self.current_palette][pyxel.rndi(0, 13)]
            # Draw the confetti piece
            pyxel.image(1).rect(cx, cy, size, size, color)
    
    def draw_waves(self, x, y, old_x, old_y):
        # Draw wavy patterns
        if old_x == 0 and old_y == 0:
            return
            
        # Calculate the distance and direction vector
        dx = x - old_x
        dy = y - old_y
        dist = ((dx * dx) + (dy * dy)) ** 0.5
        
        if dist < 1:
            return
            
        # Normalize the vector
        dx = dx / dist
        dy = dy / dist
        
        # Calculate perpendicular vector for wave effect
        perp_x = -dy
        perp_y = dx
        
        # Draw the wave pattern
        num_segments = 10
        segment_length = dist / num_segments
        amplitude = 5 * pyxel.sin(self.algo_brush_step * 0.1)
        
        for i in range(num_segments):
            t1 = i / num_segments
            t2 = (i + 1) / num_segments
            
            # Wave amplitude oscillates along the path
            wave_factor1 = amplitude * pyxel.sin(t1 * 3.14159 * 2 + self.algo_brush_step * 0.2)
            wave_factor2 = amplitude * pyxel.sin(t2 * 3.14159 * 2 + self.algo_brush_step * 0.2)
            
            # Start and end points with wave offset
            x1 = old_x + dx * (dist * t1) + perp_x * wave_factor1
            y1 = old_y + dy * (dist * t1) + perp_y * wave_factor1
            x2 = old_x + dx * (dist * t2) + perp_x * wave_factor2
            y2 = old_y + dy * (dist * t2) + perp_y * wave_factor2
            
            # Draw the segment
            color = COLOR_PALETTES[self.current_palette][(i + self.algo_brush_step) % 14]
            pyxel.image(1).line(x1, y1, x2, y2, color)

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

            # Highlight selected tool with yellow background
            if i == self.current_tool:
                pyxel.rect(x, y, 16, 16, 10)  # Yellow background

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

            # Highlight selected size with yellow background
            if size == self.current_size:
                pyxel.rect(x, y, 16, 16, 10)  # Yellow background

            # Get the brush size icon based on index
            sx, sy = BRUSH_SIZE_ICONS[i]
            
            # Draw the brush size icon with color replacement
            # This replaces color 2 (purple) with the current color
            # The last parameter is the color key for transparency (0)
            # Color 2 is explicitly not included in the color key to allow it to be replaced
            colkey = 0  # Only color 0 is transparent
            
            # First draw the icon without the purple parts
            for dy in range(16):
                for dx in range(16):
                    pixel_color = pyxel.image(0).pget(sx + dx, sy + dy)
                    if pixel_color != 0 and pixel_color != 2:  # Not transparent or purple
                        pyxel.pset(x + dx, y + dy, pixel_color)
            
            # Then draw the purple parts with the current color
            for dy in range(16):
                for dx in range(16):
                    pixel_color = pyxel.image(0).pget(sx + dx, sy + dy)
                    if pixel_color == 2:  # Purple parts
                        pyxel.pset(x + dx, y + dy, self.current_color)

        # Draw appropriate palette based on current tool
        if self.current_tool == TOOL_STAMP:
            self.draw_stamp_palette(toolbar_y + 16)
        elif self.current_tool == TOOL_ALGO_BRUSH:
            self.draw_algo_brush_palette(toolbar_y + 16)
        elif self.current_tool == TOOL_TYPE:
            self.draw_type_palette(toolbar_y + 16)
        elif self.current_tool == TOOL_FILTER:
            self.draw_filter_palette(toolbar_y + 16)
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
            elif self.current_tool == TOOL_ALGO_BRUSH:
                # Show a preview of the algorithmic brush effect
                self.draw_algo_brush_preview(pyxel.mouse_x, pyxel.mouse_y)
            elif self.current_tool == TOOL_TYPE:
                # Show a preview of the selected character
                self.draw_char_preview(pyxel.mouse_x, pyxel.mouse_y)
            elif self.current_tool == TOOL_FILTER:
                # Show a preview of the selected filter effect
                self.draw_filter_preview(pyxel.mouse_x, pyxel.mouse_y)

        # Draw custom mouse cursor based on current tool
        self.draw_custom_cursor(pyxel.mouse_x, pyxel.mouse_y)

    def draw_color_palette(self, y):
        # Draw left arrow button using icon
        pyxel.blt(0, y, 0, 192, 0, 16, 16, 0)  # Left arrow icon at (192,0)

        # Draw right arrow button using icon
        pyxel.blt(240, y, 0, 208, 0, 16, 16, 0)  # Right arrow icon at (208,0)

        # Draw palette layer indicator (small dots at the bottom)
        for i in range(self.num_palettes):
            dot_x = 128 - (self.num_palettes * 4) + i * 8
            dot_color = 7 if i == self.current_palette else 5
            pyxel.rect(dot_x, y + 13, 3, 2, dot_color)

        # Draw color palette (14 colors between the arrows)
        colors = COLOR_PALETTES[self.current_palette]
        for i, color in enumerate(colors):
            x = 16 + i * 16

            # Draw yellow background for selected color
            if color == self.current_color:
                pyxel.rect(x, y, 16, 16, 10)  # Yellow background

            # Draw color sample (fill the space but leave room for outline)
            pyxel.rect(x + 2, y + 2, 12, 12, color)
            
            # Draw dark blue outline around all colors
            pyxel.rectb(x + 1, y + 1, 14, 14, 1)

    def draw_stamp_palette(self, y):
        # Draw left arrow button using icon
        pyxel.blt(0, y, 0, 192, 0, 16, 16, 0)  # Left arrow icon at (192,0)

        # Draw right arrow button using icon
        pyxel.blt(240, y, 0, 208, 0, 16, 16, 0)  # Right arrow icon at (208,0)

        # Draw stamps between the arrows
        for i in range(14):  # Show 14 stamps at a time
            stamp_idx = i
            if stamp_idx < len(STAMPS):
                x = 16 + i * 16
                sx, sy = STAMPS[stamp_idx]

                # Draw yellow background for selected stamp
                if stamp_idx == self.current_stamp:
                    pyxel.rect(x, y, 16, 16, 10)  # Yellow background

                # Draw stamp
                pyxel.blt(x, y, 0, sx, sy, 16, 16, 0)
    
    def draw_algo_brush_palette(self, y):
        # Draw left arrow button using icon
        pyxel.blt(0, y, 0, 192, 0, 16, 16, 0)  # Left arrow icon at (192,0)

        # Draw right arrow button using icon
        pyxel.blt(240, y, 0, 208, 0, 16, 16, 0)  # Right arrow icon at (208,0)

        # Draw algorithmic brush icons between the arrows
        for i in range(min(14, self.num_algo_brushes)):
            x = 16 + i * 16
            
            # For now, we're using temporary icons from the same resource file
            sx, sy = ALGO_BRUSH_ICONS[i]

            # Draw yellow background for selected brush
            if i == self.current_algo_brush:
                pyxel.rect(x, y, 16, 16, 10)  # Yellow background

            # Draw brush icon
            pyxel.blt(x, y, 0, sx, sy, 16, 16, 0)
            
            # If no icon available, draw a placeholder with text
            if i >= len(ALGO_BRUSH_ICONS):
                pyxel.rect(x + 2, y + 2, 12, 12, 5)  # Gray background
                pyxel.text(x + 4, y + 5, "B" + str(i), 7)  # White text
    
    def draw_algo_brush_preview(self, x, y):
        # Show a simplified preview of the algorithmic brush at the cursor position
        if self.current_algo_brush == ALGO_RANDOM_CIRCLES:
            # Show a simple circle preview
            pyxel.circb(x, y, 5, 7)
            pyxel.circb(x+3, y-2, 3, 8)
            pyxel.circ(x-4, y+2, 2, 11)
        elif self.current_algo_brush == ALGO_ROTATING_LINES:
            # Show rotating lines preview
            length = 6
            for i in range(4):
                angle = self.algo_brush_angle + (i * 90)
                angle_rad = angle * 3.14159 / 180
                ex = x + length * pyxel.cos(angle_rad)
                ey = y + length * pyxel.sin(angle_rad)
                pyxel.line(x, y, ex, ey, i + 8)
        elif self.current_algo_brush == ALGO_LOOPS:
            # Show loops preview
            pyxel.circb(x, y, 4, 7)
            pyxel.circb(x+3, y+3, 3, 7)
        elif self.current_algo_brush == ALGO_SPIRALS:
            # Show spiral preview
            for i in range(8):
                angle = self.algo_brush_angle + (i * 45)
                angle_rad = angle * 3.14159 / 180
                radius = i * 0.7
                px = x + radius * pyxel.cos(angle_rad)
                py = y + radius * pyxel.sin(angle_rad)
                if i > 0:
                    pyxel.line(prev_x, prev_y, px, py, 7)
                prev_x, prev_y = px, py
        elif self.current_algo_brush == ALGO_SQUARES:
            # Show squares preview
            pyxel.rectb(x-5, y-5, 11, 11, 7)
            pyxel.rectb(x-3, y-3, 7, 7, 8)
            pyxel.rectb(x-1, y-1, 3, 3, 10)
        elif self.current_algo_brush == ALGO_STARS:
            # Show star preview
            pyxel.line(x, y-5, x+3, y-1, 7)
            pyxel.line(x+3, y-1, x+5, y-5, 7)
            pyxel.line(x+5, y-5, x+1, y+1, 7)
            pyxel.line(x+1, y+1, x+3, y+5, 7)
            pyxel.line(x+3, y+5, x-1, y+2, 7)
            pyxel.line(x-1, y+2, x-5, y+4, 7)
            pyxel.line(x-5, y+4, x-3, y, 7)
            pyxel.line(x-3, y, x-5, y-4, 7)
            pyxel.line(x-5, y-4, x, y-5, 7)
        elif self.current_algo_brush == ALGO_CONFETTI:
            # Show confetti preview
            for i in range(8):
                cx = x + pyxel.sin(i * 45) * 4
                cy = y + pyxel.cos(i * 45) * 4
                pyxel.pset(cx, cy, 8 + (i % 7))
        elif self.current_algo_brush == ALGO_WAVES:
            # Show waves preview
            px = x - 5
            py = y
            for i in range(10):
                nx = x - 5 + i
                ny = y + pyxel.sin(i * 0.6 + self.algo_brush_angle * 0.1) * 3
                pyxel.line(px, py, nx, ny, 7)
                px, py = nx, ny
    
    def draw_type_palette(self, y):
        # Draw left arrow button using icon
        pyxel.blt(0, y, 0, 192, 0, 16, 16, 0)  # Left arrow icon at (192,0)

        # Draw right arrow button using icon
        pyxel.blt(240, y, 0, 208, 0, 16, 16, 0)  # Right arrow icon at (208,0)

        # Draw character palette (14 characters between the arrows)
        for i in range(14):
            char_idx = i
            if char_idx < len(CHARS):
                x = 16 + i * 16
                sx, sy = CHARS[char_idx]

                # Draw yellow background for selected character
                if char_idx == self.current_char:
                    pyxel.rect(x, y, 16, 16, 10)  # Yellow background

                # Draw character
                pyxel.blt(x, y, 0, sx, sy, 16, 16, 0)

    def draw_filter_palette(self, y):
        # Draw left arrow button using icon
        pyxel.blt(0, y, 0, 192, 0, 16, 16, 0)  # Left arrow icon at (192,0)

        # Draw right arrow button using icon
        pyxel.blt(240, y, 0, 208, 0, 16, 16, 0)  # Right arrow icon at (208,0)

        # Draw filter icons between the arrows
        for i in range(min(14, self.num_filters)):
            x = 16 + i * 16
            
            # For now, we're using temporary icons from the same resource file
            sx, sy = FILTER_ICONS[i]

            # Draw yellow background for selected filter
            if i == self.current_filter:
                pyxel.rect(x, y, 16, 16, 10)  # Yellow background

            # Draw filter icon
            pyxel.blt(x, y, 0, sx, sy, 16, 16, 0)
            
            # If no icon available, draw a placeholder with text
            if i >= len(FILTER_ICONS):
                pyxel.rect(x + 2, y + 2, 12, 12, 5)  # Gray background
                pyxel.text(x + 4, y + 5, "F" + str(i), 7)  # White text
    
    def draw_char_preview(self, x, y):
        # Show a simplified preview of the selected character
        sx, sy = CHARS[self.current_char]
        pyxel.blt(x - 8, y - 8, 0, sx, sy, 16, 16, 0)

    def draw_filter_preview(self, x, y):
        # Show a simplified preview of the selected filter effect
        if self.current_filter == FILTER_INVERT:
            # Show inverted preview
            pyxel.circb(x, y, 5, 7)
            pyxel.circb(x+3, y-2, 3, 8)
            pyxel.circ(x-4, y+2, 2, 11)
        elif self.current_filter == FILTER_GRAYSCALE:
            # Show grayscale preview
            pyxel.rectb(x-5, y-5, 11, 11, 7)
            pyxel.rectb(x-3, y-3, 7, 7, 8)
            pyxel.rectb(x-1, y-1, 3, 3, 10)
        elif self.current_filter == FILTER_FLIP_X:
            # Show flipped horizontally preview
            pyxel.circb(x, y, 5, 7)
            pyxel.circb(x+3, y-2, 3, 8)
            pyxel.circ(x-4, y+2, 2, 11)
        elif self.current_filter == FILTER_FLIP_Y:
            # Show flipped vertically preview
            pyxel.circb(x, y, 5, 7)
            pyxel.circb(x+3, y-2, 3, 8)
            pyxel.circ(x-4, y+2, 2, 11)
        elif self.current_filter == FILTER_ROTATE_90:
            # Show rotated 90 degrees preview
            pyxel.circb(x, y, 5, 7)
            pyxel.circb(x+3, y-2, 3, 8)
            pyxel.circ(x-4, y+2, 2, 11)
        elif self.current_filter == FILTER_WAVE:
            # Show wave preview
            pyxel.circb(x, y, 5, 7)
            pyxel.circb(x+3, y-2, 3, 8)
            pyxel.circ(x-4, y+2, 2, 11)
        elif self.current_filter == FILTER_PIXELATE:
            # Show pixelated preview
            pyxel.rectb(x-5, y-5, 11, 11, 7)
            pyxel.rectb(x-3, y-3, 7, 7, 8)
            pyxel.rectb(x-1, y-1, 3, 3, 10)
        elif self.current_filter == FILTER_BLUR:
            # Show blurred preview
            pyxel.rectb(x-5, y-5, 11, 11, 7)
            pyxel.rectb(x-3, y-3, 7, 7, 8)
            pyxel.rectb(x-1, y-1, 3, 3, 10)

    def draw_custom_cursor(self, x, y):
        # Use different cursors based on current tool
        if self.current_tool == TOOL_STAMP:
            # Show stamp preview at cursor position with center hotspot
            sx, sy = STAMPS[self.current_stamp]
            pyxel.blt(x - 8, y - 8, 0, sx, sy, 16, 16, 0)
        elif self.current_tool == TOOL_TYPE:
            # Show character preview with lower-left hotspot
            sx, sy = CHARS[self.current_char]
            pyxel.blt(x, y - 15, 0, sx, sy, 16, 16, 0)
        else:
            # For all other tools, position hotspot at lower-left corner
            tool_x = self.current_tool * 16
            # Place the icon so its lower-left corner is at the mouse position
            pyxel.blt(x, y - 15, 0, tool_x, 0, 16, 16, 0)


BunnyPyx()
