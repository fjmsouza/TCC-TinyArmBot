import time

import cv2

from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.core.window import Window
from kivy.app import App

from frontend.screens.ButtonMessageError import ButtonError
from frontend.screens.OpenFiles import OpenFiles
from frontend.screens.Spinners import Spinners
from backend.managers.ConfigurationRepository import ConfigurationRepository


class MyBoxLayoutCamera(Screen):
    a = cameraColorSpace, cameraFPS, flagDetect, flagRange, content, json_path = 'RGB', '30', False, False, None, None
    b = listaGeneral, list_aux, flag_cam, text_input, now_frame, now_frame2 = [], [], False, None, None, None
    c = save_flag = False

    image_texture = ObjectProperty(None)
    image_capture = ObjectProperty(None)
    image_capture2 = ObjectProperty(None, allownone=True)

    @staticmethod
    def message_error(message):
        ButtonError.message_error(message)

    @staticmethod
    def open_file(messsage, multiple):
        file_open = OpenFiles.open_file(messsage, multiple)

        return file_open

    # Operations
    def spinner_operations(self, value):
        self.text_input = self.ids['textlist']
        Spinners.spinner_operations(self, value)

    def list_add_operations(self):
        try:
            self.content = self.text_input.text
            self.list_aux.append(self.content)
            self.text_input.select_all()
            self.text_input.delete_selection(from_undo=False)

            operations = ''
            for i in self.list_aux:
                operations = operations + '\n' + i
                self.ids.labeltesteimage.text = operations

            if len(self.list_aux) == 0:
                self.ids.labeltesteimage.text = ''

            print(self.list_aux)
        except (Exception,):
            self.message_error('Adicione alguma operação!')

    def list_remove_operations(self):
        try:
            self.list_aux.pop()

            operations = ''
            for i in self.list_aux:
                operations = operations + '\n' + i
                self.ids.labeltesteimage.text = operations

            if len(self.list_aux) == 0:
                self.ids.labeltesteimage.text = ''

            print(self.list_aux)
        except (Exception,):
            self.message_error('Adicione alguma operação!')

    def process_spinner(self):
        Spinners.process_spinner(self)

    # Dropdownlist for visualization image
    def visualization_spinner(self):
        Spinners.visualization_spinner(self)

    # Dropdownlist for transformation videooptions
    def transformations_spinner(self):
        Spinners.transformations_spinner(self)

    # Transformation: Blurring
    def blur_spinner(self):
        Spinners.blur_spinner(self)

    # Transformation: Blurring
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

    # Dropdown List for video FPS
    def fps_spinner(self):
        Spinners.fps_spinner(self)

    def open_camera(self):
        try:
            if not self.flag_cam:
                self.flag_cam = True
                self.image_capture = cv2.VideoCapture(0)
                self.play()
            else:
                self.flag_cam = False
                self.image_capture.release()

        except (Exception,):
            self.message_error("Erro ao abrir a câmera")

    def select_json(self):
        try:
            self.json_path = self.open_file('Selecione um JSON', False)

            json_display = ConfigurationRepository.json_read_display(self.json_path)
            self.ids.labeltesteimage.text = json_display

        except (Exception,):
            self.message_error("Selecione algum arquivo")

    def save_json(self):
        try:
            instance = ConfigurationRepository
            ConfigurationRepository.list_json_creat(instance, self.list_general)
            ConfigurationRepository.json_create(instance)
            self.list_aux.clear()

        except (Exception,):
            self.message_error('Para salvar algum JSON, realize algum processamento!')

    def save_frame(self, frame):
        try:
            self.save_flag = False
            time_string = time.strftime("%Y%m%d-%H%M%S")
            path_final = str(time_string) + '.jpg'

            cv2.imwrite(path_final, frame)

            print("Frame salvo!")

        except (Exception,):
            print('Aconteceu um erro ao Salvar o frame do video')

    def save_frame_flag(self):
        if self.save_flag is False:
            self.save_flag = True
        else:
            self.save_flag = False

    # Video playback
    # TODO: Modificar o tempo da clock com base no fps do vídeo
    def play(self):
        try:
            Clock.schedule_interval(self.update_video_1, 1 / 30)
            Clock.schedule_interval(self.update_video_2, 1 / 30)

        except (Exception,):
            self.message_error("Erro ao abrir a câmera")

    def detect_color_camera(self):
        if not self.flagDetect:
            self.flagDetect = True
        else:
            self.flagDetect = False

    def track_color_camera(self):
        if not self.flagRange:
            self.flagRange = True
        else:
            self.flagRange = False

    def update_video_1(self, *args):
        ret, frame = self.image_capture.read()
        if ret:
            self.update_image_video_1(frame)
            time_fps = self.image_capture.get(cv2.CAP_PROP_POS_FRAMES)
            self.now_frame = int(time_fps)

            if self.save_flag:
                self.save_frame(frame)

    # TODO: RESOLVER A QUESTÃO DO SALVAMENTO DO VÍDEO
    def update_video_2(self, *args):
        ret, frame = self.image_capture.read()
        instance = ConfigurationRepository
        if ret:

            if self.json_path is not None:
                ConfigurationRepository.set_config(instance, frame, json_path=self.json_path)
                out_image = ConfigurationRepository.execute(instance)
                self.list_aux = None

            elif self.list_aux is not None:
                ConfigurationRepository.set_config(instance, frame, list_operations=self.list_aux)
                out_image = ConfigurationRepository.execute(instance)
                self.json_path = None

            else:
                out_image = frame

            # if ret:
            #     frame = Treatment_Video.Video.treatment_cam(False, self.cameraColorSpace, self.cameraFPS, frame)
            #     if self.flagDetect == True:
            #         frame = Detector.detector(frame)
            #     if self.flagRange == True:
            #         frame = MyRangeDetector.main('RGB', frame)
            #     if self.cameraColorSpace == 'GRAY':
            #         frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
            #     if self.cameraColorSpace == 'CMYK':
            #         frame = Treatment_Video.Video.color_cmyk_2_rgb(frame)
            #     if self.cameraColorSpace == 'BGRA':
            #         frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            self.update_image_video_2(out_image)
            time_fps = self.image_capture.get(cv2.CAP_PROP_POS_FRAMES)
            self.now_frame2 = int(int(time_fps) * (self.image_capture.get(cv2.CAP_PROP_FPS)) / int(self.cameraFPS))

    def update_image_video_1(self, frame):
        buf = cv2.flip(frame, -1)
        image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), icolorfmt='bgr')
        image_texture.blit_buffer(buf.tobytes(), colorfmt='bgr')
        video = self.ids['camera1']
        video.texture = image_texture

    def update_image_video_2(self, frame):
        buf = cv2.flip(frame, - 1)
        image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), icolorfmt='bgr')
        image_texture.blit_buffer(buf.tobytes(), colorfmt='bgr')
        video = self.ids['camera2']
        video.texture = image_texture

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back_button)

    @staticmethod
    def back_button(key):
        if key == 27:
            App.get_running_app().root.current = 'home'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.back_button)
