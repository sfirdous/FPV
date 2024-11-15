import cv2
import cv2.aruco as aruco

from object_detector import *
import numpy as np

# Load Aruco detector
parameters = aruco.DetectorParameters_create()
aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)


# Load Object Detector
detector = HomogeneousBgDetector()

# Load Image
img = cv2.imread("test_image15.jpg")

# Get Aruco marker
corners, _, _ = aruco.detectMarkers(img, aruco_dict, parameters=parameters)

# Draw polygon around the marker
int_corners = np.int0(corners)
cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

# Aruco Perimeter
aruco_perimeter = cv2.arcLength(corners[0], True)

# Pixel to cm ratio
pixel_cm_ratio = aruco_perimeter / 20

contours = detector.detect_objects(img)

# Draw objects boundaries
for cnt in contours:
    # Get rect
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect

    # Get Width and Height of the Objects by applying the Ratio pixel to cm
    object_width = w / pixel_cm_ratio
    object_height = h / pixel_cm_ratio

    # Display rectangle
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)
    cv2.putText(img, "Width {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    cv2.putText(img, "Height {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)



cv2.namedWindow("Image", cv2.WINDOW_NORMAL)  # Create a named window
cv2.resizeWindow("Image", 800, 600)  # Adjust the window size to 800x600
cv2.imshow("Image", img)  # Show the image in the resized window
cv2.waitKey(0)