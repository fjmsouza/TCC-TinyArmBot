import cv2
import numpy as np


class ColorSpace:
    def __init__(self, frame):
        self.frame = frame

    def rgb_to_gray(self):
        gray = cv2.cvtColor(self.frame, cv2.COLOR_RGB2GRAY)

        return gray

    def gray_to_rgb(self):
        rgb = cv2.cvtColor(self.frame, cv2.COLOR_GRAY2RGB)

        return rgb

    def rgb_to_hls(self):
        hls = cv2.cvtColor(self.frame, cv2.COLOR_RGB2HLS)

        return hls

    def hls_to_rgb(self):
        rgb = cv2.cvtColor(self.frame, cv2.COLOR_HLS2RGB)

        return rgb

    def rgb_to_hsv(self):
        hsv = cv2.cvtColor(self.frame, cv2.COLOR_RGB2HSV)

        return hsv

    def hsv_to_rgb(self):
        rgb = cv2.cvtColor(self.frame, cv2.COLOR_HSV2RGB)

        return rgb

    def rgb_to_lab(self):
        lab = cv2.cvtColor(self.frame, cv2.COLOR_RGB2LAB)

        return lab

    def lab_to_rgb(self):
        rgb = cv2.cvtColor(self.frame, cv2.COLOR_LAB2RGB)

        return rgb

    def rgb_to_bgra(self):
        bgra = cv2.cvtColor(self.frame, cv2.COLOR_RGB2BGRA)

        return bgra

    def bgra_to_rgb(self):
        rgb = cv2.cvtColor(self.frame, cv2.COLOR_BGRA2RGB)

        return rgb

    def rgb_to_xyz(self):
        xyz = cv2.cvtColor(self.frame, cv2.COLOR_RGB2XYZ)

        return xyz

    def xyz_to_rgb(self):
        rgb = cv2.cvtColor(self.frame, cv2.COLOR_XYZ2RGB)

        return rgb

    def rgb_to_cmyk(self):
        # Create float
        bgr = self.frame.astype(float) / 255.

        # Extract channels
        with np.errstate(invalid='ignore', divide='ignore'):
            K = 1 - np.max(bgr, axis=2)
            C = (1 - bgr[..., 2] - K) / (1 - K)
            M = (1 - bgr[..., 1] - K) / (1 - K)
            Y = (1 - bgr[..., 0] - K) / (1 - K)

        # Convert the input BGR image to CMYK colorspace
        cmyk = (np.dstack((C, M, Y, K)) * 255).astype(np.uint8)
        return cmyk

    def cmyk_to_rgb(self):
        # Create float
        cmyk = self.frame.astype(float) / 255.

        # Extract channels
        with np.errstate(invalid='ignore', divide='ignore'):
            K = 1 - np.max(cmyk, axis=2)
            B = 255 * (1 - cmyk[..., 2]) * (1 - K)
            G = 255 * (1 - cmyk[..., 1]) * (1 - K)
            R = 255 * (1 - cmyk[..., 0]) * (1 - K)

            # Convert the input BGR image to CMYK colorspace
        rgb = (np.dstack((R, G, B)) * 255).astype(np.uint8)
        return rgb
