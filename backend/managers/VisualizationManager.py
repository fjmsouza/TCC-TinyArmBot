from backend.controllers.Filter import Filter
from backend.controllers.Visualization import Visualization


# TODO: Ver cubo de cores
class VisualizationManager(Filter):
    var = visualization, frame, visualization_type, path, space_color = None, None, None, None, None

    def execute(self):

        if self.visualization_type == 'ORIGINALHISTOGRAM':
            self.visualization = Visualization(self.frame).histogram_original_image()
        elif self.visualization_type == 'PROCESSEDHISTOGRAM':
            self.visualization = Visualization(self.frame).histogram_processed_image(space_color=self.space_color)
        elif self.visualization_type == 'COLORCUBE':
            self.visualization = Visualization(self.frame).color_cube()
        elif self.visualization_type == 'HISTOGRAMVIDEO':
            self.visualization = Visualization(self.frame).histogram_video(path=self.path, space_color=self.space_color)

        return self.visualization

    def set_parameters(self, frame, visualization_type, path=None, space_color=None):
        self.frame = frame
        self.visualization_type = visualization_type
        self.space_color = space_color
        self.path = path

    def get_parameters(self):
        pass
