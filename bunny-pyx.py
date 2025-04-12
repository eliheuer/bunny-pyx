# Bunny Pyx
import pyxel

# Woskspace constants
CANVAS_WIDTH = 256
CANVAS_HEIGHT = 128
TOOLBAR_HEIGHT = 32

# Tool constants
TOOL_PENCIL = 0
TOOL_BRUSH = 1
TOOL_ERASER = 2
TOOL_FILL = 3
TOOL_LINE = 4
TOOL_RECT = 5
TOOL_CIRCLE = 6
TOOL_CLEAR = 7

# Number of tools in toolbar
NUM_TOOLS = 8

# Brush sizes
SIZES = [1, 2, 4, 8]

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
            # Color selection (bottom row)
            if pyxel.mouse_y > toolbar_y + 16 and pyxel.mouse_y < toolbar_y + 32:
                col = pyxel.mouse_x // 16
                if 0 <= col < 16:
                    self.current_color = col
            # Tool selection (top row of toolbar)
            elif pyxel.mouse_y > toolbar_y and pyxel.mouse_y < toolbar_y + 16:
                col = pyxel.mouse_x // 16
                if 0 <= col < NUM_TOOLS:
                    self.current_tool = col
                    
                # Size selection (right side)
                size_idx = (pyxel.mouse_x - (256 - len(SIZES)*16)) // 16
                if (256 - len(SIZES)*16) <= pyxel.mouse_x < 256 and 0 <= size_idx < len(SIZES):
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
                if self.current_tool == TOOL_FILL:
                    pyxel.image(1).cls(self.current_color)
            
            # Continue drawing
            elif pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and self.drawing:
                if self.current_tool in (TOOL_PENCIL, TOOL_BRUSH, TOOL_ERASER):
                    color = 0 if self.current_tool == TOOL_ERASER else self.current_color
                    size = self.current_size * 2 if self.current_tool == TOOL_BRUSH else self.current_size
                    
                    # Draw line between old position and new position
                    pyxel.image(1).line(
                        self.old_x, self.old_y, 
                        pyxel.mouse_x, pyxel.mouse_y, 
                        color
                    )
                    
                    # For brush, make thicker line
                    if self.current_tool == TOOL_BRUSH:
                        for dx in range(-size//2, size//2 + 1):
                            for dy in range(-size//2, size//2 + 1):
                                if dx*dx + dy*dy <= (size//2)*(size//2):
                                    pyxel.image(1).line(
                                        self.old_x + dx, self.old_y + dy,
                                        pyxel.mouse_x + dx, pyxel.mouse_y + dy,
                                        color
                                    )
            
            # End drawing
            elif pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) and self.drawing:
                self.drawing = False
                
                # Line, rectangle and circle shapes finalize when mouse is released
                if self.current_tool == TOOL_LINE:
                    pyxel.image(1).line(
                        self.start_x, self.start_y,
                        pyxel.mouse_x, pyxel.mouse_y,
                        self.current_color
                    )
                elif self.current_tool == TOOL_RECT:
                    x1, y1 = self.start_x, self.start_y
                    x2, y2 = pyxel.mouse_x, pyxel.mouse_y
                    
                    # Make sure x1,y1 is top-left and x2,y2 is bottom-right
                    if x1 > x2:
                        x1, x2 = x2, x1
                    if y1 > y2:
                        y1, y2 = y2, y1
                    
                    pyxel.image(1).rect(x1, y1, x2 - x1 + 1, y2 - y1 + 1, self.current_color)
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
        size = self.current_size * 2 if self.current_tool == TOOL_BRUSH else self.current_size
        
        if self.current_tool == TOOL_BRUSH:
            pyxel.image(1).circ(x, y, size // 2, color)
        else:
            pyxel.image(1).rect(
                x - size // 2, 
                y - size // 2, 
                size, 
                size, 
                color
            )
        
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
            
            # Highlight selected tool
            if i == self.current_tool:
                pyxel.rectb(x, y, 16, 16, 7)
            
            # Draw the icon from sprite sheet (image 0)
            pyxel.blt(x, y, 0, i * 16, 0, 16, 16, 0)
        
        # Draw brush size selectors
        for i, size in enumerate(SIZES):
            x = 256 - (len(SIZES) - i) * 16
            y = toolbar_y
            
            # Only highlight the selected size
            if size == self.current_size:
                pyxel.rectb(x, y, 16, 16, 7)
                
            pyxel.circ(x + 8, y + 8, size // 2, 7)
        
        # Draw color palette (using 16x16 squares)
        for i in range(16):
            x = i * 16
            y = toolbar_y + 16
            pyxel.rect(x, y, 16, 16, i)
            
            # Highlight selected color
            if i == self.current_color:
                pyxel.rectb(x, y, 16, 16, 7)
                
        # Preview for shape tools
        if self.drawing and pyxel.mouse_y < CANVAS_HEIGHT:
            if self.current_tool == TOOL_LINE:
                pyxel.line(
                    self.start_x, self.start_y,
                    pyxel.mouse_x, pyxel.mouse_y,
                    self.current_color
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

BunnyPyx() 
