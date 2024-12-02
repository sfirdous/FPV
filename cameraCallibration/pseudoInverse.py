import numpy as np

# Define the intrinsic matrix P
fx, fy = 933.2709066392878, 924.716502790399
cx, cy = 495.05701189803943, 657.6301853051167
P = np.array([[fx, 0, cx],
              [0, fy, cy],
              [0,  0,  1]])

# Image points (2D) in homogeneous coordinates
image_points = np.array([
    [105.37255, 158.19608, 1],  # First coordinate
    [224.78767, 283.7525, 1],   # Second coordinate
    [104.54036, 285.1601, 1]    # Third coordinate
])

# Compute the pseudoinverse of P
P_pseudo = np.linalg.pinv(P)

# Solve for 3D camera coordinates for each image point
camera_coordinates = [P_pseudo @ point for point in image_points]

# Print the 3D camera coordinates
for i, coord in enumerate(camera_coordinates, 1):
    print(f"3D Camera Coordinates for Point {i}: {coord}")
