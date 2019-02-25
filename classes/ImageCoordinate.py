from classes.Screenshot import Screenshot
import cv2
import numpy as np
from matplotlib import pyplot as plt


class ImageCoordinate:
    @staticmethod
    def count_occurrence(this):
        Screenshot.shot()
        this = this + '.png'
        img_rgb = cv2.imread(this)
        template = cv2.imread('playing.png')
        res = cv2.matchTemplate(img_rgb, template, 1)
        threshold = 0.8
        loc = np.where(res >= threshold)
        cv2.imwrite('result.png', img_rgb)
        return loc

    @staticmethod
    def is_on_screen(this):
        this = this + '.png'
        Screenshot.shot()
        small_image = cv2.imread(this)
        large_image = cv2.imread('playing.png')
        result = cv2.matchTemplate(small_image, large_image, 1)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # print('ImageCoordinate::is_on_screen => ' + this + ' ' + str(min_val))
        if min_val > 0.05:
            return False
        else:
            return True

    @staticmethod
    def coords(this, shot=True):
        this = this + '.png'
        if shot:
            Screenshot.shot()
        else:
            print('No screenshot')
        small_image = cv2.imread(this)
        h, w, c = small_image.shape
        large_image = cv2.imread('playing.png')
        result = cv2.matchTemplate(small_image, large_image, 1)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # print('ImageCoordinate::coords => ' + this + ' ' + str(min_val))
        if min_val > 0.25:
            return [0, 0, min_val]
        mn, _, mn_loc, _ = cv2.minMaxLoc(result)
        mp_x, mp_y = mn_loc
        location = [mp_x + w / 2, mp_y + h / 2, min_val]
        return location