import cv2
import numpy as np
from PIL import Image
from PIL import ImageEnhance
import math


def calculate_FOA(img1, img2):
    h, w = img1.shape
    together = 0
    all = 0
    img1n = 0
    img2n = 0
    for i in range(0, h):
       for j in range(0, w):
            if(img1[i][j] == 255 and img2[i][j] == 255):
                together = together+1
            if(img1[i][j]==255):
                img1n = img1n+1
            if(img2[i][j]==255):
                img2n = img2n+1
    if together == 0 or min(img1n, img2n) == 0:
        res = 0
    else:
        res = together/min(img1n, img2n)
    return res


def compute_circle(polygon):
    a = cv2.contourArea(polygon)*math.pi*4
    b = math.pow(cv2.arcLength(polygon, True), 2)
    if b == 0:
        return 0
    return a / b
# RGB方法
def test(img):

    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    _, bimg = cv2.threshold(b, 160, 255, cv2.THRESH_BINARY_INV)
    _, gimg = cv2.threshold(g, 160, 255, cv2.THRESH_BINARY_INV)

    merge = cv2.addWeighted(bimg, 0.5, gimg, 0.5, gamma=0)
    _, merge = cv2.threshold(merge, 0, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(merge, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        if area < 250:
            cv2.fillConvexPoly(merge, contours[i], 255)
    contours, hierarchy = cv2.findContours(merge, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for j in range(len(contours)):
        area = cv2.contourArea(contours[j])
        if area < 200:
            cv2.fillConvexPoly(merge, contours[j], 0)
        if compute_circle(contours[j]) > 0.2 and area < 800:
            cv2.fillConvexPoly(merge, contours[j], 0)
    cv2.imwrite("../data/dif_size/t15.5.png", merge)
    return merge


