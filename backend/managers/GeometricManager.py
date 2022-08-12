from backend.controllers.Filter import Filter
from backend.controllers.Geometric import Geometric


class GeometricManager(Filter):
    var1 = geometric, frame, geometric_type = None, None, None
    var2 = a, b, c, d, e, f = None, None, None, None, None, None,

    def execute(self):

        if self.geometric_type == 'GEOMETRICTRANSLATION':
            self.geometric = Geometric(self.frame).translation(self.a, self.b, self.c, self.d, self.e, self.f)

        elif self.geometric_type == 'GEOMETRICROTATION':
            self.geometric = Geometric(self.frame).rotation(self.a, self.b, self.c, self.d, self.e, self.f)

        elif self.geometric_type == 'GEOMETRICRECTIFY':
            self.geometric = Geometric(self.frame).rectify()

        return self.geometric

    def set_parameters(self, frame, geometric_type, a=None, b=None, c=None, d=None, e=None, f=None, x0=None, y0=None, x1=None,
                       y1=None, x2=None, y2=None, x3=None, y3=None):
        self.frame = frame
        self.geometric_type = geometric_type
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def get_parameters(self):
        pass
