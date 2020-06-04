import pyautogui as gui
import time
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
        if keyboard.is_pressed('q'):
            return

def main():
    pass






find_location()
# main()
