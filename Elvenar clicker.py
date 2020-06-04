import pyautogui as gui
import time
import ctypes


def find_location():
    while True:
        time.sleep(1)
        x, y = gui.position()
        print("X:", x, "Y:", y, "RGB:", gui.screenshot().getpixel(gui.position()))
        if x == 0 and y == 0:
            break


def startProd(workX, workY):
    gui.click(workX, workY)
    time.sleep(1)
    # X: 763 Y: 493 - Beverages
    gui.click(763, 493)
    time.sleep(1)


def main():
    while True:
        # X: 132 Y: 1052 - Firefox
        gui.click(132, 1052)
        time.sleep(1)

        # X: 895 Y: 524 - Workshop 1
        startProd(895, 524)
        # X: 804 Y: 580 - Workshop 2
        startProd(804, 580)
        # X: 678 Y: 618 - Workshop 3
        startProd(678, 618)
        time.sleep(350)


main()
# find_location()
