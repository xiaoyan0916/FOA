import cv2
import numpy as np
import cv2 as cv

def calculate_dark(img1,img2):
    h,w = img1.shape
    together=0
    img1n=0
    img2n=0
    for i in range(h):
       for j in range(w):
            if(img1[i][j]==255 and img2[i][j]==255):
                together = together+1
            if(img1[i][j]==255):
                img1n = img1n+1
            if(img2[i][j]==255):
                img2n = img2n+1

    return(together/min(img1n,img2n))

def adaptive_otsu(img):
    img_g = cv.equalizeHist(img)
    h, w = img_g.shape
    mask = np.zeros_like(img_g)
    winHalfWidth = 10
    localVarThresh = 0.000

    for i in range(0,w):
        new_img = img_g[:, max(1,i-winHalfWidth): min(w,i+winHalfWidth)]
        th , th_otsu = cv.threshold(new_img, 0, 255, cv.THRESH_OTSU)
        intile = np.var(new_img / 255)
        if intile > localVarThresh:
            _, mask[:,i:i+1] = cv.threshold(img_g[:,i:i+1], th, 255, cv.THRESH_BINARY)
        else:
            mask[:, i:i+1] = 255
    cv2.imwrite("../data/dif_size/tian_test_15_0_res.png", mask)
    return mask