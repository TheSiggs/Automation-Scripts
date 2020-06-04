import pyautogui as gui
import time
from random import randint


def find_location():
    while True:
        time.sleep(1)
        x, y = gui.position()
        print("X:", x, "Y:", y, "RGB:", gui.screenshot().getpixel(gui.position()))
        if x == 0 and y == 0:
            break


def typeIn(text):
    gui.typewrite(text + " ")


def enter():
    gui.press('enter')


def sleep(t):
    time.sleep(t)


print("Spam: ")
Input = input()


while True:
    gui.click(79, 947)
    if gui.position() != (79, 947):
        break
    for i in range(randint(5, 15)):
        typeIn(Input)

    enter()
