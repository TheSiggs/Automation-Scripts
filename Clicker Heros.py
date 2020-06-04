import pyautogui as gui
import time


def find_location():
    while True:
        time.sleep(1)
        x, y = gui.position()
        print("X:", x, "Y:", y, "RGB:", gui.screenshot().getpixel(gui.position()))
        if x == 0 and y == 0:
            break


def typeIn(text):
    for i in text:
        gui.press(i)


def enter():
    gui.press('enter')


while (True):
    x, y = gui.position()
    gui.click(1194, 402)
    gui.click(670, 600)
    if x == 0 and y == 0:
    	break
    time.sleep(5)
    # find_location()
