#! python3


"""
LIVE UPDATE FOR THE MOUSE COORDINATES.

Includes RGB values for the coordinates.
"""


from pyautogui import position, screenshot
import pyautogui

pyautogui.FAILSAFE = True

# def live():
print("COORDINATES".rjust(14) + "PIXEL-COLOR".rjust(19))
while True:
    # Getting x and y coordinates on screen
    x, y = position()
    pixel_color = screenshot().getpixel((x, y))

    position_str = "[X: " + str(x).rjust(4) + " Y: " + str(y).rjust(3)
    position_str += "] • [RGB: " + str(pixel_color[0]).rjust(3) + \
                    str(pixel_color[1]).rjust(4) + \
                    str(pixel_color[2]).rjust(4) + "]"

    if position() != position_str:
        print("\b" * len(position_str), end = "", flush = True)

    print(position_str, end = "")
