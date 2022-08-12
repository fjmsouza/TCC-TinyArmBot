from backend.controllers.Filter import Filter
from backend.controllers.Resize import Resize


class ResizeManager(Filter):
    var = resize, frame, resize_image = None, None, None

    def execute(self):
        self.resize_image = Resize(self.frame).resize(self.resize_image)

        return self.resize_image

    def set_parameters(self, frame, resize_image):
        self.frame = frame
        self.resize_image = resize_image

    def get_parameters(self):
        pass
