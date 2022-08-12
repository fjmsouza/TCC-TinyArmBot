import time

import cv2
import threading

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
from backend.managers.VisualizationManager import VisualizationManager
from backend.managers.OCRManager import OCRManager


class MyBoxLayoutVideo(Screen):
    a = colorSpace, FPS, resize, video_path, lst, video, frame = 'RGB', '30', '100', None, None, None, None
    b = fps, fpsimg, flagDetect, json_path, text_input, content, save_flag = None, None, False, None, None, None, False
    c = now_frame, now_frame2, image_index, image_index2, flag_play, list_aux = None, None, [], [], None, []
    d = cut_frame = None

    image_texture = ObjectProperty(None)
    image_capture = ObjectProperty(None)
    image_capture2 = ObjectProperty(None, allownone=True)

    @staticmethod
    def message_error(message):
        ButtonError.message_error(message)

    @staticmethod
    def open_file(message, multiple):
        file_open = OpenFiles.open_file(message, multiple)

        return file_open

    def select_video(self):
        try:
            # Chama a função para abrir arquivos
            self.video_path = self.open_file('Selecione um Vídeo', False)

            self.video = cv2.VideoCapture(self.video_path)

            # frames part
            self.image_capture = cv2.VideoCapture(self.video_path)

            if len(self.image_index) != 0:
                self.image_index = []
                self.image_index2 = []
                self.now_frame = 0
                self.now_frame2 = 0

            if self.image_capture2 is not None:
                self.image_capture2 = None

            self.slider_setting()

            cv2.destroyAllWindows()
        except (Exception,):
            self.message_error("Selecione algum arquivo")

    def select_json(self):
        try:
            self.json_path = self.open_file('Selecione um JSON', False)

            json_display = ConfigurationRepository.json_read_display(self.json_path)
            self.ids.labeltesteimage.text = json_display

        except (Exception,):
            self.message_error("Selecione algum arquivo")

    # Dropdownlist for video colorspace
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

    def process_spinner(self):
        Spinners.process_spinner_video(self)

    # Dropdownlist for visualization image
    def visualization_spinner(self):
        Spinners.visualization_spinner(self)

    # Dropdownlist for transformation video options
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

    # Transformation: ColorSpace
    def colorspace_spinner(self):
        Spinners.colorspace_spinner(self)

    # Dropdown List for video size
    def resize_spinner(self):
        Spinners.resize_spinner(self)

    # Dropdown List for video FPS
    def dropdown_fps_video(self):
        Spinners.fps_spinner(self)

    def apply_tesseract_ocr(self):
        try:
            instance = OCRManager
            OCRManager.set_parameters(instance, self.cut_frame, 'TESS')
            out_text = OCRManager.execute(instance)

            self.ids.labelsaidaocr.text = str(out_text)

        except (Exception,):
            self.message_error('Adicione alguma operação!')

    def apply_tesseract_ocr_th(self):
        threading.Thread(target=self.apply_tesseract_ocr).start()

    def process_video(self):
        try:
            # frames part
            self.image_capture = cv2.VideoCapture(self.video_path)

            self.image_capture.read()

            if len(self.image_index) != 0:
                self.image_index = []
                self.image_index2 = []
                self.now_frame = 0
                self.now_frame2 = 0

            self.slider_setting()

            cv2.destroyAllWindows()
        except (Exception,):
            if self.video_path is None:
                self.message_error("Selecione algum arquivo")
            else:
                self.message_error("Erro ao processar o video")

    def process_video_thr(self):
        thr = threading.Thread(target=self.process_video)
        thr.start()
        thr.join()

    def save_frame(self, frame):
        try:
            self.save_flag = False
            time_string = time.strftime("%Y%m%d-%H%M%S")
            path_final = str(time_string) + '.jpg'

            cv2.imwrite(path_final, frame)
            self.cut_frame = frame

            print("Frame salvo!")

        except (Exception,):
            print('Aconteceu um erro ao Salvar o frame do video')

    def save_frame_flag(self):
        if self.save_flag is False:
            self.save_flag = True
        else:
            self.save_flag = False

    def generate_histogram_video(self):
        try:
            self.frame = None
            instance = VisualizationManager
            VisualizationManager.set_parameters(instance, self.frame, 'HISTOGRAMVIDEO', self.video_path, 'RGB')
            VisualizationManager.execute(instance)

            new_video_path = 'Histogram.mp4'

            self.image_capture2 = cv2.VideoCapture(new_video_path)

            if len(self.image_index) != 0:
                self.image_index = []
                self.image_index2 = []
                self.now_frame = 0
                self.now_frame2 = 0

            self.slider_setting()

            cv2.destroyAllWindows()
        except (Exception,):
            if self.video_path is None:
                self.message_error("Selecione algum arquivo")
            else:
                self.message_error("Erro ao Gerar Histograma do video")

    def generate_histogram_video_th(self):
        threading.Thread(target=self.generate_histogram_video).start()

    def detect_color_video(self):
        self.flagDetect = True

    def track_color_video(self):
        # MyRangeDetector.main("RGB", self.video_path)
        pass

    def slider_setting(self):
        count = self.image_capture.get(cv2.CAP_PROP_FRAME_COUNT)
        self.ids["timeSlider"].max = count

        # Load the video once and save all the frames in an array
        while True:
            if self.image_capture2 is None:
                ret, frame = self.image_capture.read()
                video = self.ids['video2']
                video.texture = None

                if ret:
                    self.image_index.append(frame)

                else:
                    self.image_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    break
            else:
                ret, frame = self.image_capture.read()
                ret, frame2 = self.image_capture2.read()

                if ret:
                    self.image_index.append(frame)
                    self.image_index2.append(frame2)

                else:
                    self.image_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    self.image_capture2.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    break

    # Video playback
    def play(self):
        try:
            if not self.flag_play:
                self.image_capture.set(cv2.CAP_PROP_POS_FRAMES, self.now_frame)

                Clock.schedule_interval(self.update_video_1, 1 / self.image_capture.get(cv2.CAP_PROP_FPS))
                Clock.schedule_interval(self.update_video_2, 1 / self.image_capture.get(cv2.CAP_PROP_FPS))
                self.flag_play = True

            else:
                Clock.unschedule(self.update_video_1)
                Clock.unschedule(self.update_video_2)
                self.flag_play = False

            if self.ids.play.icon == 'pause':
                self.ids.play.icon = 'play'
            else:
                self.ids.play.icon = "pause"

        except (Exception,):
            if self.video_path is None:
                self.message_error("Selecione algum arquivo")
            else:
                self.message_error("Erro no botão play do video")

    def replay(self):
        try:
            self.now_frame = 0
            self.now_frame2 = 0

            if 0 == len(self.image_index2):
                if self.flag_play:
                    self.play()
                    # self.image_capture.set(cv2.CAP_PROP_POS_FRAMES, self.now_frame)
                    Clock.schedule_interval(self.update_video_1, 1 / self.image_capture.get(cv2.CAP_PROP_FPS))
                    self.play()
                else:
                    self.slider_update()
                    self.image_capture.set(cv2.CAP_PROP_POS_FRAMES, self.now_frame)
                    Clock.unschedule(self.update_video_1)
                    self.play()

            else:
                if self.flag_play:
                    self.play()
                    self.image_capture.set(cv2.CAP_PROP_POS_FRAMES, self.now_frame)
                    self.image_capture2.set(cv2.CAP_PROP_POS_FRAMES, self.now_frame2)

                    Clock.schedule_interval(self.update_video_1, 1 / self.image_capture.get(cv2.CAP_PROP_FPS))
                    Clock.schedule_interval(self.update_video_2, 1 / self.image_capture2.get(cv2.CAP_PROP_FPS))
                    self.play()

                else:
                    self.slider_update()
                    self.image_capture.set(cv2.CAP_PROP_POS_FRAMES, self.now_frame)
                    self.image_capture2.set(cv2.CAP_PROP_POS_FRAMES, self.now_frame2)

                    Clock.unschedule(self.update_video_1)
                    Clock.unschedule(self.update_video_2)
                    self.play()
        except (Exception,):
            print('Não é possível dar replay')

    # Video playback clock processing
    def update_video_1(self, *args):
        ret, frame = self.image_capture.read()
        # When the next frame can be read
        if ret:
            self.update_image_video_1(frame)
            time_fps = self.image_capture.get(cv2.CAP_PROP_POS_FRAMES)
            timems = self.image_capture.get(cv2.CAP_PROP_POS_MSEC)
            self.ids["timeSlider"].value = time_fps
            self.now_frame = int(timems)

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

            if self.save_flag:
                self.save_frame(out_image)

            self.update_image_video_2(out_image)
            time_fps = self.image_capture.get(cv2.CAP_PROP_POS_MSEC)
            self.now_frame2 = int(time_fps)

    def update_image_video_1(self, frame):
        # flip upside down
        buf = cv2.flip(frame, 0)
        image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        image_texture.blit_buffer(buf.tobytes(), colorfmt='bgr', bufferfmt='ubyte')
        video = self.ids['video']
        video.texture = image_texture

    def update_image_video_2(self, frame):
        # flip upside down
        buf = cv2.flip(frame, 0)
        image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        image_texture.blit_buffer(buf.tobytes(), colorfmt='bgr', bufferfmt='ubyte')
        video = self.ids['video2']
        video.texture = image_texture

    # Seek bar
    def sider_touch_move(self):
        # Clock.schedule_interval(self.slider_update, 0)
        self.slider_update()
        self.update_video_1()
        self.update_video_2()

    # Screen drawing process when the seek bar is moved
    def slider_update(self):
        if len(self.image_index2) == 0:
            # When the seek bar value and the playback frame value are different
            if self.now_frame != int(self.ids["timeSlider"].value):
                self.play()
                frame = self.image_index[int(self.ids["timeSlider"].value)]
                self.update_image_video_1(frame)
                self.now_frame = int(self.ids["timeSlider"].value)
                self.play()

        else:
            if self.fps == int(self.FPS):
                if self.now_frame != int(self.ids["timeSlider"].value):
                    self.play()
                    frame = self.image_index[int(self.ids["timeSlider"].value)]
                    frame2 = self.image_index2[int(self.ids["timeSlider"].value)]
                    self.update_image_video_1(frame)
                    self.update_image_video_2(frame2)
                    self.now_frame = int(self.ids["timeSlider"].value)
                    self.now_frame2 = int(self.ids["timeSlider"].value)
                    self.play()

            else:
                if self.now_frame != int(self.ids["timeSlider"].value):
                    self.play()
                    frame = self.image_index[self.now_frame - 1]
                    frame2 = self.image_index2[self.now_frame2 - 1]
                    self.update_image_video_1(frame)
                    self.update_image_video_2(frame2)
                    self.now_frame = int(self.ids["timeSlider"].value)
                    self.now_frame2 = int(self.ids["timeSlider"].value)
                    self.play()

    # Eventos do teclado
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back_button)

    # Quando apaertar ESC volta para a tela de menu
    @staticmethod
    def back_button(key):
        if key == 27:
            App.get_running_app().root.current = 'home'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.back_button)
