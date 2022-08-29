import numpy as np

def determinant(frame):
    sum = np.matrix(frame).sum()

    # det = np.linalg.det(sum)
    return sum