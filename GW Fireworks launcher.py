import pyautogui as gui
import time
from random import randint


def click(x, y): gui.click(x, y)


def wait(t): time.sleep(t)


def finish_loop():
    x, y = gui.position()
    if x == 0 or y == 0:
        return False
    else:
        return True


def find_location():
    while True:
        time.sleep(1)
        x, y = gui.position()
        print("X:", x, "Y:", y, "RGB:", gui.screenshot().getpixel(gui.position()))
        if x == 0 and y == 0:
            break


def main():
    while(finish_loop != False):
        click(601, 258)
        click(601, 258)
        wait(1)
        for i in range(3):
            click(664, 1038)
            wait(7)
        for i in range(3):
            click(722, 1032)
            wait(7)
        for i in range(3):
            click(764, 1036)
            wait(7)
    print("finishing loop")



# X: 601 Y: 258 - firework
# tap X: 664 Y: 1038 3 times
# tap X: 722 Y: 1032 3 times
# tap X: 764 Y: 1036 3 times
# loop
main()
# find_location()
