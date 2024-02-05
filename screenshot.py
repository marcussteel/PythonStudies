import pygetwindow
import platform
import pyautogui
from PIL import Image
from datetime import datetime
import time
from selenium import webdriver
import ctypes #screen size öğrenmek için


def get_screen_size(monitor = 1):
    main_x = pyautogui.size()[0] # getting the width of the main screen
    main_y = pyautogui.size()[1] # getting the height of the main screen
    if monitor == 1:
        screensize = main_x, main_y
        print(f'Screen size :{screensize} in monitor: {monitor}')
    elif monitor == 2:

        user32 = ctypes.windll.user32
        second_x = abs(user32.GetSystemMetrics(78)- main_x)
        if second_x == 1920:
            second_y = 1080
        elif second_x == 3840:
            second_y = 2160
        screensize = second_x, second_y
        print(f'Screen size :{screensize} in monitor: {monitor}')

    return screensize

def screen_size_and_position():
    x,y = get_screen_size(1)
    driver.set_window_size(x/2, y/2)
    driver.set_window_position(x/2, 0, windowHandle ='current')

    #path = 'C:\\Users\\musta\\AppData\\Local\\Programs\\Opera\\opera.exe'
    path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
    
    chromeOps = webdriver.ChromeOptions()
    chromeOps._binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\Chrome.exe"
    chromeOps._arguments = ["--enable-internal-flash"]
    
    chromeOps.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=chromeOps)



date1 = datetime.today().strftime('%Y%m%d_%H%M%S')
image_name = f"screenshot-{date1}.png"
#image_name = 'check_image.png'
path = f'./images/{image_name}'



def take_screenshot_spec_window(add_to_x1=0,add_to_y1=0,remove_from_x2=0,remove_from_y2=0, app = 'Chrome'):
    titles = pygetwindow.getAllTitles()
    #print(titles) #açık olan pencereleri gösterir

    if platform.system() == 'Windows' :
        window = pygetwindow.getWindowsWithTitle(app)[0]
        left, top = window.topleft
        right, bottom = window.bottomright
        pyautogui.screenshot(path)
        im = Image.open(path)
        im = im.crop((left + add_to_x1, top + add_to_y1, right - remove_from_x2, bottom - remove_from_y2))
        im.save(path)
        #im.show(path)
        print('Screen saved succesfully...')
    elif platform.system() == 'Darwin' :
        x1, y1, width, height = pygetwindow.getWindowGeometry('Terminal')
        x2 = x1 + width
        y2 = y1 + height

        pyautogui.screenshot(path)
        im = im.crop((x1 + add_to_x1, y1 + add_to_y1, x2 - remove_from_x2, y2 - remove_from_y2))
        im.save(path)
        print('Screen saved succesfully...')
        #im.show(path)
    time.sleep(0.5)

def screenshot(add_to_x1=0,add_to_y1=0,remove_from_x2=0,remove_from_y2=0):
    screensize = get_screen_size(1)
    #print(screensize)
    myScreenshot = pyautogui.screenshot()
    left, top = 0 , 0
    right, bottom = screensize
    myScreenshot = myScreenshot.crop((left + add_to_x1, top + add_to_y1, right - remove_from_x2, bottom - remove_from_y2))
    myScreenshot.save(path)

#take_screenshot_spec_window( app='Opera') # minus -1
screenshot(0,50,0,50)
#get_screen_size(1)
