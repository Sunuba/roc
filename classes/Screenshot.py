import datetime
import pyautogui
from time import sleep

class Screenshot:
    @staticmethod
    def shot(name='playing.png'):
        today = datetime.datetime.now()
        # print('Taking screenshot: ' + today.strftime("%H:%M:%S"))
        pyautogui.screenshot(name)

    @staticmethod
    def burst(name='graph'):
        for i in range(0, 100000):
            sleep(1)
            Screenshot.shot(name='screenshots/' + str(name) + str(i) + '.png')