import pyautogui as gui
import msvcrt as m
import time


def enter(text):
    for i in text:
        gui.press(i)


def notepad():
    gui.press('winleft')
    enter("Notepad")

    gui.press('enter')

    time.sleep(0.5)
    gui.typewrite("Hello World")
    gui.hotkey('alt', '3')
notepad()
