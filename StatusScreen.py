import cv2
import numpy as np
import imutils
import Ocr
import Determinant


def preprocess(frame):
    prepared_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    prepared_frame = cv2.GaussianBlur(src=prepared_frame, ksize=(5, 5), sigmaX=0)

    # frame = imutils.resize(frame, height=480)

    # frame[frame<50]=0
    # frame[frame > 90] = 255

    # borra
    # frame = cv2.medianBlur(frame,3)          #funfou melhor 3,3

    # limiariza
    # frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 3)
    #
    # frame = cv2.bilateralFilter(frame, 20, 200, 250)
    # frame = cv2.Laplacian(frame, cv2.CV_8U ,ksize=3)    #funfou melhor
    # frame = cv2.Canny(frame, 30,30)
    # frame[frame != 0] = (0, 255, 0)

    # #Laplace
    # ddepth = cv2.CV_8U
    # kernel_size = 3
    # # [laplacian]
    # # Apply Laplace function
    # dst = cv2.Laplacian(frame, ddepth, ksize=kernel_size)
    # # [laplacian]
    # # [convert]
    # # converting back to uint8
    # abs_dst = cv2.convertScaleAbs(dst)
    # # [convert]
    # frame = abs_dst

    #Canny
    # th1 = 50
    # th2 = 130  # Canny recomenda que threshold2 seja 3x o threshold1 - muda e teste
    # d = 3  # Gaussian Blur
    # edgeresult = frame
    # edgeresult = cv2.GaussianBlur(edgeresult, (2 * d + 1, 2 * d + 1), -1)[d:-d, d:-d]
    # gray = cv2.cvtColor(edgeresult, cv2.COLOR_BGR2GRAY)
    # edge = cv2.Canny(gray, th1, th2)
    # edgeresult[edge != 0] = (0, 255, 0)
    # frame = cv2.cvtColor(edgeresult, cv2.COLOR_BGR2RGB)




    #binariza
    # ret,frame = cv2.threshold(frame,91,255,cv2.THRESH_BINARY)
    # borra
    # frame = cv2.medianBlur(frame,3)
    # frame = cv2.GaussianBlur(frame, (3, 3), 2)  # funfou melhor
    # frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 3)
    # frame = cv2.bilateralFilter(frame, 20, 200, 250)
    # ret, frame = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # manual thresholding
    # th2 = 93  # this threshold might vary!
    # frame[frame >= th2] = 255
    # frame[frame < th2] = 0

    #
    # kernel = np.ones((2, 2), np.uint8)          #funfou melhor com 2,2
    # frame = cv2.dilate(frame, kernel, iterations=1)

    # borra
    # frame = cv2.medianBlur(frame,3)
    # frame = cv2.GaussianBlur(frame, (1, 1), 2)

    # frame = cv2.medianBlur(frame,3)
    # ret,frame = cv2.threshold(frame,80,255,cv2.THRESH_BINARY_INV)


    return prepared_frame

def execute(frame):
    # usar ocrs como "hash"??? ou diff de imagens mesmo?
    frame = preprocess(frame)
    # status_screen = Ocr.applyPytesseract(frame)
    # frame = Ocr.applyEasyocr(frame)

    det = Determinant.determinant(frame)
    return det