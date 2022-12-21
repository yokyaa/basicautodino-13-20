import pyautogui
from PIL import Image, ImageGrab
import time

def press(key):
   pyautogui.keyDown(key)
   return

def react(data):
    for i in range(300, 360):
        for j in range(500, 573):
            if data[i, j] < 171:
                press("down")
                print("down")
                return
    for i in range(300, 490):
        for j in range(580, 630):
            if data[i, j] < 100:
                press("up")
                print("jump")
                return
    return


if __name__ == "__main__":
    time.sleep(2)
    press('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        react(data)
