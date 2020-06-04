import pyautogui
import time

grey = (107,106,107)

blue = (476, 444)
red = (920, 443)
oneVsone = (641, 304)

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
pyautogui.size()
width, height = pyautogui.size()
im = pyautogui.screenshot()

while True:
	mousepos = pyautogui.position()
	
	# time.sleep(1)
	# print(pyautogui.position(), im.getpixel(pyautogui.position()))

# pyautogui.position()
# pyautogui.click(200, 250, button='left')
# pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])


