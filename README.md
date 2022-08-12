# Ferramenta de Processamento de Imagem

Repositório com front-end e back-end da ferramenta de processamento de imagem.

## Bibliotecas Necessárias
- pip install opencv-python
- pip install pytorch
- pip install easyocr
- pip install tesseract
- pip install pytesseract
- pip install easygui
- pip install kivy
- pip install kivymd
- pip install matplotlib
- pip install gdown

### Observações: 
- Ao clonar o repositório rodar o arquivo resources_yolo
- Mudar os caminhos para o computador que for ser utilizado
- Configurar o pytesseract no computador usando o caminho: 'C:/Program Files/Tesseract-OCR/tesseract.exe' (Linux não precisa)

### Lista com os parâmetros default:
1. Borramento: 
- BLUR(5, 5),
- GAUSSIANBLUR(10)
- MEDIANBLUR(5),
- BILATERAL(7, 49, 49),
2. Morfologias: 
- DILATE(5, 5, 1)
- ERODE(5, 5, 1)
- GRADIENT(5, 5)
- OPEN(5, 5)
- CLOSE(5, 5)
3. Binarizações: 
- THRESHOLD(127)
- ADAPTIVETHRESHOLD(11, 2)
- ADAPTIVEGAUTHRESHOLD(11, 2)
- OTSUTHRESHOLD(127)
4. Bordas: 
- SOBEL(9), 
- CANNY(100, 200, 10)
- LAPLACIAN()
5. Transformação Geométrica: 
- GEOMETRICTRANSLATION(1, 0, 400, 0, 1, 250)
- GEOMETRICROTATION(1, 2, 1, 2, 250, 2)
- GEOMETRICRECTIFY()


