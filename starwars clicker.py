import pyautogui as gui
import time


def getLocation():
    while True:
        time.sleep(1)
        x, y = gui.position()
        print("X:", x, "Y:", y, "RGB:", gui.screenshot().getpixel(gui.position()))
        if x == 0 and y == 0:
            break


def sendCrew(CrewX, CrewY, JobX=402, JobY=167):
    # "Send Companion Button"
    SendX = 515
    SendY = 479

    # select member
    gui.click(CrewX, CrewY)
    time.sleep(1)

    # Select job
    gui.click(JobX, JobY)
    time.sleep(1)

    # Click "Send Companion"
    gui.click(SendX, SendY)
    time.sleep(1)

    # Click "Mission Complete"
    for i in range(300, 700, 5):
        gui.click(816, i)


def main():
    StopX = 816
    StopY = 695
    print("Starting Script")
    while True:
        print("Sending Companion 1")
        sendCrew(104, 243)
        time.sleep(1)
        if gui.position() != (StopX, StopY):
            print("Stoping Script")
            break

        print("Sending Companion 2")
        sendCrew(136, 292)
        time.sleep(1)
        if gui.position() != (StopX, StopY):
            print("Stoping Script")
            break

        print("Sending Companion 3")
        sendCrew(128, 345)
        time.sleep(1)
        if gui.position() != (StopX, StopY):
            print("Stoping Script")
            break

# X: 104 Y: 243
# X: 136 Y: 292
# X: 128 Y: 345

# X: 402 Y: 167

# X: 515 Y: 479
# getLocation()
main()
