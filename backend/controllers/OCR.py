import easyocr
import pytesseract
from backend.controllers.yolo_crop.Crop import Crop
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


class OCR:
    def __init__(self, frame):
        self.frame = frame

    def apply_easyocr(self):
        reader = easyocr.Reader(['pt', 'en'], gpu=False)

        out = reader.readtext(self.frame, detail=0, allowlist='1234567890')

        return out

    def apply_pytesseract(self):
        config_tittle = '--psm 1 --oem 1'

        out = pytesseract.image_to_string(self.frame, config=config_tittle)

        return out

    def apply_easyocr_yolo(self):
        reader = easyocr.Reader(['pt', 'en'], gpu=True)

        crop = Crop.get_cropped_frames(self.frame)

        tittle_img = crop[0]
        vote_img = crop[1]

        tittle = reader.readtext(tittle_img, detail=0)
        votes = reader.readtext(vote_img, detail=0)

        return tittle + votes

    def apply_pytesseract_yolo(self):
        crop = Crop.get_cropped_frames(self.frame)

        tittle_img = crop[0]
        vote_img = crop[1]

        config_tittle = '--psm 1 --oem 1 -c tessedit_char_whitelist=0123456789'
        config_votes = '--psm 4 --oem 1 -c tessedit_char_whitelist=BRANCO0123456789'

        tittle = pytesseract.image_to_string(tittle_img, config=config_tittle)
        votes = pytesseract.image_to_string(vote_img, config=config_votes)

        return tittle + votes
