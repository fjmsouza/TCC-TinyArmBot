from backend.controllers.Filter import Filter
from backend.controllers.Binarization import Binarization


class BinarizationManager(Filter):
    var = binarization, frame, binarization_type, threshold, blocksize, c = None, None, None, None, None, None

    def execute(self):

        if self.binarization_type == 'THRESHOLD':
            self.binarization = Binarization(self.frame).simple_binarization(self.threshold)
        elif self.binarization_type == 'OTSUTHRESHOLD':
            self.binarization = Binarization(self.frame).otsu_binarization(self.threshold)
        elif self.binarization_type == 'ADAPTIVETHRESHOLD':
            self.binarization = Binarization(self.frame).adaptive_binarization(self.blocksize, self.c)
        elif self.binarization_type == 'ADAPTIVEGAUTHRESHOLD':
            self.binarization = Binarization(self.frame).gaussian_binarization(self.blocksize, self.c)

        return self.binarization

    def set_parameters(self, frame, binarization_type, threshold=None, blocksize=None, c=None):
        self.frame = frame
        self.binarization_type = binarization_type
        self.threshold = threshold
        self.blocksize = blocksize
        self.c = c

    def get_parameters(self):
        pass
