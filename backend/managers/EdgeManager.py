from backend.controllers.Filter import Filter
from backend.controllers.Edge import Edge


class EdgeManager(Filter):
    var = edge, frame, edge_type, ksize, threshold1, threshold2, d = None, None, None, None, None, None, None

    def execute(self):

        if self.edge_type == 'CANNY':
            self.edge = Edge(self.frame).canny_edge(self.threshold1, self.threshold2, self.d)
        elif self.edge_type == 'SOBEL':
            self.edge = Edge(self.frame).sobel_edge(self.ksize)
        elif self.edge_type == 'LAPLACIAN':
            self.edge = Edge(self.frame).laplacian_edge()

        return self.edge

    def set_parameters(self, frame, edge_type, ksize=None, threshold1=None, threshold2=None, d=None):
        self.frame = frame
        self.edge_type = edge_type
        self.ksize = ksize
        self.threshold1 = threshold1
        self.threshold2 = threshold2
        self.d = d

    def get_parameters(self):
        pass
