import cv2
import numpy as np

# Create an empty image
height = 400
width = 600
image = np.zeros((height, width, 3), dtype=np.uint8)

# Create horizontal gradient
for x in range(width):
    r = int((x / width) * 255)        # Red increases
    b = 255 - r                       # Blue decreases
    image[:, x] = (b, 0, r)           # BGR format

cv2.imshow("Color Gradient", image)
cv2.waitKey(0)
cv2.destroyAllWindows()