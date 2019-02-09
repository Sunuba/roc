import pyautogui
from time import sleep


class Clicker:

    @staticmethod
    def repeat_click(say):
        x, y = pyautogui.position()
        print(x, y)
        pyautogui.click(x, y, clicks=say-1, interval=0.1)

    @staticmethod
    def move_to(coords, seconds=0.35, yat=0.35):
        sleep(yat)
        # print('moving to: (' + str(coords[0]) + ', ' + str(coords[1]) + ')')
        pyautogui.moveTo(coords[0], coords[1], seconds)

    @staticmethod
    def click(coords, clicks=1, interval=1, button='left', yat=1):
        sleep(yat)
        # print('Clicking on: (' + str(coords[0]) + ', ' + str(coords[1]) + ')')
        pyautogui.click(coords[0], coords[1], clicks, interval, button)

    @staticmethod
    def move_click(coords, seconds=0.35, yat=1, clicks=1, interval=1, button='left'):
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

