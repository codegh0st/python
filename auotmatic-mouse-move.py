import pyautogui
import random

"""
pyautogui is moudule to automate the mouse and keyboard. with this module you can write a script
which will be able to play a game, very powerfull and intererting module.  
Documentation: https://pyautogui.readthedocs.io/en/latest/index.html
"""

screenWidth, screenHeight = pyautogui.size()
print(screenHeight,screenWidth)
print("MOVE YOUR MOUSE POINT TO ANY CORNER OF YOUR SCREEN 'QUICKLY' TO END THIS PROGRAM !")
while True:
    x = random.randint(10, 1000)
    y = random.randint(10, 1600)
    
    pyautogui.moveTo(x, y, duration=0.5)
  
