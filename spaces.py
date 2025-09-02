import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/city.jpg')
cv.imshow('City',img)

# plt.imshow(img)
# plt.show()

# # BGR to GrayScale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# #cv.imshow('Gray', gray)

# # BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2RGB)
cv.imshow('HSV-->BGR',hsv_bgr)
# # BGR to L*a*b
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB',lab)
# # BGR to rgb
# rgb = cv.cvtColor(img ,cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)

# plt.imshow(rgb)
# plt.show()



cv.waitKey(0)