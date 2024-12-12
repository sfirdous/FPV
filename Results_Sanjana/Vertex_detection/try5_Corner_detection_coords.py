import cv2
import numpy as np

img = cv2.imread('D:\FPV\Results_Sanjana\Vertex_detection\Shapes\Square_vivoT15g.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resize the image to fit the window size (e.g., 800x600)
window_width = 800
window_height = 600
resized_img = cv2.resize(img, (window_width, window_height))

# Display the resized image
cv2.imshow('image', resized_img)

# Resize the window to the same size as the image
cv2.resizeWindow('image', window_width, window_height)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 5, 3, 0.04)
ret, dst = cv2.threshold(dst, 0.1 * dst.max(), 255, 0)
dst = np.uint8(dst)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)

for i in range(1, len(corners)):
    print(corners[i])

img[dst > 0.1 * dst.max()] = [0, 0, 255]

# Show the image with detected corners
cv2.imshow('image', img)

# Resize the window to the same size as the image
cv2.resizeWindow('image', window_width, window_height)

cv2.waitKey(0)
cv2.destroyAllWindows()

