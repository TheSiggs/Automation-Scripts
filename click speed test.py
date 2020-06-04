import pyautogui as gui
import time


# X: 1514 Y: 222

# while True:
# 	time.sleep(1)
# 	x,y = gui.position()
# 	print("X:",x, "Y:",y ,"RGB:", gui.screenshot().getpixel(gui.position()))
# 	if x == 0 and y == 0:
# 		break

def typeIn(text):
    for i in text:
        gui.press(i)


def enter():
    gui.press('enter')

while True:
    # time.sleep(1)\
    gui.click(1514, 222)
    typeIn("nigger")
    enter()
    if gui.position() != (1514, 222):
        break
