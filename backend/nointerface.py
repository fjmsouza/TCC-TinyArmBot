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
multiple_files = open_file('Selecione os arquivos', True)

instance = ConfigurationRepository
ocr = OCRManager

json_teste = open_file('Selecione o json', False)
# list_teste = ['BLUR(5, 5)', 'CLOSE(5, 5)', 'THRESHOLD(127)', 'SOBEL(9)']

list_processed_images = []

for i in range(len(multiple_files)):
    frame = cv2.imread(multiple_files[i])

    ConfigurationRepository.set_config(instance, frame, json_path=json_teste)
    # ConfigurationRepository.set_config(instancia, frame, list_operations=list_teste)
    out_image = ConfigurationRepository.execute(instance)

    list_processed_images.append(out_image)

# Limpar aquivo de saída do OCR
clean_archive()

# Colocar a chamada da função de aplicar OCRs
for i in range(len(list_processed_images)):
    OCRManager.set_parameters(ocr, list_processed_images[i], 'EASYYOLO')

    out_text = OCRManager.execute(ocr)
    out_text = Organize.Organize(out_text)

    output_archive = open(cwd + '/backend/OUTPUT_TREATMENT_EASY_OCR.txt', 'a+')
    print(out_text)

    if i == len(list_processed_images) - 1:
        output_archive.write(str(out_text))
    else:
        output_archive.write(str(out_text) + "\n")

    output_archive.close()

print(Metrics.Metrics(cwd + '/backend/OUTPUT_TREATMENT_REFERENCE.txt', cwd + '/backend/OUTPUT_TREATMENT_EASY_OCR.txt'))
