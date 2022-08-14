from easygui import fileopenbox
from backend.managers.ConfigurationRepository import ConfigurationRepository
from backend.managers.OCRManager import OCRManager
from backend.controllers.Metrics import Metrics
from backend.controllers.Organize import Organize
import cv2
import os
cwd = os.getcwd()


def open_file(message, multiple):
    list_files = []

    path_open = fileopenbox(title=message, multiple=multiple)

    if multiple:
        for n in range(len(path_open)):
            list_files.append(path_open[n])

        return list_files

    else:
        return path_open


def clean_archive():
    archive_output = open(cwd + '/backend/OUTPUT_TREATMENT_EASY_OCR.txt', 'w')
    archive_output.write('')
    archive_output.close()


# Início do código Principal
multiple_files = open_file('Selecione um arquivo', False)

instance = ConfigurationRepository
ocr = OCRManager

json_teste = open_file('Selecione o json', False)

list_processed_images = []

frame = cv2.imread(multiple_files)
ConfigurationRepository.set_config(instance, frame, json_path=json_teste)
out_image = ConfigurationRepository.execute(instance)

