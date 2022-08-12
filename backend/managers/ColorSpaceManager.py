from backend.controllers.Filter import Filter
from backend.controllers.ColorSpace import ColorSpace


class ColorSpaceManager(Filter):
    var = conversion, frame, contype = None, None, None

    def execute(self):

        if self.contype == 'RGBTOGRAY':
            self.conversion = ColorSpace(self.frame).rgb_to_gray()

        elif self.contype == 'GRAYTORGB':
            self.conversion = ColorSpace(self.frame).gray_to_rgb()

        elif self.contype == 'RGBTOHLS':
            self.conversion = ColorSpace(self.frame).rgb_to_hls()

        elif self.contype == 'HLSTORGB':
            self.conversion = ColorSpace(self.frame).hls_to_rgb()

        elif self.contype == 'RGBTOHSV':
            self.conversion = ColorSpace(self.frame).rgb_to_hsv()

        elif self.contype == 'HSVTORGB':
            self.conversion = ColorSpace(self.frame).hsv_to_rgb()

        elif self.contype == 'RGBTOLAB':
            self.conversion = ColorSpace(self.frame).rgb_to_lab()

        elif self.contype == 'LABTORGB':
            self.conversion = ColorSpace(self.frame).lab_to_rgb()

        elif self.contype == 'RGBTOBGRA':
            self.conversion = ColorSpace(self.frame).rgb_to_bgra()

        elif self.contype == 'BGRATORGB':
            self.conversion = ColorSpace(self.frame).bgra_to_rgb()

        elif self.contype == 'RGBTOXYZ':
            self.conversion = ColorSpace(self.frame).rgb_to_xyz()

        elif self.contype == 'XYZTORGB':
            self.conversion = ColorSpace(self.frame).xyz_to_rgb()

        elif self.contype == 'RGBTOCMYK':
            self.conversion = ColorSpace(self.frame).rgb_to_cmyk()

        elif self.contype == 'CMYKTORGB':
            self.conversion = ColorSpace(self.frame).cmyk_to_rgb()

        return self.conversion

    def set_parameters(self, frame, contype):
        self.frame = frame
        self.contype = contype

    def get_parameters(self):
        pass
