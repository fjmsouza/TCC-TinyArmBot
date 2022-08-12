import cv2
import numpy as np


class Edge:
    def __init__(self, frame):
        self.frame = frame

    def canny_edge(self, threshold1, threshold2, d):#d - used to calculate the kernel
        edge_result = self.frame.copy()
        edge_result = cv2.GaussianBlur(edge_result, (2 * d + 1, 2 * d + 1), -1)[d:-d, d:-d]
        canny = cv2.Canny(edge_result, threshold1, threshold2)

        return canny

    def sobel_edge(self, ksize):
        sobelX = cv2.Sobel(self.frame, cv2.CV_64F, 1, 0, ksize)
        sobelY = cv2.Sobel(self.frame, cv2.CV_64F, 0, 1, ksize)
        sobelX = np.uint8(np.absolute(sobelX))
        sobelY = np.uint8(np.absolute(sobelY))
        sobel = cv2.bitwise_or(sobelX, sobelY)

        return sobel

    def laplacian_edge(self):
        laplacian = cv2.Laplacian(self.frame, cv2.CV_64F)
        laplacian = np.uint8(np.absolute(laplacian))

        return laplacian
