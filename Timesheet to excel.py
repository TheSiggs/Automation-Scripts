import pyautogui as gui
import time
import keyboard


# Basic Commands
def click(x, y): gui.click(x, y)

def write(text): gui.write(text)

def copy(): gui.hotkey('ctrl', 'c')  # ctrl-c to copy
def paste(): gui.hotkey('ctrl', 'v')  # ctrl-v to paste
def select_all(): gui.hotkey('ctrl', 'a') # select all

def tab(n = 1): 
	for _ in range(n):
		gui.press('tab') # press the tab key


def enter(): gui.press("enter") # press the enter key

def up(n): 
	for _ in range(n):
		gui.press('up') # press the left arrow key
def down(n): 
	for _ in range(n):
		gui.press('down') # press the left arrow key
def left(n): 
	for _ in range(n):
		gui.press('left') # press the left arrow key
def right(n): 
	for _ in range(n):
		gui.press('right') # press the left arrow key

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

def invoice_number():
    click(1525,20) # X: 1525 Y: 20 - Google Sheets
    down(1) # Invoice #
    copy()
    click(685,315) # X: 685 Y: 315 - Invoice Number
    select_all()
    paste()

def invoice_from():
    click(1525,20) # X: 1525 Y: 20 - Google Sheets
    right(3)
    copy()
    click(291,390) # X: 291 Y: 390 - Invoice From
    select_all()
    paste()

def invoice_to():
    click(1525,20) # X: 1525 Y: 20 - Google Sheets
    left(1)
    copy()
    click(238,498) # X: 238 Y: 498 - Invoice To
    select_all()
    paste()

def date():
    click(719,396) # Date - X: 719 Y: 396
    enter()

def populate_items(amount):
    click(244,625) # X: 244 Y: 625 - Items
    click(1525,20) # X: 1525 Y: 20 - Google Sheets
    left(2)
    down(2)
    for loop in range(amount):
	    # Item 1
	    copy()
	    click(802,25) # X: 802 Y: 25 - Invoice Generator
	    paste()
	    write(" - ")
	    click(1525,20) # X: 1525 Y: 20 - Google Sheets
	    right(1)
	    copy()
	    click(802,25) # X: 802 Y: 25 - Invoice Generator
	    paste()
	    write(" - ")
	    click(1525,20) # X: 1525 Y: 20 - Google Sheets
	    right(1)
	    copy()
	    click(802,25) # X: 802 Y: 25 - Invoice Generator
	    paste()
	    click(1525,20) # X: 1525 Y: 20 - Google Sheets
	    right(1)
	    copy()
	    left(4)
	    down(1)
	    click(802,25) # X: 802 Y: 25 - Invoice Generator
	    tab()
	    paste()
	    tab()
	    write("45")
	    tab()
	    enter()
	    click(1525,20) # X: 1525 Y: 20 - Google Sheets

def change_currency():
	click(802,25) # X: 802 Y: 25 - Invoice Generator
	gui.press('pagedown')
	wait(0.5)
	click(479,716) # X: 479 Y: 716 - Change Currency
	write('New Zealand Dollar')
	click(481,273) # X: 481 Y: 273 First Option

def invoice_name():
	click(672,255) # X: 672 Y: 255 - Invoice Name
	select_all()
	write("TAX INVOICE")

def notes():
	click(802,25) # X: 802 Y: 25 - Invoice Generator
	tab(14)
	write("Please pay to 01-0745-0513847-51 at your earliest convenience")



def main():
	lines = gui.prompt("How many lines items do you want added")
	lines = int(lines)
	# Invoice Name
	invoice_name()
	# Invoice Number
	invoice_number()
	# Invoice From
	invoice_from()
	# Invoice To
	invoice_to()
	# Date
	date()
	# Populate Items
	populate_items(lines)
	# Add Notes
	notes()
	# Change Currency
	change_currency()
	gui.alert("Invoice Completed")

# find_location()
main()

# X: 1525 Y: 20 - Google Sheets

# X: 802 Y: 25 - Invoice Generator

# X: 672 Y: 255 - Invoice Name
# X: 685 Y: 315 - Invoice Number
# X: 291 Y: 390 - Invoice From
# X: 238 Y: 498 - Invoice To
# X: 251 Y: 606 - Items