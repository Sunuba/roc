import pyautogui
from time import sleep
import random
import win32gui
import math as m

class Clicker:
    processname=''
    @classmethod
    def find_window_movetop(cls):
        hwnd = win32gui.FindWindow(None, cls.processname)
        win32gui.ShowWindow(hwnd,5)
        win32gui.SetForegroundWindow(hwnd)
        rect = win32gui.GetWindowRect(hwnd)
        sleep(0.2)
        return rect
        
    @classmethod
    def repeat_click(cls,say, adjust_x=0, adjust_y=0, interval=0.10):
        rect =cls.find_window_movetop()
        posx = rect[0]
        posy = rect[1]

        x, y = pyautogui.position()
        x = x+adjust_x
        y = y+adjust_y
        print(x, y)
        pyautogui.click(m.ceil(x+posx), m.ceil(y+posy), clicks=say-1, interval=interval)

    @classmethod
    def click(cls,coords, clicks=1, interval=1, button='left', yat=1):
        rect =cls.find_window_movetop()
        posx = rect[0]
        posy = rect[1]

        base = 0.3+random.random()*random.random()*0.9
        print(base)
        sleep(base)
        print(m.ceil(coords[0]+posx), m.ceil(coords[1]+posy))
        # print('Clicking on: (' + str(coords[0]) + ', ' + str(coords[1]) + ')')
        pyautogui.click(m.ceil(coords[0]+posx), m.ceil(coords[1]+posy), clicks, interval, button)

    @classmethod
    def move(cls,x, y):
        rect =cls.find_window_movetop()
        posx = rect[0]
        posy = rect[1]
        print('check these point')
        print(x+posx,y+posy)
        pyautogui.move(m.ceil(x+posx), m.ceil(y+posy))

    @classmethod
    def mouse_pos(cls):
        rect =cls.find_window_movetop()
        posx = rect[0]
        poxy = rect[1]
        x, y = pyautogui.position()
        m_p = [x, y]
        return m_p

    @classmethod
    def drag(cls,coords):
        print('drag')
        rect =cls.find_window_movetop()
        posx = rect[0]
        posy = rect[1]
        w = rect[2] - posx
        h = rect[3] - posy
        coord = [random.randint(int(w/7),int(w*6/7)),random.randint(int(h/4),int(h*3/4))]
        pyautogui.mouseDown(m.ceil(coord[0]+posx),m.ceil(coord[1]+posy))

        base = 0.4+random.random()*random.random()*3
        sleep(base)
        pyautogui.mouseUp(m.ceil(coords[0]+posx),m.ceil(coords[1]+posy))

    @classmethod
    def randomdrag(cls):
        print('randomdrag')
        rect =cls.find_window_movetop()
        posx = rect[0]
        posy = rect[1]
        w = rect[2] - posx
        h = rect[3] - posy
        print('spec')
        print(posx,posy,w,h)
        coord = [random.randint(int(w/7),int(w*6/7)),random.randint(int(h/4),int(h*3/4))]        
        pyautogui.mouseDown(m.ceil(coord[0]+posx),m.ceil(coord[1]+posy))

        base = 0.4+random.random()*random.random()*3
        sleep(base)
        coord = [random.randint(int(w/7),int(w*6/7)),random.randint(int(h/4),int(h*3/4))]
        pyautogui.mouseUp(m.ceil(coord[0]+posx),m.ceil(coord[1]+posy))

    @classmethod
    def centerclick(cls, clicks=1, interval=1, button='left', yat=1):
        rect =cls.find_window_movetop()
        posx = rect[0]
        posy = rect[1]
        w = rect[2] - posx
        h = rect[3] - posy

        # print('Clicking on: (' + str(coords[0]) + ', ' + str(coords[1]) + ')')
        pyautogui.click(m.ceil(w/2+posx), m.ceil(h/2+posy), clicks, interval, button)