import pyautogui as gui
import time
from random import randint

# Basic Commands


def click(x, y): gui.click(x, y)


def wait(t): time.sleep(t)


def find_location():
    while True:
        time.sleep(1)
        x, y = gui.position()
        print("X:", x, "Y:", y, "RGB:", gui.screenshot().getpixel(gui.position()))
        if x == 0 and y == 0:
            break


def main():
    while True:
        click(1684, 969)
        gui.typewrite("!charity")
        click(1887, 1010)
        wait(65)



# X: 1887 Y: 1010 Chat BUtton
# X: 1684 Y: 969 Chat Box
# find_location()
main()
