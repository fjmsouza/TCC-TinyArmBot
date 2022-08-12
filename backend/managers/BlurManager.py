from backend.controllers.Filter import Filter
from backend.controllers.Blur import Blur


class BlurManager(Filter):
    var = blur, frame, blur_type, c, d, ksize, sigma_color, sigma_space = None, None, None, None, None, None, None, None

    def execute(self):

        if self.blur_type == 'BLUR':
            self.blur = Blur(self.frame).simple_blur(self.c, self.d)
        elif self.blur_type == 'GAUSSIANBLUR':
            self.blur = Blur(self.frame).gaussian_blur(self.d)
        elif self.blur_type == 'MEDIANBLUR':
            self.blur = Blur(self.frame).median_blur(self.ksize)
        elif self.blur_type == 'BILATERAL':
            self.blur = Blur(self.frame).bilateral_blur(self.d, self.sigma_color, self.sigma_space)

        return self.blur

    def set_parameters(self, frame, blur_type, c=None, d=None, ksize=None, sigma_color=None, sigma_space=None):
        self.frame = frame
        self.blur_type = blur_type
        self.c = c
        self.d = d
        self.ksize = ksize
        self.sigma_color = sigma_color
        self.sigma_space = sigma_space

    def get_parameters(self):
        pass
