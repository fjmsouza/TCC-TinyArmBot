from backend.controllers.Filter import Filter
from backend.controllers.Morphology import Morphology


class MorphologyManager(Filter):
    var = morphology, frame, morphology_type, c, d, iterations = None, None, None, None, None, None

    def execute(self):

        if self.morphology_type == 'ERODE':
            self.morphology = Morphology(self.frame).erode(self.c, self.d, self.iterations)
        elif self.morphology_type == 'DILATE':
            self.morphology = Morphology(self.frame).dilate(self.c, self.d, self.iterations)
        elif self.morphology_type == 'GRADIENT':
            self.morphology = Morphology(self.frame).gradient(self.c, self.d)
        elif self.morphology_type == 'OPEN':
            self.morphology = Morphology(self.frame).open(self.c, self.d)
        elif self.morphology_type == 'CLOSE':
            self.morphology = Morphology(self.frame).close(self.c, self.d)

        return self.morphology

    def set_parameters(self, frame, morphology_type, c, d, iterations=None):
        self.frame = frame
        self.morphology_type = morphology_type
        self.c = c
        self.d = d
        self.iterations = iterations

    def get_parameters(self):
        pass
