import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)


cv.waitKey(0)