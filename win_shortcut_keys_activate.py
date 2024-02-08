import pyautogui
import os
import time


paths_will_be_open = ['C:\\Users\\musta\\AppData\\Local\\Programs\\Opera\\opera.exe',
                       'D:\\Forexthings\\Diary\\2024', 'D:\\Forexthings\\screencaps', 
                       'D:\\Forexthings\\Trade_Set.7z', 'D:\\Forexthings\\temp folder']


for i in paths_will_be_open:
    path = i
    path = os.path.realpath(path)
    os.startfile(path)

time.sleep(10)

#pyautogui.keyDown('winleft')
#pyautogui.press('v')
#pyautogui.keyUp('winleft')
pyautogui.hotkey('winleft', 'ctrl', 'right')
path = 'D:\\_MT_\\MT5 - EvolveMarkets01 - Portable\\terminal64.exe'
path = os.path.realpath(path)
os.startfile(path)
time.sleep(15)
pyautogui.hotkey('winleft', 'ctrl', 'left')
