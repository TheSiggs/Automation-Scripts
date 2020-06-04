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
        click(700, 650)  # Place Bet
        wait(1)
        click(400, 250)  # Click Horse 1
        wait(1)
        for x in range(1, 7):
          click(777, 400)  # Click Left arrow 7 times
          wait(0.5)
        wait(1)
        click(777, 400)  # Click Left arrow 1 more time
        gui.dragTo(700, 600, 40)  # drags to place bet
        wait(1)
        gui.click(button="right")
        wait(1)
    except:
      return


# X: 539 Y: 362
# find_location()
main()
