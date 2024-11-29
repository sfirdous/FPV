import numpy as np

# Define the intrinsic matrix P
fx, fy = 933.2709066392878, 924.716502790399
cx, cy = 495.05701189803943, 657.6301853051167
P = np.array([[fx, 0, cx],
              [0, fy, cy],
              [0,  0,  1]])

# Image point (2D) in homogeneous coordinates
x_image = np.array([u, v, 1])  # Replace u, v with actual image coordinates

# Compute the pseudoinverse of P
P_pseudo = np.linalg.pinv(P)

# Solve for X in camera coordinates
X_camera = P_pseudo @ x_image

print("3D Camera Coordinates:", X_camera)