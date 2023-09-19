import cv2
import numpy as np

# 图片路径
img = cv2.imread('../data/beijing/shp/gaode_test.png')
a = []
b = []


# def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         xy = "%d,%d" % (x, y)
#         a.append(x)
#         b.append(y)
#         cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
#         cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
#                     1.0, (0, 0, 0), thickness=1)
#         cv2.imshow("image", img)
#
#
# cv2.namedWindow("image")
# cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
# cv2.imshow("image", img)
# cv2.waitKey(0)
# print(a, b)


# print(img[215, 723])
# print(img[205, 649])
# print(img[292, 990])

green = np.uint8([[img[292, 990]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(hsv_green)

