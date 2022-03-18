from   PIL      import Image 
import numpy    as np
import glob 
import cv2
import os

from brigthness import * 

# CAMINHO ABSOLUTO DO FILE main.py 
PATH = os.path.dirname( __file__ )

# PARA ABRIR TODAS AS IMAGENS DO TIPO PNG 
BATH = glob.glob( PATH + "\\img\\*.png" ) 

# PARA ABRIR A IMAGEM 
for file_path in BATH: 
    with Image.open( file_path, mode = 'r' ) as img: 
        
        # CONVERTER PARA O MODO ESCALA DE CINZA (UNIT8)
        img = img.convert( mode = 'L' )

        # PEGO AS DIMENSÕES DAS IMAGEM 
        w, h = img.size 

        # CONVERTER DIMENSÃO 
        if w > h:   img = img.resize( size = (250, 200) )  
        else:       img = img.resize( size = (200, 250) )      
        w, h = img.size 

        # CARACTER_WIDTH, CARACTER_HEIGTH 
        c_w, c_h    = length_text 

        # CRIAÇÃO DE UMA IMAGEM VAZIA 
        new_img = np.zeros( (h*c_h, w*c_w, 1), dtype = np.uint8 )
        
        # CRIA OS NOMES DAS IMAGENS 
        NAME = file_path.removeprefix( PATH + '\\img' ) 
        NAME = NAME.removesuffix( '.png' ) 

        # COLOCA OS CARACTERES NAS POSIÇÕES CORRETAS 
        with open( PATH + '\\text\\' + NAME + '.txt', 'w' ) as file:
            file.seek(0) 
            for width in range( w ): 
                for height in range( h ):
                    pixel  = img.getpixel( (width, height) )
                    pixel /= 255  
                    text = get_better_pixel( pixel )
                    file.write( text )
                    cv2.putText( img = new_img, text = text, org = ( c_w*width, c_h*height ), fontFace = font, fontScale = scale_, color = 255, thickness = thickness )
                file.write( '\n' )
        
        # SALVA AS IMAGENS GERADAS 
        cv2.imwrite( PATH + '\\out' + NAME + '.png', new_img )
    