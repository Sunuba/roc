import pyautogui
from time import sleep
import random


class Clicker:

    @staticmethod
    def repeat_click(say, adjust_x=0, adjust_y=0, interval=0.10):
        x, y = pyautogui.position()
        x = x+adjust_x
        y = y+adjust_y
        print(x, y)
        pyautogui.click(x, y, clicks=say-1, interval=interval)

    @staticmethod
    def move_to(coords, seconds=0.35, yat=0.35):
        sleep(yat)
        # print('moving to: (' + str(coords[0]) + ', ' + str(coords[1]) + ')')
        pyautogui.moveTo(coords[0], coords[1], seconds)

    @staticmethod
    def click(coords, clicks=1, interval=1, button='left', yat=1):
        base = 0.6+random.random()*random.random()*0.9
        print(base)
        sleep(base)
        # print('Clicking on: (' + str(coords[0]) + ', ' + str(coords[1]) + ')')
        pyautogui.click(coords[0], coords[1], clicks, interval, button)

    @staticmethod
    def move_click(coords, seconds=0.35, yat=1, clicks=1, interval=1, button='left'):
        base = 0.5+random.random()*random.random()*0.9
        print(base)
        sleep(base)
        pyautogui.moveTo(coords[0], coords[1], seconds)
        sleep(yat)
        # print('moving to: (' + str(coords[0]) + ', ' + str(coords[1]) + ') and clicking')
        pyautogui.click(coords[0], coords[1], clicks, interval, button)

    @staticmethod
    def move(x, y):
        pyautogui.move(x, y)

    @staticmethod
    def mouse_pos():
        x, y = pyautogui.position()
        m_p = [x, y]
        return m_p

    @staticmethod
    def drag(coords):
        coord = [random.randint(200,800),random.randint(200,800)]
        pyautogui.mouseDown()

        Clicker.move(coord[0],coord[1])
        base = 0.5+random.random()*random.random()*20
        sleep(base)
        pyautogui.mouseUp(x=coords[0], y=coords[1])
