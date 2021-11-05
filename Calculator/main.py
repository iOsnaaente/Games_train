from PIL import Image # Importando o módulo Pillow para abrir a imagem no script

import pytesseract # Módulo para a utilização da tecnologia OCR

out = pytesseract.image_to_string( Image.open('l24sup.jpeg') )

print(out)
