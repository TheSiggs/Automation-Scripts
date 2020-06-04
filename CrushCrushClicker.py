import pyautogui as gui
import time
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
        if keyboard.is_pressed('q'):
            return


# Actions
def gift(reps, gift, page):
    if gift == 1: # gift 1 - X: 754 Y: 493
        xcoord = 754
        ycoord = 493
    if gift == 2: # gift 2 - X: 928 Y: 485
        xcoord = 928
        ycoord = 485
    if gift == 3: # gift 3 - X: 759 Y: 570
        xcoord = 759
        ycoord = 570
    if gift == 4: # gift 4 - X: 918 Y: 565
        xcoord = 918
        ycoord = 565
    if gift == 5: # gift 5 - X: 772 Y: 636
        xcoord = 772
        ycoord = 636
    if gift == 6: # gift 6 - X: 923 Y: 627
        xcoord = 923
        ycoord = 627
    if gift == 7: # gift 7 - X: 764 Y: 698
        xcoord = 764
        ycoord = 698
    if gift == 8: # gift 8 - X: 931 Y: 695
        xcoord = 931
        ycoord = 695

    for i in range(reps):
        if keyboard.is_pressed('q'):
            return
        click(1077,510) # Click Gift - X: 1077 Y: 510
        # wait(1)
        for _ in range(page-1):
            click(990,423) # Click Next Page - X: 990 Y: 423
        # wait(1)
        click(xcoord, ycoord) # Click Gift
        # wait(1)
        for _ in range(9): # Buys maximum ammount 
            click(1132,577) # Click plus 9 times - X: 1132 Y: 577
            # wait(1)
        click(1210,537) # Click Pay - X: 1210 Y: 537
        click(1210,642) # Pay with gems - X: 1210 Y: 642
        click(942,557) # Accept X: 942 Y: 557

def date(reps, date):
    click(1080,554) # Date - X: 1080 Y: 554
    if date == 1: # 1. Moonlight Stroll - X: 802 Y: 488
        click(802,488) 
    if date == 2: # 2. Movie Theater - X: 787 Y: 561
        click(787,561) 
    if date == 3: # 3. Sightseeing - X: 798 Y: 642
        click(798,642) 
    if date == 4: # 4. Beach - X: 804 Y: 713
        click(804,713) 
    click(1225, 533) # Pay X: 1225 Y: 533
    for _ in range(reps-1):
        click(711,688) # Go Again - X: 711 Y: 688
        if keyboard.is_pressed('q'):
            return
    click(1179,693) # Click to Complete - X: 1179 Y: 693

def flirt(reps):
    for _ in range(reps):
        click(1081,421) # Flirt - X: 1081 Y: 421
        if keyboard.is_pressed('q'):
            return


def main():
    while True:
        print("\nFormat g for gift, d for date, f for flirt")
        command = input("Command: ")
        if command == "g":
            gift_amount = input("Amount: ")
            gift_number = input("Gift: ")
            gift_page = input("Page: ")
            gift(int(gift_amount), int(gift_number), int(gift_page))

        if command == "d":
            date_ammount = input("Amount: ")
            date_type = input("Date (1. Moonlight Stroll 2. Movie Theater 3. Sightseeing 4. Beach): ")
            date(int(date_ammount), int(date_type))

        if command == "f":
            flirt_amount = input("Amount: ")
            flirt(int(flirt_amount))

        if command == "q":
            break







# find_location()
main()

# Gift - X: 1077 Y: 510
# Next Page - X: 990 Y: 423
# Plus - X: 1132 Y: 577
# Pay - X: 1210 Y: 537
# Pay with gems - X: 1210 Y: 642
# Confirm pay with gems - X: 942 Y: 557

# Gifts
# gift 1 - X: 754 Y: 493     gift 2 - X: 928 Y: 485
# gift 3 - X: 759 Y: 570     gift 4 - X: 918 Y: 565
# gift 5 - X: 772 Y: 636     gift 6 - X: 923 Y: 627
# gift 7 - X: 764 Y: 698     gift 8 - X: 931 Y: 695

# Date - X: 1080 Y: 554
# 1. Moonlight Stroll - X: 802 Y: 488
# 2. Movie Theater - X: 787 Y: 561
# 3. Sightseeing - X: 798 Y: 642
# 4. Beach - X: 804 Y: 713