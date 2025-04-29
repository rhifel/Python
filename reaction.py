import pyautogui
import time

while True:
    
    if pyautogui.pixel(666,512) == (75, 219, 106):
        print("I see green")
        pyautogui.click(666,512)
        break
    time.sleep(0.01)
    #else:
        #print("I don't see green")
'''
print(pyautogui.position())
print(pyautogui.pixel(215,432))
'''