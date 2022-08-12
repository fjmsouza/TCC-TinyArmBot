import threading
import time
import cv2

from kivy.uix.screenmanager import Screen
from kivy.graphics.texture import Texture
from kivy.core.window import Window
from kivy.app import App

from frontend.screens.ButtonMessageError import ButtonError
from frontend.screens.OpenFiles import OpenFiles
from frontend.screens.Spinners import Spinners
from backend.managers.ConfigurationRepository import ConfigurationRepository
from backend.managers.VisualizationManager import VisualizationManager
from backend.managers.OCRManager import OCRManager
from backend.controllers.Organize import Organize


class MyBoxLayoutImage(Screen):
    a = image_path, lst, imageColorSpace, image_resize, json_path = None, None, 'RGB', '100', None
    b = list_general, list_aux, img_aux, process, arg, image_json, content = [], [], None, None, None, None, None
    c = list_images, list_processed_images, N1, N2, N1Size, N2Size = None, None, None, None, None, None
    d = text_input, path_arch_final, pre_list_processed_images, list_path_final_names = None, None, [], []

    @staticmethod
    def message_error(message):
        ButtonError.message_error(message)

    @staticmethod
    def open_file(message, multiple):
        file_open = OpenFiles.open_file(message, multiple)

        return file_open

    def show_process_image(self, frame):
        try:
            image_show = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        except (Exception,):
            image_show = frame

        buf = cv2.flip(image_show, 0)
        image_texture = Texture.create(size=(image_show.shape[1], image_show.shape[0]), icolorfmt='bgr')
        image_texture.blit_buffer(buf.tobytes(), colorfmt='bgr')
        video = self.ids['my_image2']
        video.texture = image_texture

    def select_image(self):
        try:
            self.list_images = self.open_file('Selecione uma imagem', True)
            self.N1 = 0
            self.image_path = self.list_images[0]

            self.img_aux = cv2.imread(self.image_path)
            self.image_json = cv2.imread(self.image_path)

            # Exibe a Imagem Selecionada
            self.ids.my_image.source = self.image_path

        except (Exception,):
            self.message_error("Selecione algum arquivo")

    def select_json(self):
        try:
            self.json_path = self.open_file('Selecione um JSON', False)

            json_display = ConfigurationRepository.json_read_display(self.json_path)
            self.ids.labeltesteimage.text = json_display

        except (Exception,):
            self.message_error("Selecione algum JSON")

    def process_json(self):
        try:
            instance = ConfigurationRepository

            for i in range(len(self.list_images)):
                self.img_aux = cv2.imread(self.list_images[i])

                ConfigurationRepository.set_config(instance, self.img_aux, json_path=self.json_path)
                out_image = ConfigurationRepository.execute(instance)

                self.path_arch_final = str(time.strftime("%Y%m%d-%H%M%S")) + "N" + str(i) + '.jpg'

                self.pre_list_processed_images.append(out_image)
            self.list_processed_images = self.pre_list_processed_images
            self.N2 = 0
            self.show_process_image(self.list_processed_images[0])  # Função criada para exibir a imagem processada

        except (Exception,):
            self.message_error('Selecione algum JSON!')

    def process_json_th(self):
        threading.Thread(target=self.process_json).start()

    def save_json(self):
        try:
            instance = ConfigurationRepository
            ConfigurationRepository.list_json_creat(instance, self.list_general)
            ConfigurationRepository.json_create(instance)
            self.list_aux.clear()

        except (Exception,):
            self.message_error('Para salvar algum JSON, realize algum processamento!')

    def apply_easy_ocr(self):
        try:
            for i in range(len(self.list_processed_images)):
                instance = OCRManager
                OCRManager.set_parameters(instance, self.list_processed_images[i], 'EASYYOLO')
                out_text = OCRManager.execute(instance)
                out_text = Organize.Organize(out_text)
                
                self.ids.labelsaidaocr.text = str(out_text)

        except (Exception,):
            self.message_error('Adicione alguma operação!')

    def apply_easy_ocr_th(self):
        threading.Thread(target=self.apply_easy_ocr).start()

    def apply_tesseract_ocr(self):
        try:
            for i in range(len(self.list_processed_images)):
                instance = OCRManager
                OCRManager.set_parameters(instance, self.list_processed_images[i], 'TESSYOLO')
                out_text = OCRManager.execute(instance)
                out_text = Organize.Organize(out_text)

                self.ids.labelsaidaocr.text = str(out_text)

        except (Exception,):
            self.message_error('Adicione alguma operação!')

    def spinner_operations(self, value):
        self.text_input = self.ids['textlist']

        Spinners.spinner_operations(self, value)

    def list_add_operations(self):
        try:
            self.content = self.text_input.text
            self.list_aux.append(self.content)
            self.text_input.select_all()
            self.text_input.delete_selection(from_undo=False)

            operation = ''
            for i in self.list_aux:
                operation = operation + '\n' + i
                self.ids.labeltesteimage.text = operation

            if len(self.list_aux) == 0:
                self.ids.labeltesteimage.text = ''

            print(self.list_aux)

        except (Exception,):
            self.message_error('Adicione alguma operação!')

    def list_remove_operations(self):
        try:
            self.list_aux.pop()

            operation = ''
            for i in self.list_aux:
                operation = operation + '\n' + i
                self.ids.labeltesteimage.text = operation

            if len(self.list_aux) == 0:
                self.ids.labeltesteimage.text = ''

            print(self.list_aux)

        except (Exception,):
            self.message_error('Adicione alguma operação!')

    # Dropdownlist for image colorspace
    def process_spinner(self):
        Spinners.process_spinner(self)

    # Dropdownlist for visualization image
    def visualization_spinner(self):
        Spinners.visualization_spinner(self)

    def transformations_spinner(self):
        Spinners.transformations_spinner(self)

    # Transformation: Blurring
    def blur_spinner(self):
        Spinners.blur_spinner(self)

    # Transformation: Morphology
    def morphology_spinner(self):
        Spinners.morphology_spinner(self)

    # Transformation: Binarization
    def binarization_spinner(self):
        Spinners.binarization_spinner(self)

    # Transformation: Geometric Transformation
    def geometric_transformation_spinner(self):
        Spinners.geometric_transformation_spinner(self)

    # Transformation: Edge
    def edge_spinner(self):
        Spinners.edge_spinner(self)

    def colorspace_spinner(self):
        Spinners.colorspace_spinner(self)

    # Dropdown List for video size
    def resize_spinner(self):
        Spinners.resize_spinner(self)

    def process_image(self):
        try:
            self.pre_list_processed_images = []
            for i in range(len(self.list_images)):
                self.img_aux = cv2.imread(self.list_images[i])
                self.path_arch_final = str(time.strftime("%Y%m%d-%H%M%S")) + "N" + str(i) + '.jpg'

                instance = ConfigurationRepository
                ConfigurationRepository.set_config(instance, self.img_aux, list_operations=self.list_aux)
                out_image = ConfigurationRepository.execute(instance)

                self.pre_list_processed_images.append(out_image)
                self.list_path_final_names.append(self.path_arch_final)

            self.list_processed_images = self.pre_list_processed_images
            self.N2 = 0
            self.show_process_image(self.list_processed_images[0])  # Função criada para exibir a imagem processada

            for n in self.list_aux:
                self.list_general.append(n)

        except (Exception,):
            if self.image_path is None:
                self.message_error("Selecione algum arquivo")
            else:
                self.message_error("Erro ao processar imagem")

    def save_images(self):
        try:
            for i in range(len(self.pre_list_processed_images)):
                cv2.imwrite(str(self.list_path_final_names[i]) + '.jpg', self.pre_list_processed_images[i])

        except (Exception,):
            if self.path_arch_final is None:
                self.message_error("Selecione e processe alguma imagem para poder salvar")
            else:
                self.message_error("Erro ao salvar imagem")

    def generate_cube(self):
        try:
            frame = cv2.imread(self.image_path)
            instance = VisualizationManager
            VisualizationManager.set_parameters(instance, frame, 'COLORCUBE')
            color_cube = VisualizationManager.execute(instance)

            self.show_process_image(color_cube)

        except (Exception,):
            if self.image_path is None:
                self.message_error("Selecione algum arquivo")
            else:
                self.message_error("Erro ao gerar o cubo")

    def generate_histogram(self):
        try:
            frame = cv2.imread(self.image_path)
            instance = VisualizationManager
            VisualizationManager.set_parameters(instance, frame, 'ORIGINALHISTOGRAM')
            histogram = VisualizationManager.execute(instance)

            self.show_process_image(histogram)

        except (Exception,):
            if self.image_path is None:
                self.message_error("Selecione algum arquivo")
            else:
                self.message_error("Erro ao gerar o histograma")

    def detect_color_image(self):
        # MyRangeDetector.main("RGB", self.image_path)
        pass

    def track_color_image(self):
        # Detector.detector("IMAGE", self.image_path)
        pass

    def left_button_image(self):
        try:
            self.N1 = self.N1 - 1

            if int(len(self.list_images)) > self.N1 >= 0:

                self.image_path = self.list_images[self.N1]
                self.ids.my_image.source = self.image_path
                self.show_process_image(self.list_processed_images[self.N1])

            elif self.N1 < 0:
                self.N1 = int(len(self.list_images)) - 1

                self.image_path = self.list_images[self.N1]
                self.ids.my_image.source = self.image_path
                self.show_process_image(self.list_processed_images[self.N1])

        except (Exception,):
            self.message_error("Selecione alguma imagem")

    def right_button_image(self):
        try:
            self.N1 = self.N1 + 1

            if self.N1 < int(len(self.list_images)):

                self.image_path = self.list_images[self.N1]
                self.ids.my_image.source = self.image_path
                self.show_process_image(self.list_processed_images[self.N1])

            elif self.N1 >= int(len(self.list_images)):
                self.N1 = 0

                self.image_path = self.list_images[self.N1]
                self.ids.my_image.source = self.image_path
                self.show_process_image(self.list_processed_images[self.N1])
        except (Exception,):
            self.message_error("Selecione alguma imagem")

    def clean_images(self):
        self.list_images = []
        self.list_processed_images = []

        self.ids.my_image.source = 'assets/branco.jpg'
        self.ids.my_image2.source = 'assets/branco.jpg'

    # Quando apertar ESC volta para a tela de menu
    @staticmethod
    def back_button(key):
        if key == 27:
            App.get_running_app().root.current = "home"
            return True

    # Eventos do teclado
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.back_button)
