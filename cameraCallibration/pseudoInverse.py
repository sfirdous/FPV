import numpy as np

# Define P and x
P = np.array([[...], [...], [...]])  # 3x4 matrix
x = np.array([...])                 # 3x1 vector

# Compute the pseudoinverse of P
P_pseudo = np.linalg.pinv(P)

# Solve for X
X = P_pseudo @ x