import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('Color Strip')

# Create trackbars for color change
cv2.createTrackbar('R', 'Color Strip', 0, 255, nothing)
cv2.createTrackbar('G', 'Color Strip', 0, 255, nothing)
cv2.createTrackbar('B', 'Color Strip', 0, 255, nothing)

# Create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'Color Strip', 0, 1, nothing)

while True:
    cv2.imshow('Color Strip', img)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

    # Get current positions of the trackbars
    r = cv2.getTrackbarPos('R', 'Color Strip')
    g = cv2.getTrackbarPos('G', 'Color Strip')
    b = cv2.getTrackbarPos('B', 'Color Strip')
    s = cv2.getTrackbarPos(switch, 'Color Strip')

    if s == 0:
        img[:] = 0  # Show black when switch is OFF
    else:
        img[:] = [b, g, r]  # OpenCV uses BGR order

cv2.destroyAllWindows()