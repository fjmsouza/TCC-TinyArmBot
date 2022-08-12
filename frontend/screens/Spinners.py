from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.screenmanager import Screen


class Spinners(Screen):

    def __init__(self, **kw):
        super().__init__(kw)
        self.menu_video_fps = None
        self.menu_list_fps = None
        self.menu_image_resize = None
        self.menu_image_colorspace = None
        self.menu_list_image_colorspace = None
        self.menu_image_edge = None
        self.menu_list_image_edge = None
        self.menu_image_geometric_transformation = None
        self.menu_list_image_geometric_transformation = None
        self.menu_image_binarization = None
        self.menu_list_image_binarization = None
        self.menu_image_morphology = None
        self.menu_list_image_morphology = None
        self.menu_image_blurring = None
        self.menu_list_image_blurring = None
        self.menu_list_transformation_image = None
        self.menu_choose_visualization_colorspace = None
        self.menu_list_transformation_visualization = None
        self.menu_choose_image_colorspace = None
        self.menu_list_process_image = None
        self.menu_list_image_resize = None

    def spinner_operations(self, value):

        # Blur
        if value == 'Borramento':
            self.text_input.insert_text('BLUR(5, 5)')
            self.menu_image_blurring.dismiss()
        elif value == 'Gaussian':
            self.text_input.insert_text('GAUSSIANBLUR(10)')
            self.menu_image_blurring.dismiss()
        elif value == 'Mediana':
            self.text_input.insert_text('MEDIANBLUR(5)')
            self.menu_image_blurring.dismiss()
        elif value == 'Bilateral':
            self.text_input.insert_text('BILATERAL(7, 49, 49)')
            self.menu_image_blurring.dismiss()

        # Morphology
        elif value == 'Dilatação':
            self.text_input.insert_text('DILATE(5, 5, 1)')
            self.menu_image_morphology.dismiss()
        elif value == 'Erosão':
            self.text_input.insert_text('ERODE(5, 5, 1)')
            self.menu_image_morphology.dismiss()
        elif value == 'Gradiente':
            self.text_input.insert_text('GRADIENT(5, 5)')
            self.menu_image_morphology.dismiss()
        elif value == 'Abertura':
            self.text_input.insert_text('OPEN(5, 5)')
            self.menu_image_morphology.dismiss()
        elif value == 'Fechamento':
            self.text_input.insert_text('CLOSE(5, 5)')
            self.menu_image_morphology.dismiss()

        # Binarization
        elif value == 'Binarização Simples':
            self.text_input.insert_text('THRESHOLD(127)')
            self.menu_image_binarization.dismiss()
        elif value == 'Binarização Adaptiva':
            self.text_input.insert_text('ADAPTIVETHRESHOLD(11, 2)')
            self.menu_image_binarization.dismiss()
        elif value == 'Binarização Gaussiana':
            self.text_input.insert_text('ADAPTIVEGAUTHRESHOLD(11, 2)')
            self.menu_image_binarization.dismiss()
        elif value == 'Binarização de Otsu':
            self.text_input.insert_text('OTSUTHRESHOLD(127)')
            self.menu_image_binarization.dismiss()

        # Edge
        elif value == 'Sobel':
            self.text_input.insert_text('SOBEL(9)')
            self.menu_image_edge.dismiss()
        elif value == 'Canny':
            self.text_input.insert_text('CANNY(100, 200, 10)')
            self.menu_image_edge.dismiss()
        elif value == 'Laplaciano':
            self.text_input.insert_text('LAPLACIAN()')
            self.menu_image_edge.dismiss()

        # Transformation
        elif value == 'Translação':
            self.text_input.insert_text('GEOMETRICTRANSLATION(1, 0, 400, 0, 1, 250)')
            self.menu_image_geometric_transformation.dismiss()
        elif value == 'Rotação':
            self.text_input.insert_text('GEOMETRICROTATION(1, 2, 1, 2, 250, 2)')
            self.menu_image_geometric_transformation.dismiss()
        elif value == 'Retificação':
            self.text_input.insert_text('GEOMETRICRECTIFY()')
            self.menu_image_geometric_transformation.dismiss()

        # Color Space
        elif value == 'RGBTOGRAY':
            self.text_input.insert_text('COLORSPACE(RGBTOGRAY)')
            self.menu_image_colorspace.dismiss()
        elif value == 'RGBTOHLS':
            self.text_input.insert_text('COLORSPACE(RGBTOHLS)')
            self.menu_image_colorspace.dismiss()
        elif value == 'RGBTOHSV':
            self.text_input.insert_text('COLORSPACE(RGBTOHSV)')
            self.menu_image_colorspace.dismiss()
        elif value == 'RGBTOLAB':
            self.text_input.insert_text('COLORSPACE(RGBTOLAB)')
            self.menu_image_colorspace.dismiss()
        elif value == 'RGBTOBGRA':
            self.text_input.insert_text('COLORSPACE(RGBTOBGRA)')
            self.menu_image_colorspace.dismiss()
        elif value == 'RGBTOXYZ':
            self.text_input.insert_text('COLORSPACE(RGBTOXYZ)')
            self.menu_image_colorspace.dismiss()
        elif value == 'RGBTOCMYK':
            self.text_input.insert_text('COLORSPACE(RGBTOCMYK)')
            self.menu_image_colorspace.dismiss()
        elif value == 'GRAYTORGB':
            self.text_input.insert_text('COLORSPACE(GRAYTORGB)')
            self.menu_image_colorspace.dismiss()
        elif value == 'HLSTORGB':
            self.text_input.insert_text('COLORSPACE(HLSTORGB)')
            self.menu_image_colorspace.dismiss()
        elif value == 'HSVTORGB':
            self.text_input.insert_text('COLORSPACE(HSVTORGB)')
            self.menu_image_colorspace.dismiss()
        elif value == 'LABTORGB':
            self.text_input.insert_text('COLORSPACE(LABTORGB)')
            self.menu_image_colorspace.dismiss()
        elif value == 'BGRATORGB':
            self.text_input.insert_text('COLORSPACE(BGRATORGB)')
            self.menu_image_colorspace.dismiss()
        elif value == 'XYZTORGB':
            self.text_input.insert_text('COLORSPACE(XYZTORGB)')
            self.menu_image_colorspace.dismiss()
        elif value == 'CMYKTORGB':
            self.text_input.insert_text('COLORSPACE(CMYKTORGB)')
            self.menu_image_colorspace.dismiss()

        # Resize
        elif value == '25':
            self.text_input.insert_text('RESIZE(25)')
            self.menu_image_resize.dismiss()
        elif value == '25':
            self.text_input.insert_text('RESIZE(50)')
            self.menu_image_resize.dismiss()
        elif value == '25':
            self.text_input.insert_text('RESIZE(75)')
            self.menu_image_resize.dismiss()
        elif value == '25':
            self.text_input.insert_text('RESIZE(100)')
            self.menu_image_resize.dismiss()

    # Dropdownlist for image colorspace
    def process_spinner(self):
        self.menu_list_process_image = [
            {"viewclass": "OneLineListItem", "text": "Espaço de cor",
             "on_release": lambda x="Espaço de cor": self.colorspace_spinner()},
            {"viewclass": "OneLineListItem", "text": "Tamanho (%)",
             "on_release": lambda x="Tamanho (%)": self.resize_spinner()}
        ]
        self.menu_choose_image_colorspace = MDDropdownMenu(
            caller=self.ids.processoptionsbutton,
            items=self.menu_list_process_image,
            width_mult=4
        )
        self.menu_choose_image_colorspace.open()

    # Dropdownlist for image colorspace
    def process_spinner_video(self):
        self.menu_list_process_image = [
            {"viewclass": "OneLineListItem", "text": "Espaço de cor",
             "on_release": lambda x="Espaço de cor": self.colorspace_spinner()},
            {"viewclass": "OneLineListItem", "text": "Tamanho (%)",
             "on_release": lambda x="Tamanho (%)": self.resize_spinner()},
            {"viewclass": "OneLineListItem", "text": "Tamanho (%)",
             "on_release": lambda x="FPS": self.fps_spinner()},
        ]
        self.menu_choose_image_colorspace = MDDropdownMenu(
            caller=self.ids.processoptionsbutton,
            items=self.menu_list_process_image,
            width_mult=4
        )
        self.menu_choose_image_colorspace.open()

    # Dropdownlist for visualization image
    def visualization_spinner(self):
        self.menu_list_transformation_visualization = [
            {"viewclass": "OneLineListItem", "text": "Gerar Cubo de Cores",
             "on_release": lambda x="Cubo": self.generate_cube()},
            {"viewclass": "OneLineListItem", "text": "Gerar Histograma",
             "on_release": lambda x="Histograma": self.generate_histogram()},
            {"viewclass": "OneLineListItem", "text": "Gerar Histograma do Vídeo",
             "on_release": lambda x="Histograma": self.generate_histogram_video_th()},
            {"viewclass": "OneLineListItem", "text": "Detectar Cor",
             "on_release": lambda x="Detectar": self.detect_color()},
            {"viewclass": "OneLineListItem", "text": "Rastrear Cor",
             "on_release": lambda x="Rastrear": self.track_color()},
        ]
        self.menu_choose_visualization_colorspace = MDDropdownMenu(
            caller=self.ids.visualizationbutton,
            items=self.menu_list_transformation_visualization,
            width_mult=4
        )
        self.menu_choose_visualization_colorspace.open()

    # Dropdownlist for image transformations
    def transformations_spinner(self):
        self.menu_list_transformation_image = [
            {"viewclass": "OneLineListItem", "text": "Borramento",
             "on_release": lambda x="Borramento": self.blur_spinner()},
            {"viewclass": "OneLineListItem", "text": "Morfologia",
             "on_release": lambda x="Morfologia": self.morphology_spinner()},
            {"viewclass": "OneLineListItem", "text": "Binarização",
             "on_release": lambda x="Binarização": self.binarization_spinner()},
            {"viewclass": "OneLineListItem", "text": "Transformação Geométrica",
             "on_release": lambda x="Transformação Geométrica": self.geometric_transformation_spinner()},
            {"viewclass": "OneLineListItem", "text": "Bordas", "on_release": lambda x="Bordas": self.edge_spinner()}
        ]

        self.menu_choose_image_colorspace = MDDropdownMenu(
            caller=self.ids.transformationbutton,
            items=self.menu_list_transformation_image,
            width_mult=4
        )
        self.menu_choose_image_colorspace.open()

    # Transformation: Blurring
    def blur_spinner(self):
        self.menu_list_image_blurring = [
            {"viewclass": "OneLineListItem", "text": "Blur",
             "on_release": lambda y="Blur": self.spinner_operations("Borramento")},
            {"viewclass": "OneLineListItem", "text": "Glaussian",
             "on_release": lambda y="Glaussian": self.spinner_operations("Gaussian")},
            {"viewclass": "OneLineListItem", "text": "Mediana",
             "on_release": lambda y="Mediana": self.spinner_operations("Mediana")},
            {"viewclass": "OneLineListItem", "text": "Bilateral",
             "on_release": lambda y="Bilateral": self.spinner_operations("Bilateral")}
        ]
        self.menu_image_blurring = MDDropdownMenu(
            caller=self.ids.transformationbutton,
            items=self.menu_list_image_blurring,
            width_mult=4
        )
        self.menu_image_blurring.open()

    # Transformation: Blurring
    def morphology_spinner(self):
        self.menu_list_image_morphology = [
            {"viewclass": "OneLineListItem", "text": "Dilatação",
             "on_release": lambda y="Dilatação": self.spinner_operations("Dilatação")},
            {"viewclass": "OneLineListItem", "text": "Erosão",
             "on_release": lambda y="Erosão": self.spinner_operations("Erosão")},
            {"viewclass": "OneLineListItem", "text": "Abertura",
             "on_release": lambda y="Abertura": self.spinner_operations("Abertura")},
            {"viewclass": "OneLineListItem", "text": "Fechamento",
             "on_release": lambda y="Fechamento": self.spinner_operations("Fechamento")},
            {"viewclass": "OneLineListItem", "text": "Gradiente",
             "on_release": lambda y="Gradiente": self.spinner_operations("Gradiente")}
        ]
        self.menu_image_morphology = MDDropdownMenu(
            caller=self.ids.transformationbutton,
            items=self.menu_list_image_morphology,
            width_mult=4
        )
        self.menu_image_morphology.open()

    # Transformation: Binarization
    def binarization_spinner(self):
        self.menu_list_image_binarization = [
            {"viewclass": "OneLineListItem", "text": "Simples",
             "on_release": lambda y="Simples": self.spinner_operations("Binarização Simples")},
            {"viewclass": "OneLineListItem", "text": "OTSU",
             "on_release": lambda y="OTSU": self.spinner_operations("Binarização de Otsu")},
            {"viewclass": "OneLineListItem", "text": "Adaptativa Glaussiana",
             "on_release": lambda y="Adaptativa Glaussiana": self.spinner_operations("Binarização Gaussiana")},
            {"viewclass": "OneLineListItem", "text": "Adaptativa",
             "on_release": lambda y="Adaptativa": self.spinner_operations("Binarização Adaptiva")}
        ]
        self.menu_image_binarization = MDDropdownMenu(
            caller=self.ids.transformationbutton,
            items=self.menu_list_image_binarization,
            width_mult=4
        )
        self.menu_image_binarization.open()

    # Transformation: Geometric Transformation
    def geometric_transformation_spinner(self):
        self.menu_list_image_geometric_transformation = [
            {"viewclass": "OneLineListItem", "text": "Translação",
             "on_release": lambda y="Translação": self.spinner_operations("Translação")},
            {"viewclass": "OneLineListItem", "text": "Rotação",
             "on_release": lambda y="Rotação": self.spinner_operations("Rotação")},
            {"viewclass": "OneLineListItem", "text": "Retificação",
             "on_release": lambda y="Retificação": self.spinner_operations("Retificação")}
        ]
        self.menu_image_geometric_transformation = MDDropdownMenu(
            caller=self.ids.transformationbutton,
            items=self.menu_list_image_geometric_transformation,
            width_mult=4
        )
        self.menu_image_geometric_transformation.open()

    # Transformation: Edge
    def edge_spinner(self):
        self.menu_list_image_edge = [
            {"viewclass": "OneLineListItem", "text": "Canny",
             "on_release": lambda y="Canny": self.spinner_operations("Canny")},
            {"viewclass": "OneLineListItem", "text": "Sobel",
             "on_release": lambda y="Sobel": self.spinner_operations("Sobel")},
            {"viewclass": "OneLineListItem", "text": "Laplaciano",
             "on_release": lambda y="Laplaciano": self.spinner_operations("Laplaciano")}
        ]
        self.menu_image_edge = MDDropdownMenu(
            caller=self.ids.transformationbutton,
            items=self.menu_list_image_edge,
            width_mult=4
        )
        self.menu_image_edge.open()

    def colorspace_spinner(self):
        self.menu_list_image_colorspace = [
            {"viewclass": "OneLineListItem", "text": "RGBTOGRAY",
             "on_release": lambda x="GRAY": self.spinner_operations("RGBTOGRAY")},
            {"viewclass": "OneLineListItem", "text": "RGBTOHLS",
             "on_release": lambda x="HLS": self.spinner_operations("RGBTOHLS")},
            {"viewclass": "OneLineListItem", "text": "RGBTOHSV",
             "on_release": lambda x="HSV": self.spinner_operations("RGBTOHSV")},
            {"viewclass": "OneLineListItem", "text": "RGBTOLAB",
             "on_release": lambda x="LAB": self.spinner_operations("RGBTOLAB")},
            {"viewclass": "OneLineListItem", "text": "RGBTOBGRA",
             "on_release": lambda x="BGRA": self.spinner_operations("RGBTOBGRA")},
            {"viewclass": "OneLineListItem", "text": "RGBTOXYZ",
             "on_release": lambda x="XYZ": self.spinner_operations("RGBTOXYZ")},
            {"viewclass": "OneLineListItem", "text": "RGBTOCMYK",
             "on_release": lambda x="CMYK": self.spinner_operations("RGBTOCMYK")},
            {"viewclass": "OneLineListItem", "text": "GRAYTORGB",
             "on_release": lambda x="RGB": self.spinner_operations("GRAYTORGB")},
            {"viewclass": "OneLineListItem", "text": "HLSTORGB",
             "on_release": lambda x="RGB": self.spinner_operations("HLSTORGB")},
            {"viewclass": "OneLineListItem", "text": "HSVTORGB",
             "on_release": lambda x="RGB": self.spinner_operations("HSVTORGB")},
            {"viewclass": "OneLineListItem", "text": "LABTORGB",
             "on_release": lambda x="RGB": self.spinner_operations("LABTORGB")},
            {"viewclass": "OneLineListItem", "text": "BGRATORGB",
             "on_release": lambda x="RGB": self.spinner_operations("BGRATORGB")},
            {"viewclass": "OneLineListItem", "text": "XYZTORGB",
             "on_release": lambda x="RGB": self.spinner_operations("XYZTORGB")},
            {"viewclass": "OneLineListItem", "text": "CMYKTORGB",
             "on_release": lambda x="RGB": self.spinner_operations("CMYKTORGB")}
        ]
        self.menu_image_colorspace = MDDropdownMenu(
            caller=self.ids.processoptionsbutton,
            items=self.menu_list_image_colorspace,
            width_mult=4

        )
        self.menu_image_colorspace.open()

    # Dropdown List for video size
    def resize_spinner(self):
        self.menu_list_image_resize = [
            {"viewclass": "OneLineListItem", "text": "25",
             "on_release": lambda y="25": self.spinner_operations("25")},
            {"viewclass": "OneLineListItem", "text": "50",
             "on_release": lambda y="50": self.spinner_operations("50")},
            {"viewclass": "OneLineListItem", "text": "75",
             "on_release": lambda y="75": self.spinner_operations("75")},
            {"viewclass": "OneLineListItem", "text": "100",
             "on_release": lambda y="100": self.spinner_operations("100")}
        ]
        self.menu_image_resize = MDDropdownMenu(
            caller=self.ids.processoptionsbutton,
            items=self.menu_list_image_resize,
            width_mult=4
        )
        self.menu_image_resize.open()

    # Dropdown List for video FPS
    def fps_spinner(self):
        self.menu_list_fps = [
            {"viewclass": "OneLineListItem", "text": "5", "on_release": lambda y="5": self.video_spinner_fps("5")},
            {"viewclass": "OneLineListItem", "text": "10", "on_release": lambda y="10": self.video_spinner_fps("10")},
            {"viewclass": "OneLineListItem", "text": "15", "on_release": lambda y="15": self.video_spinner_fps("15")},
            {"viewclass": "OneLineListItem", "text": "20", "on_release": lambda y="20": self.video_spinner_fps("20")},
            {"viewclass": "OneLineListItem", "text": "25", "on_release": lambda y="25": self.video_spinner_fps("25")},
            {"viewclass": "OneLineListItem", "text": "30", "on_release": lambda y="30": self.video_spinner_fps("30")},
        ]
        self.menu_video_fps = MDDropdownMenu(
            caller=self.ids.processoptionsbutton,
            items=self.menu_list_fps,
            width_mult=4
        )
        self.menu_video_fps.open()
