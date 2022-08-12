import json
import time

from backend.managers.BinarizationManager import BinarizationManager
from backend.managers.BlurManager import BlurManager
from backend.managers.EdgeManager import EdgeManager
from backend.managers.GeometricManager import GeometricManager
from backend.managers.MorphologyManager import MorphologyManager
from backend.managers.ColorSpaceManager import ColorSpaceManager
from backend.managers.ResizeManager import ResizeManager


class ConfigurationRepository:
    a = frame_out, list_operations, json_path,  = None, None, None
    b = process, arg, process_json, arg_json = [], [], [], []

    def get_config(self):
        pass

    def set_config(self, frame, list_operations=None, json_path=None):
        self.frame_out = frame
        self.list_operations = list_operations
        self.json_path = json_path

    @staticmethod
    def json_read_display(path):
        with open(path, 'r') as f:
            data = json.load(f)
            process = data['process']['type']
            arg = data['process']['arg']
            i = 0
            list_string = "Operações:\n"
        for _ in process:
            list_string = (list_string + process[i] + '(' + arg[i] + ')' + "\n")
            i = i + 1
        return list_string

    @staticmethod
    def treatment_end(msg, end):
        y = msg.find(end)
        out = msg[:y]
        return out

    @staticmethod
    def treatment_mid(msg, beginning, end):
        x = msg.find(beginning)
        y = msg.find(end)
        out = msg[x + 1:y]
        return out

    @staticmethod
    def treatment_beg(msg, beginning):
        x = msg.find(beginning)
        out = msg[x + 1:]
        return out

    @staticmethod
    def creat_list(msg):
        arg = []
        b = msg.count(",")
        i = 0
        while i <= b:
            x = msg.find(",")
            msg1 = msg[:x]
            msg = msg[x + 1:]

            if x == -1:
                arg.append(msg.strip())
            elif i == b:
                x = msg.find(",", -1)
                msg = msg[x:]
                arg.append(msg.strip())
            else:
                arg.append(msg1.strip())
            i = i + 1
        return arg

    def json_create(self):
        dic = {'path': 'caminho', 'process': {"type": self.process, "arg": self.arg}}

        timestr = time.strftime("(%Y%m%d-%H%M%S)")

        with open(timestr + 'Config.json', 'w') as json_file:
            json.dump(dic, json_file, indent=0, separators=(',', ': '))

    def list_json_creat(self, lista):
        self.process = []
        self.arg = []
        for n in range(len(lista)):
            processmid = self.treatment_end(lista[n], "(")
            arg = self.treatment_mid(lista[n], "(", ")")
            self.process.append(processmid)
            self.arg.append(arg)

    def execute(self):
        self.process = []
        self.arg = []
        if self.json_path is not None:
            with open(self.json_path, 'r') as f:
                data = json.load(f)
                process = data['process']['type']
                arg = data['process']['arg']
        else:
            ConfigurationRepository.list_json_creat(self, self.list_operations)
            process = self.process
            arg = self.arg

        i = 0

        for _ in process:

            arg_list = ConfigurationRepository.creat_list(arg[i])

            # Binarizações
            if process[i] == "THRESHOLD":
                self.frame_out = BinarizationManager.set_parameters(self, self.frame_out,
                                                                    process[i],
                                                                    threshold=int(arg_list[0]))
                self.frame_out = BinarizationManager.execute(self)

            elif process[i] == "OTSUTHRESHOLD":
                self.frame_out = BinarizationManager.set_parameters(self, self.frame_out,
                                                                    process[i],
                                                                    threshold=int(arg_list[0]))
                self.frame_out = BinarizationManager.execute(self)

            elif process[i] == "ADAPTIVETHRESHOLD":
                self.frame_out = BinarizationManager.set_parameters(self, self.frame_out,
                                                                    process[i],
                                                                    blocksize=int(arg_list[0]),
                                                                    c=int(arg_list[1]))
                self.frame_out = BinarizationManager.execute(self)

            elif process[i] == "ADAPTIVEGAUTHRESHOLD":
                self.frame_out = BinarizationManager.set_parameters(self, self.frame_out,
                                                                    process[i],
                                                                    blocksize=int(arg_list[0]),
                                                                    c=int(arg_list[1]))
                self.frame_out = BinarizationManager.execute(self)

            # Borramento
            elif process[i] == "BLUR":
                self.frame_out = BlurManager.set_parameters(self, self.frame_out, process[i],
                                                            c=int(arg_list[0]), d=int(arg_list[1]))
                self.frame_out = BlurManager.execute(self)

            elif process[i] == "GAUSSIANBLUR":
                self.frame_out = BlurManager.set_parameters(self, self.frame_out, process[i],
                                                            d=int(arg_list[0]))
                self.frame_out = BlurManager.execute(self)

            elif process[i] == "MEDIANBLUR":
                self.frame_out = BlurManager.set_parameters(self, self.frame_out, process[i],
                                                            ksize=int(arg_list[0]))
                self.frame_out = BlurManager.execute(self)

            elif process[i] == "BILATERAL":
                self.frame_out = BlurManager.set_parameters(self, self.frame_out, process[i], d=int(arg_list[0]),
                                                            sigma_color=int(arg_list[1]),
                                                            sigma_space=int(arg_list[2]))
                self.frame_out = BlurManager.execute(self)

            # Morfologia
            elif process[i] == "DILATE":
                self.frame_out = MorphologyManager.set_parameters(self, self.frame_out,
                                                                  process[i],
                                                                  c=int(arg_list[0]),
                                                                  d=int(arg_list[1]),
                                                                  iterations=int(arg_list[2]))
                self.frame_out = MorphologyManager.execute(self)

            elif process[i] == "ERODE":
                self.frame_out = MorphologyManager.set_parameters(self, self.frame_out,
                                                                  process[i],
                                                                  c=int(arg_list[0]),
                                                                  d=int(arg_list[1]),
                                                                  iterations=int(arg_list[2]))
                self.frame_out = MorphologyManager.execute(self)

            elif process[i] == "GRADIENT":
                self.frame_out = MorphologyManager.set_parameters(self, self.frame_out,
                                                                  morphology_type=process[i],
                                                                  c=int(arg_list[0]),
                                                                  d=int(arg_list[1]))
                self.frame_out = MorphologyManager.execute(self)

            elif process[i] == "OPEN":
                self.frame_out = MorphologyManager.set_parameters(self, self.frame_out,
                                                                  morphology_type=process[i],
                                                                  c=int(arg_list[0]),
                                                                  d=int(arg_list[1]))
                self.frame_out = MorphologyManager.execute(self)

            elif process[i] == "CLOSE":
                self.frame_out = MorphologyManager.set_parameters(self, self.frame_out,
                                                                  morphology_type=process[i],
                                                                  c=int(arg_list[0]),
                                                                  d=int(arg_list[1]))
                self.frame_out = MorphologyManager.execute(self)

            # Bordas
            elif process[i] == "SOBEL":
                self.frame_out = EdgeManager.set_parameters(self, self.frame_out, edge_type=process[i],
                                                            ksize=int(arg_list[0]))
                self.frame_out = EdgeManager.execute(self)

            elif process[i] == "CANNY":
                self.frame_out = EdgeManager.set_parameters(self, self.frame_out, edge_type=process[i],
                                                            threshold1=int(arg_list[0]), threshold2=int(arg_list[1]),
                                                            d=int(arg_list[2]))
                self.frame_out = EdgeManager.execute(self)

            elif process[i] == "LAPLACIAN":
                self.frame_out = EdgeManager.set_parameters(self, self.frame_out, process[i])
                self.frame_out = EdgeManager.execute(self)

            # Transformações
            elif process[i] == "GEOMETRICTRANSLATION":
                self.frame_out = GeometricManager.set_parameters(self, self.frame_out, process[i],
                                                                 int(arg_list[0]),
                                                                 int(arg_list[1]),
                                                                 int(arg_list[2]),
                                                                 int(arg_list[3]),
                                                                 int(arg_list[4]),
                                                                 int(arg_list[5]))
                self.frame_out = GeometricManager.execute(self)

            elif process[i] == "GEOMETRICROTATION":
                self.frame_out = GeometricManager.set_parameters(self, self.frame_out, process[i],
                                                                 int(arg_list[0]),
                                                                 int(arg_list[1]),
                                                                 int(arg_list[2]),
                                                                 int(arg_list[3]),
                                                                 int(arg_list[4]),
                                                                 int(arg_list[5]))
                self.frame_out = GeometricManager.execute(self)

            elif process[i] == 'GEOMETRICRECTIFY':
                self.frame_out = GeometricManager.set_parameters(self, self.frame_out,
                                                                 geometric_type=process[i])
                self.frame_out = GeometricManager.execute(self)

            # Espaço de cor
            elif process[i] == "COLORSPACE":
                self.frame_out = ColorSpaceManager.set_parameters(self, self.frame_out, arg_list[0])
                self.frame_out = ColorSpaceManager.execute(self)

            # Resize
            elif process[i] == "RESIZE":
                self.frame_out = ResizeManager.set_parameters(self, self.frame_out, arg_list[0])
                self.frame_out = ResizeManager.execute(self)

            i = i + 1

        return self.frame_out
