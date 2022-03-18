import numpy as np 
import random
import cv2 

# CRIAÇÃO DO DICIONÁRIO DE CARACTERES 
text        = chr( random.randint( 24, 129 ) )
font        = cv2.FONT_HERSHEY_COMPLEX
scale_      = 1 
thickness   = 1
length_text = cv2.getTextSize( text = text, fontFace = font, fontScale = scale_, thickness = thickness )[0]
size = ( length_text[0], length_text[1], 1 )
DICT = { }
for char in range( 32, 127 ):    
    img  = np.zeros( size, dtype = np.uint8 )
    cv2.putText( img, chr( char ), (0, size[1]), font, scale_, color = 255, thickness = thickness )
    bright = 0 
    for i in range( size[0] ):
        for j in range( size[1] ): 
            if img[i][j] == 255: 
                bright += 1
    num_pixels = size[ 0 ] * size[ 1 ]
    DICT.update( { chr(char) : bright / num_pixels } )

# NORMALIZAR DICIONÁRIO 
MAX_VALUE = DICT[ (max( DICT, key = lambda key: DICT[ key ] ) ) ]
MIN_VALUE = DICT[ (min( DICT, key = lambda key: DICT[ key ] ) ) ]
NORM_FUNC = lambda value : ( value - MIN_VALUE ) / ( MAX_VALUE - MIN_VALUE )
for key in DICT.keys():
    DICT[ key ] = NORM_FUNC( DICT [ key ] )

# ORDENAÇÃO DO DICIONÁRIO 
NEW_DICT = {} 
for i in sorted( DICT, key = DICT.get ):
    NEW_DICT.update( { i : DICT[i] } )

def get_better_pixel( pixel : float ):
    for key in NEW_DICT.keys():
        if pixel > NEW_DICT[ key ]:
            continue 
        else: 
            return key 
