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
        wait(1)
        gui.rightClick(698, 217)
        wait(0.1)
        gui.rightClick(698, 217)
        wait(1)
        gui.press('1')
        wait(1)
        gui.press('esc')

# X: 698 Y: 217


main()
# find_location()
