from backend.controllers.Filter import Filter
from backend.controllers.OCR import OCR


class OCRManager(Filter):
    var = ocr_out, frame, ocr_type = None, None, None

    def execute(self):
        if self.ocr_type == 'EASY':
            self.ocr_out = OCR(self.frame).apply_easyocr()
        elif self.ocr_type == 'TESS':
            self.ocr_out = OCR(self.frame).apply_pytesseract()
        elif self.ocr_type == 'EASYYOLO':
            self.ocr_out = OCR(self.frame).apply_easyocr_yolo()
        elif self.ocr_type == 'TESSYOLO':
            self.ocr_out = OCR(self.frame).apply_pytesseract_yolo()

        return self.ocr_out

    def set_parameters(self, frame, ocr_type):
        self.frame = frame
        self.ocr_type = ocr_type

    def get_parameters(self):
        pass
