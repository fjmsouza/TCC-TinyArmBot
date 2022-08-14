import easyocr
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def apply_easyocr(frame):
    reader = easyocr.Reader(['pt', 'en'], gpu=False)

    out = reader.readtext(frame, detail=0, allowlist='1234567890')

    return out

def apply_pytesseract(frame):
    config_tittle = '--psm 1 --oem 1'

    out = pytesseract.image_to_string(frame, config=config_tittle)

    return out