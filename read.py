import cv2 as cv 

# img = cv.imread('Photos/cat.jpg')

# cv.imshow('Cat', img)

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(2)& 0xFF==ord('d') :
        break
capture.release()
cv.destroyAllWindows()


