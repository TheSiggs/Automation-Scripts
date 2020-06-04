import pyautogui as gui
import time
from random import randint
import keyboard

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
    click(539, 362)
    while True:
        try:
            if keyboard.is_pressed('q'):
                print("closing program")
                return
            else:
                click(964,616)
        except:
            return


# X: 539 Y: 362
# find_location()
main()
