import cv2
import numpy as np


def nothing(x):
    pass


img = cv2.imread("../data/image_1.png")
img = cv2.resize(img, (640, 350))
# Create a black image, a window
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('H Max', 'image', 0, 255, nothing)
cv2.createTrackbar('H Min', 'image', 0, 255, nothing)
cv2.createTrackbar('S Max', 'image', 0, 255, nothing)
cv2.createTrackbar('S Min', 'image', 0, 255, nothing)
cv2.createTrackbar('V Max', 'image', 0, 255, nothing)
cv2.createTrackbar('V Min', 'image', 0, 255, nothing)


while(1):
    cv2.imshow('image', img)

    # get current positions of four trackbars
    hmax = cv2.getTrackbarPos('H Max', 'image')
    hmin = cv2.getTrackbarPos('H Min', 'image')
    smax = cv2.getTrackbarPos('S Max', 'image')
    smin = cv2.getTrackbarPos('S Min', 'image')
    vmax = cv2.getTrackbarPos('V Max', 'image')
    vmin = cv2.getTrackbarPos('V Min', 'image')

    lower = np.array([hmin, smin, vmin])
    upper = np.array([hmax, smax, vmax])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(img, img, mask=mask)
    rgb = cv2.cvtColor(output, cv2.COLOR_HSV2RGB)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    dilation = cv2.dilate(gray, np.ones((5, 5), np.uint8), iterations=1)
    cv2.imshow("output", dilation)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
