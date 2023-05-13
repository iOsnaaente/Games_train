# importações automáticas 
from random import randint 
from time   import time


#   REGRAS 
#   A grelha do Sudoku é composta por 9x9 espaços.
def build_table( ) -> list:
    return [ 0 for i in range( 9*9 ) ]


#   Só podes usar números de 1 a 9.
def check_play( table : list ) -> bool:
    for i in range( 9*9 ):
        if type(table[i]) is not int: 
            return False 
    return True  


#   Cada bloco 3×3 pode apenas conter números de 1 a 9.
def check_square( t : list ) -> bool:
    for i in range( 3 ):
        for j in range( 3 ):       
            squared = t[ 0+(j*3 + 27*i) : 3+(j*3 + 27*i) ] + t[ 9+(j*3 + 27*i) : 12+(j*3 + 27*i)] + t[ 18+(j*3 + 27*i) : 21+(j*3 + 27*i) ]  
            test = []
            for values in squared:
                if values == 0:             continue 
                elif values not in test:    test.append( values )
                else:                       return False 
    return True 


#   Cada linha horizontal pode apenas conter números de 1 a 9.
def check_row( t : list  ) -> bool :
    for i in range( 9 ):
        row = t[ 0+(i*9) : 9+(i*9) ]
        test = [] 
        for values in row:
            if values == 0:             continue 
            elif values not in test:    test.append( values )
            else:                       return False 
    return True 


#   Cada coluna vertical pode apenas conter números de 1 a 9.
def check_collum( t : list ) -> bool:
    for i in range( 9 ):
        coll = t[ i : : 9 ]
        test = [] 
        for values in coll: 
            if values == 0:         continue
            if values not in test:  test.append( values )
            else:                   return False 
    return True 

# Avaliar o jogo 
def check_game( table : list ) -> bool :
    if check_square( table ):
        if check_row( table ):
            if check_collum( table ):
                return True
    return False 


#   O jogo termina quando toda a grelha do Sudoku estiver preenchida corretamente com números
def check_end_game( table : list ) -> bool:
    for i in table: 
        if i == 0: 
            return False 
    return True 


# Usado para printar a tabela toda vez que for feita uma nova jogada
def print_table( table : list ) -> None:
    for i in range(9):
        if i == 3 or i == 6:
            print( '------  '*3 )
        for j in range(9):
            if j ==3 or j == 6:
                print( '| ', end = '')
            if table[i*9 + j ] == 0:
                print( '_ ', end = '')
            else:
                print( str(table[ i*9 + j ]) + ' ', end = '')

        print( '\n ')

# Printa somente a tabela sem formatação 
def print_root_table( table : list ) -> None:
    print( table ) 


# MACRO CONFIGURAÇÕES 
TIME_BEGIN = 0 
SCORE = 0 


# Iniciar o jogo 
def init_game( level : int = 50) -> list : 
    table = build_table()
    for i in range( level ): 
        wrong_position = True
        while wrong_position == True:
            number = randint( 1, 9 ) 
            position = randint( 0, len(table)-1 )
            if table[position] == 0: 
                table[position] = number
                if check_game( table ): wrong_position = False 
                else:                   table[ position ] = 0
    TIME_BEGIN = time() 
    return table 

# Dar pontuação 
def compute_score():
    SCORE = (time() - TIME_BEGIN)*0.001 