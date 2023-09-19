import time
import sklearn.metrics
from PIL import Image
from PIL import ImageEnhance
import numpy as np
import cv2
import imageio
from sklearn.metrics.cluster import mutual_info_score
from ssim import compute_ssim
from vector import test, calculate_FOA
from remote import adaptive_otsu, calculate_dark
import xlwt
import matplotlib.pyplot as plt
import keras_ocr
import math

n = 1
f = xlwt.Workbook()
sheet = f.add_sheet('shp', cell_overwrite_ok=True)

sheet.write(0, 1, "MI")
sheet.write(0, 2, "NMI")
sheet.write(0, 3, "SSIM")
sheet.write(0, 4, "FOA")

for a in range(-10, 0, 1):
    sheet.write(n, 0, a)
    # the path of the registered map
    img1_path = ""
    # the path of the reference map
    img2_path = ""

    # remote sensing maps读取方式
    # img1 = cv2.imread(img1_path, 0)
    # img2 = cv2.imread(img2_path, 0)
    # img1_rs = adaptive_otsu(img1)
    # img2_rs = adaptive_otsu(img2)

    # vector maps读取方式
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # ssim读取方式
    img_mat_1 = imageio.imread(img1_path, as_gray=True)
    img_mat_2 = imageio.imread(img2_path, as_gray=True)

    # cal MI, NMI, SSIM
    img_ref = np.array(img1, dtype=np.int32)
    img_sen = np.array(img2, dtype=np.int32)
    img_ref = img_ref .reshape(-1)
    img_sen_roi = img_sen .reshape(-1)
    MI = mutual_info_score(img_ref, img_sen_roi)
    NMI = sklearn.metrics.normalized_mutual_info_score(img_ref, img_sen_roi)
    SSIM = compute_ssim(img_mat_1, img_mat_2)

    # rs数据计算MOA
    # FOA = calculate_dark(img1_rs, img2_rs)

    # vector数据计算MOA
    FOA = calculate_FOA(test(img1), test(img2))

    sheet.write(n, 1, MI)
    sheet.write(n, 2, NMI)
    sheet.write(n, 3, SSIM)
    sheet.write(n, 4, FOA)
    n = n+1
# the savepath of metrics
f.save("../linshi.xls")

