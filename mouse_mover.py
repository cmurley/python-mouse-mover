# Mouse Mover
# Utility to move the mouse every 2 minutes

# Import Mouse from pynput
from pynput import mouse
import time


# Create function to move mouse
def moveMouse():
    # Define Mouse Controller
    mouse_control = mouse.Controller()

    # Read current pointer position
    print('The current pointer position is {0}'.format(
        mouse_control.position))

    # Move pointer to 0x0 - Top Right of Screen
    mouse_control.position = (0, 0)

    # Move Pointer realative to position by 10px x 10px
    mouse_control.move(100, 100)

    # Read New Pointer position
    print('The new pointer position is {0}'.format(
        mouse_control.position))


def main():
    while True:
        moveMouse()
        time.sleep(5)

main()