import datetime
import pyautogui
from time import sleep
import cv2
import numpy as np
from PIL import Image


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

    @staticmethod
    def sequential_shot(name='seq', i=0):
        sleep(1)
        Screenshot.shot(name='sequential/color/' + str(name) + str(i) + '.png')

    @staticmethod
    def region_shot(name='seq', seq_id=0, x1=0, y1=0, x2=200, y2=200, color=False, x_val=0):
        sleep(1)
        image = pyautogui.screenshot(region=(x1, y1, x2, y2))
        if not color:
            image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
        else:
            image = cv2.cvtColor(np.array(image), 2)
        cv2.imwrite('sequential/bw/' + str(name) + str(seq_id) + '.png', image)

        # process image
        im = Image.open('sequential/bw/' + str(name) + str(seq_id) + '.png')
        R, G, B = im.convert('RGB').split()
        r = R.load()
        g = G.load()
        b = B.load()
        w, h = im.size

        # Convert non-black pixels to white
        for i in range(w):
            for j in range(h):
                # if(r[i, j] != 0 or g[i, j] != 0 or b[i, j] != 0):
                if (x_val < r[i, j] < 100 or x_val < g[i, j] < 100 or x_val < b[i, j] < 100):
                    r[i, j] = 0
                    # g[i, j] = 0
                    # Just change R channel

        # Merge just the R channel as all channels
        im = Image.merge('RGB', (R, R, R))
        im.save('sequential/bw/' + str(name) + str(seq_id) + '.png')