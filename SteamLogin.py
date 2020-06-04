import pyautogui as gui
import time
from random import randint
import keyboard

# Basic Commands
def click(x, y): gui.click(x, y)

def wait(t): time.sleep(t)

def write(text): gui.typewrite(text)

def find_location():
    while True:
        time.sleep(1)
        x, y = gui.position()
        print("X:", x, "Y:", y, "RGB:", gui.screenshot().getpixel(gui.position()))
        if x == 0 and y == 0:
            break


def main():
    click(855, 454) # Username
    write("DotNetPlus")
    click(853, 490) # Password
    write("DynamicPi01")
    click(866, 545) # Login Button
    return

# X: 539 Y: 362
# find_location()
main()

