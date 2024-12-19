import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('image.jpg', 0)

# Apply Harris Corner detection
corners = cv2.cornerHarris(image, 2, 3, 0.04)

# Threshold to get the corner points (you can adjust the threshold as needed)
corner_threshold = 0.01 * corners.max()
corner_coords = np.column_stack(np.where(corners > corner_threshold))

# Check if we found any corners
if corner_coords.shape[0] == 0:
    print("No corners detected!")
else:
    print(f"Number of corners detected: {corner_coords.shape[0]}")

# Camera matrix (example values, you should use your actual calibration results)
K = np.array([[800, 0, 320],  # Focal length fx, and cx (optical center)
              [0, 800, 240],  # Focal length fy, and cy (optical center)
              [0, 0, 1]])

# Distortion coefficients (example, use your own)
dist_coeffs = np.array([0, 0, 0, 0])

# Convert corner coordinates to float32 and reshape them to (n_points, 1, 2)
corner_coords_float = np.array(corner_coords, dtype=np.float32)

# Reshape to (n_points, 1, 2) as required by cv2.undistortPoints
corner_coords_reshaped = corner_coords_float.reshape(-1, 1, 2)

# If distortion coefficients are not zero, undistort the corner points
if not np.all(dist_coeffs == 0):
    undistorted_corners = cv2.undistortPoints(corner_coords_reshaped, K, dist_coeffs)
else:
    # If there is no distortion, undistortPoints won't change anything,
    # but we still need to convert to normalized camera coordinates
    undistorted_corners = corner_coords_reshaped

# Now, undistorted_corners is a list of undistorted points in normalized coordinates

# Convert the corner coordinates back to the original image scale if needed (optional)
# If you need to convert the undistorted points back to image coordinates:
undistorted_corners_image_space = cv2.convertPointsToHomogeneous(undistorted_corners).reshape(-1, 3)
undistorted_corners_image_space = undistorted_corners_image_space[:, :2]  # Convert to 2D points

# Print undistorted corners
print(f"Undistorted corner coordinates:\n{undistorted_corners_image_space}")

# Optionally, display the results (if you're visualizing)
# Convert the grayscale image to a color image for visualization
image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# Mark the undistorted corners on the image
for point in undistorted_corners_image_space:
    cv2.circle(image_color, tuple(np.int32(point)), 5, (0, 0, 255), -1)  # Mark corners in red

# Show the image with the marked corners
cv2.imshow('Corners', image_color)
cv2.waitKey(0)
cv2.destroyAllWindows()





'''
import cv2
import numpy as np
import math

# Load the image
image = cv2.imread('Shapes/DrawnTriangle.jpg', 0)  # Read the image in grayscale
image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# Apply Harris Corner detection
corners = cv2.cornerHarris(image, 2, 3, 0.04)

# Threshold the corners to make them visible
corners = cv2.dilate(corners, None)
image_color[corners > 0.01 * corners.max()] = [0, 0, 255]  # Mark corners in red

# Find the coordinates of the corners
corner_coords = np.column_stack(np.where(corners > 0.01 * corners.max()))

# Assume corner 1 is (x1, y1) and corner 2 is (x2, y2)
x1, y1 = corner_coords[0]  # Example corner 1
x2, y2 = corner_coords[1]  # Example corner 2

print("("+str(x1)+", "+str(y1)+")"+", ("+str(x2)+", "+str(y2)+")")

# Compute Euclidean distance
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"Distance between corner 1 and corner 2: {distance}")

cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green line
cv2.imshow('Corners', image_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''