import pyautogui
import time
import os
pyautogui.FAILSAFE = False
pyautogui.moveTo(1,1, duration = 0.5)
pyautogui.moveTo(1,500, duration = 0.5)
speedTraced = False
clickTraced = False
doubleClickTraced = False
okClicks = 0
print("Starting Pafish")
os.system("start cmd /C pafish64.exe")
time.sleep(1)
pyautogui.hotkey('alt','tab')
time.sleep(1)
with pyautogui.hold('win'):
	pyautogui.press('right')
	time.sleep(0.400)
	pyautogui.press('down')

while(speedTraced != True):
    try:
        m,n = pyautogui.locateCenterOnScreen('mouseSpeed.png')
        pyautogui.moveTo(800,800, duration = 0.2)
        speedTraced = True
    except:
        pyautogui.moveTo(1,1, duration = 0.5)
        pyautogui.moveTo(1,500, duration = 0.5)
print("Speed Check Done")

while(clickTraced != True or doubleClickTraced != True):
	try:
		m,n = pyautogui.locateCenterOnScreen('mouseClick.png')
		a,b = pyautogui.locateCenterOnScreen('mouseDoubleClick.png')
		clickTraced = True
		doubleClickTraced = True
	except:
		pyautogui.rightClick()
		pyautogui.leftClick()
print("Click checks done")   

time.sleep(0.200)
while(okClicks < 2):
    try:
        #pyautogui.click(x, y)
        x,y = pyautogui.locateCenterOnScreen('OK.png')
        print(x,y)
        time.sleep(0.200)
        pyautogui.click('OK.png')
        okClicks +=1
        pyautogui.press('enter')
    except TypeError:
        print("Still no image")
