import cv2

image = cv2.imread('lambo.jpeg', cv2.IMREAD_UNCHANGED)
cv2.imshow('Title', image)

cv2.waitKey(0)