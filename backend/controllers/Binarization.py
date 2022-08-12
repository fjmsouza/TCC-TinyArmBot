import cv2


class Binarization:
    def __init__(self, frame):
        self.frame = frame

    def simple_binarization(self, threshold=127):
        img_in = cv2.cvtColor(self.frame, cv2.COLOR_RGB2GRAY)
        ret, thresh = cv2.threshold(img_in, threshold, 255, cv2.THRESH_BINARY)
        thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)

        return thresh

    def otsu_binarization(self, threshold=127):
        img_in = cv2.cvtColor(self.frame, cv2.COLOR_RGB2GRAY)
        ret, thresh = cv2.threshold(img_in, threshold, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)

        return thresh

    def adaptive_binarization(self, blocksize, c):#c is a constant that is subtracted from the mean or weighted sum of the neighbourhood pixels
        img_in = cv2.cvtColor(self.frame, cv2.COLOR_RGB2GRAY)
        thresh = cv2.adaptiveThreshold(img_in, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blocksize, c)
        thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)

        return thresh

    def gaussian_binarization(self, blocksize, c):
        img_in = cv2.cvtColor(self.frame, cv2.COLOR_RGB2GRAY)
        thresh = cv2.adaptiveThreshold(img_in, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blocksize, c)
        thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)

        return thresh
