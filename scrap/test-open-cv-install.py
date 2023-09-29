import cv2 as cv

img = cv.imread("./test_image.jpg")
cv.imshow("Test Image", img)

cv.waitKey(0)
