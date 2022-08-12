import time

import cv2
import matplotlib
from matplotlib import pyplot as plt
from PIL import Image
import io
import numpy as np


# TODO: Nesse arquivo tem que modificar a saída das funções para retornar uma imagem ao inves de plotar
class Visualization:
    def __init__(self, frame):
        self.frame = frame

    def histogram_original_image(self):
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histogram = cv2.calcHist([self.frame], [i], None, [256], [0, 256])
            plt.plot(histogram, color=col)
            plt.xlim([0, 256])
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='jpg')
        image = Image.open(img_buf)
        frame = np.asarray(image)

        return frame

    def color_cube(self):

        cv2.imwrite('teste.jpg', self.frame)
        image = Image.open('teste.jpg')

        px = image.load()

        height, width = self.frame.shape[:2]
        ax = plt.axes(projection='3d')
        x = []
        y = []
        z = []
        c = []

        unique_pixels = set([px[col, row]
                             for row in range(image.height)
                             for col in range(image.width)])

        for pix in unique_pixels:
            new_col = (pix[0] / 255, pix[1] / 255, pix[2] / 255)
            x.append(pix[0])
            y.append(pix[1])
            z.append(pix[2])
            c.append(new_col)

        ax.scatter(x, y, z, s=0.1, c=c)
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='jpg')
        im = Image.open(img_buf)
        frame = np.asarray(im)
        plt.show()
        return frame

    def histogram_processed_image(self, space_color):

        if space_color == 'GRAY' or 'RGB':
            r, g, b = self.frame[:, :, 0], self.frame[:, :, 1], self.frame[:, :, 2]
            histogram_r = cv2.calcHist([r], [0], None, [256], [0, 256])
            histogram_g = cv2.calcHist([g], [0], None, [256], [0, 256])
            histogram_b = cv2.calcHist([b], [0], None, [256], [0, 256])
            plt.plot(histogram_r, color='r', label="r")
            plt.plot(histogram_g, color='g', label="g")
            plt.plot(histogram_b, color='b', label="b")
            image_buf = io.BytesIO()
            plt.savefig(image_buf, format='jpg')
            image = Image.open(image_buf)
            frame = np.asarray(image)
            return frame

        elif space_color == 'HLS':
            h, l, s = self.frame[:, :, 0], self.frame[:, :, 1], self.frame[:, :, 2]
            histogram_h = cv2.calcHist([h], [0], None, [256], [0, 256])
            histogram_l = cv2.calcHist([l], [0], None, [256], [0, 256])
            histogram_s = cv2.calcHist([s], [0], None, [256], [0, 256])
            plt.plot(histogram_h, color='r', label="h")
            plt.plot(histogram_l, color='g', label="l")
            plt.plot(histogram_s, color='b', label="s")
            image_buf = io.BytesIO()
            plt.savefig(image_buf, format='jpg')
            image = Image.open(image_buf)
            frame = np.asarray(image)
            return frame

        elif space_color == 'HSV':
            h, s, v = self.frame[:, :, 0], self.frame[:, :, 1], self.frame[:, :, 2]
            histogram_h = cv2.calcHist([h], [0], None, [256], [0, 256])
            histogram_s = cv2.calcHist([s], [0], None, [256], [0, 256])
            histogram_v = cv2.calcHist([v], [0], None, [256], [0, 256])
            plt.plot(histogram_h, color='r', label="h")
            plt.plot(histogram_s, color='g', label="s")
            plt.plot(histogram_v, color='b', label="v")
            image_buf = io.BytesIO()
            plt.savefig(image_buf, format='jpg')
            image = Image.open(image_buf)
            frame = np.asarray(image)
            return frame

        elif space_color == 'LAB':
            l, a, b = self.frame[:, :, 0], self.frame[:, :, 1], self.frame[:, :, 2]
            histogram_l = cv2.calcHist([l], [0], None, [256], [0, 256])
            histogram_a = cv2.calcHist([a], [0], None, [256], [0, 256])
            histogram_b = cv2.calcHist([b], [0], None, [256], [0, 256])
            plt.plot(histogram_l, color='r', label="l")
            plt.plot(histogram_a, color='g', label="a")
            plt.plot(histogram_b, color='b', label="b")
            image_buf = io.BytesIO()
            plt.savefig(image_buf, format='jpg')
            image = Image.open(image_buf)
            frame = np.asarray(image)
            return frame

        elif space_color == 'BGRA':
            b, g, r = self.frame[:, :, 0], self.frame[:, :, 1], self.frame[:, :, 2]
            histogram_b = cv2.calcHist([b], [0], None, [256], [0, 256])
            histogram_g = cv2.calcHist([g], [0], None, [256], [0, 256])
            histogram_r = cv2.calcHist([r], [0], None, [256], [0, 256])

            plt.plot(histogram_b, color='r', label="b")
            plt.plot(histogram_g, color='g', label="g")
            plt.plot(histogram_r, color='b', label="r")
            image_buf = io.BytesIO()
            plt.savefig(image_buf, format='jpg')
            image = Image.open(image_buf)
            frame = np.asarray(image)
            return frame

        elif space_color == 'XYZ':
            x, y, z = self.frame[:, :, 0], self.frame[:, :, 1], self.frame[:, :, 2]
            histogram_x = cv2.calcHist([x], [0], None, [256], [0, 256])
            histogram_y = cv2.calcHist([y], [0], None, [256], [0, 256])
            histogram_z = cv2.calcHist([z], [0], None, [256], [0, 256])
            plt.plot(histogram_x, color='r', label="x")
            plt.plot(histogram_y, color='g', label="y")
            plt.plot(histogram_z, color='b', label="z")
            image_buf = io.BytesIO()
            plt.savefig(image_buf, format='jpg')
            image = Image.open(image_buf)
            frame = np.asarray(image)
            return frame

        elif space_color == 'CMYK':
            c, m, y = self.frame[:, :, 0], self.frame[:, :, 1], self.frame[:, :, 2]
            histogram_c = cv2.calcHist([c], [0], None, [256], [0, 256])
            histogram_m = cv2.calcHist([m], [0], None, [256], [0, 256])
            histogram_y = cv2.calcHist([y], [0], None, [256], [0, 256])

            plt.plot(histogram_c, color='r', label="c")
            plt.plot(histogram_m, color='g', label="m")
            plt.plot(histogram_y, color='b', label="y")
            image_buf = io.BytesIO()
            plt.savefig(image_buf, format='jpg')
            image = Image.open(image_buf)
            frame = np.asarray(image)
            return frame

    def histogram_video(self, path, space_color):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        video = cv2.VideoCapture(path)
        size = (640, 480)
        fps = int(video.get(cv2.CAP_PROP_FPS))

        result = cv2.VideoWriter('/Home/Documents/GitHub/Ferramenta_de_PI/Resources/Output/Histogram.mp4'
                                 , cv2.VideoWriter_fourcc(*'IMC4'), fps, size)

        while True:
            ret, frame = video.read()
            if ret:
                if space_color == 'GRAY' or space_color == 'RGB':
                    r, g, b = frame[:, :, 0], frame[:, :, 1], frame[:, :, 2]
                    hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])
                    hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
                    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
                    plt.plot(hist_r, color='r', label="r")
                    plt.plot(hist_g, color='g', label="g")
                    plt.plot(hist_b, color='b', label="b")
                    plt.legend()
                    matplotlib.use("Agg")
                    img_buf = io.BytesIO()
                    plt.savefig(img_buf, format='png')
                    im = Image.open(img_buf)
                    imgArray = np.asarray(im)
                    plt.close()
                    result.write(imgArray)

                if space_color == 'HLS':
                    h, l, s = frame[:, :, 0], frame[:, :, 1], frame[:, :, 2]
                    hist_h = cv2.calcHist([h], [0], None, [256], [0, 256])
                    hist_l = cv2.calcHist([l], [0], None, [256], [0, 256])
                    hist_s = cv2.calcHist([s], [0], None, [256], [0, 256])
                    plt.plot(hist_h, color='r', label="h")
                    plt.plot(hist_l, color='g', label="l")
                    plt.plot(hist_s, color='b', label="s")
                    plt.legend()
                    matplotlib.use("Agg")
                    img_buf = io.BytesIO()
                    plt.savefig(img_buf, format='png')
                    im = Image.open(img_buf)
                    imgArray = np.asarray(im)
                    plt.close()
                    result.write(imgArray)

                if space_color == 'HSV':
                    h, s, v = frame[:, :, 0], frame[:, :, 1], frame[:, :, 2]
                    hist_h = cv2.calcHist([h], [0], None, [256], [0, 256])
                    hist_s = cv2.calcHist([s], [0], None, [256], [0, 256])
                    hist_v = cv2.calcHist([v], [0], None, [256], [0, 256])
                    plt.plot(hist_h, color='r', label="h")
                    plt.plot(hist_s, color='g', label="s")
                    plt.plot(hist_v, color='b', label="v")
                    plt.legend()
                    matplotlib.use("Agg")
                    img_buf = io.BytesIO()
                    plt.savefig(img_buf, format='png')
                    im = Image.open(img_buf)
                    imgArray = np.asarray(im)
                    plt.close()
                    result.write(imgArray)

                if space_color == 'LAB':
                    l, a, b = frame[:, :, 0], frame[:, :, 1], frame[:, :, 2]
                    hist_l = cv2.calcHist([l], [0], None, [256], [0, 256])
                    hist_a = cv2.calcHist([a], [0], None, [256], [0, 256])
                    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
                    plt.plot(hist_l, color='r', label="l")
                    plt.plot(hist_a, color='g', label="a")
                    plt.plot(hist_b, color='b', label="b")
                    plt.legend()
                    matplotlib.use("Agg")
                    img_buf = io.BytesIO()
                    plt.savefig(img_buf, format='png')
                    im = Image.open(img_buf)
                    imgArray = np.asarray(im)
                    plt.close()
                    result.write(imgArray)

                if space_color == 'BGRA':
                    b, g, r = frame[:, :, 0], frame[:, :, 1], frame[:, :, 2]
                    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
                    hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
                    hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

                    plt.plot(hist_b, color='r', label="b")
                    plt.plot(hist_g, color='g', label="g")
                    plt.plot(hist_r, color='b', label="r")
                    plt.legend()
                    matplotlib.use("Agg")
                    img_buf = io.BytesIO()
                    plt.savefig(img_buf, format='png')
                    im = Image.open(img_buf)
                    imgArray = np.asarray(im)
                    plt.close()
                    result.write(imgArray)

                if space_color == 'XYZ':
                    x, y, z = frame[:, :, 0], frame[:, :, 1], frame[:, :, 2]
                    hist_x = cv2.calcHist([x], [0], None, [256], [0, 256])
                    hist_y = cv2.calcHist([y], [0], None, [256], [0, 256])
                    hist_z = cv2.calcHist([z], [0], None, [256], [0, 256])
                    plt.plot(hist_x, color='r', label="x")
                    plt.plot(hist_y, color='g', label="y")
                    plt.plot(hist_z, color='b', label="z")
                    plt.legend()
                    matplotlib.use("Agg")
                    img_buf = io.BytesIO()
                    plt.savefig(img_buf, format='png')
                    im = Image.open(img_buf)
                    imgArray = np.asarray(im)
                    plt.close()
                    result.write(imgArray)

                if space_color == 'CMYK':
                    c, m, y = frame[:, :, 0], frame[:, :, 1], frame[:, :, 2]
                    hist_c = cv2.calcHist([c], [0], None, [256], [0, 256])
                    hist_m = cv2.calcHist([m], [0], None, [256], [0, 256])
                    hist_y = cv2.calcHist([y], [0], None, [256], [0, 256])

                    plt.plot(hist_c, color='r', label="c")
                    plt.plot(hist_m, color='g', label="m")
                    plt.plot(hist_y, color='b', label="y")
                    plt.legend()
                    matplotlib.use("Agg")
                    img_buf = io.BytesIO()
                    plt.savefig(img_buf, format='png')
                    im = Image.open(img_buf)
                    imgArray = np.asarray(im)
                    plt.close()
                    result.write(imgArray)
            else:
                break

        print('Histograma do vídeo gerado')
        result.release()
        video.release()
        cv2.destroyAllWindows()
