import cv2


class Blur:
    def __init__(self, frame):
        self.frame = frame

    def simple_blur(self, c, d): #c e d - width and height of the kernel
        blur = cv2.blur(self.frame, (c, d))

        return blur

    def gaussian_blur(self, d): #d - used to calculate the kernel
        gaussian = cv2.GaussianBlur(self.frame, (2 * d + 1, 2 * d + 1), -1)[d:-d, d:-d]

        return gaussian

    def median_blur(self, ksize):
        median = cv2.medianBlur(self.frame, ksize)

        return median

    def bilateral_blur(self, d, sigma_color, sigma_space): #d - Diameter of each pixel neighborhood that is used during filtering
        bilateral = cv2.bilateralFilter(self.frame, d, sigma_color, sigma_space)

        return bilateral
