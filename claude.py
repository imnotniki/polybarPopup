import Xlib.display
import Xlib.X
import Xlib.XK
import Xlib.protocol.event
import pyautogui
import time

# Initialize the display
display = Xlib.display.Display()
screen = display.screen()
root = screen.root
mouse_x, mouse_y = pyautogui.position()
# Draw rectangle
rect_width = 300
rect_height = 200

# Create a window
window = root.create_window(
    mouse_x-150, mouse_y + 10, rect_width, rect_height, 0,
    screen.root_depth, Xlib.X.InputOutput, Xlib.X.CopyFromParent,
    background_pixel=screen.white_pixel,
    event_mask=Xlib.X.ExposureMask | Xlib.X.KeyPressMask,
    override_redirect=1
)

# Map the window
window.map()

# Function to draw rectangle
def draw_rectangle(x, y, width, height, color):
    gc = window.create_gc(foreground=color)
    window.fill_rectangle(gc, x, y, width, height)

# Function to draw text
def draw_text(x, y, text, color, font_size=20):
    gc = window.create_gc(foreground=color)
    font = display.open_font('fixed')
    gc.font = font  # Set the font in the graphics context
    window.draw_text(gc, x, y, text.encode('utf-8'))  # Encode the text to bytes

# Main function
def main():

    draw_rectangle(mouse_x, mouse_y, rect_width, rect_height, screen.white_pixel)

    # Draw text
    draw_text(mouse_x + 10, mouse_y + 30, "Hello World", screen.black_pixel)
    draw_text(mouse_x + 10, mouse_y + 70, "Cheese", screen.black_pixel)

    # Display for 2 seconds
    display.sync()
    time.sleep(2)

    # Fade out (you'll need to implement this part)

    # Close the window
    window.destroy()
    display.sync()

if __name__ == "__main__":
    main()
