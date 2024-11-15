import cv2
import numpy as np

# Load calibrated camera parameters (from Zhang's algorithm)
# Assuming these have been calculated and saved after calibration
# replace with actual values
camera_matrix = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])
# replace with actual distortion coefficients
dist_coeffs = np.array([k1, k2, p1, p2, k3])

# Load the image with the object and reference
image_path = 'object_with_reference.jpg'
image = cv2.imread(image_path)

# Undistort the image (correcting lens distortion)
h, w = image.shape[:2]
new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(
    camera_matrix, dist_coeffs, (w, h), 1, (w, h))
undistorted_img = cv2.undistort(
    image, camera_matrix, dist_coeffs, None, new_camera_matrix)

# Convert to grayscale and apply edge detection
gray = cv2.cvtColor(undistorted_img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

# Find contours
contours, _ = cv2.findContours(
    edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Assume the largest contour is the object
object_contour = max(contours, key=cv2.contourArea)

# Get the bounding box for the object
x, y, width_pixels, height_pixels = cv2.boundingRect(object_contour)

# Measure the reference object in pixels (e.g., a known segment like a ruler)
# Manually or automatically identify the reference object in pixels (e.g., 100 pixels represents 10 cm)
# Replace reference_width_pixels and reference_width_cm with actual known values
reference_width_pixels = 100  # example, measure this for your setup
reference_width_cm = 10       # actual known width of reference object in cm

# Calculate pixel-to-cm ratio
pixel_to_cm_ratio = reference_width_cm / reference_width_pixels

# Calculate object dimensions in centimeters
object_width_cm = width_pixels * pixel_to_cm_ratio
object_height_cm = height_pixels * pixel_to_cm_ratio

print(f"Object Width: {object_width_cm:.2f} cm")
print(f"Object Height: {object_height_cm:.2f} cm")
