import pyautogui
import time

pyautogui.doubleClick(-1400,400)
time.sleep(4)
pyautogui.write('123456')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('002')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(260, 90)
