import pyautogui as gui

im = gui.screenshot()
mouse = gui.position()

while True:
	print(gui.locateOnScreen('dino.png'))