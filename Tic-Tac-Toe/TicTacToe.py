import numpy as np 

JOGADOR_X =  1
JOGADOR_O = -1
JOGADOR_N =  0

BOARD = np.array( [ JOGADOR_N for _ in range(9) ], dtype = np.int8 )

def print_board( ):
    # PRINTA O TABULEIRO
    print( ' {%2.0f} | {%2.0f} | {%2.0f}  \t  1 | 2 | 3 '.format( BOARD[0], BOARD[1], BOARD[2] ) )
    print( ' {%2.0f} | {%2.0f} | {%2.0f}  \t  4 | 5 | 6 '.format( BOARD[3], BOARD[4], BOARD[5] ) )
    print( ' {%2.0f} | {%2.0f} | {%2.0f}  \t  7 | 8 | 9 '.format( BOARD[6], BOARD[7], BOARD[8] ) )


def check_end_game(): 
    # COLUNAS 
    for row in range(3):
        if abs(BOARD[row]+BOARD[row+3]+BOARD[row+6]) == 3:
            return True  
    # LINHAS
    for collum in range(3): 
        if abs( BOARD[collum*3] +  BOARD[collum*3 + 1] +  BOARD[collum*3 + 2] ) == 3: 
            return True 
    # DIAGONAIS
    if abs(BOARD[0] + BOARD[4] + BOARD[8]) == 3:  
        return True
    if abs(BOARD[6] + BOARD[4] + BOARD[2]) == 3:  
        return True
    # CASO O JOGO NÂO TENHA ENCERRADO AINDA
    return False


NUM_JOGADAS = 0
while NUM_JOGADAS < 9:
    if check_end_game():    break 
    print_board() 
    while True:
        try:
            JOGADA = int( input("\nDê entrada à posição a ser jogada: ") )
            if JOGADA == 99:   
                break
            if BOARD[ JOGADA -1 ] != JOGADOR_N:
                print('Jogada inválida.')
            else: 
                print('Jogou na posição {}'.format( JOGADA ) )
                BOARD[ JOGADA -1 ] = JOGADOR_X if NUM_JOGADAS %2 == 0 else JOGADOR_O  
                break
        except:
            print('Jogada inválida, tente novamente.')

    if JOGADA == 99:    
        break
    
    NUM_JOGADAS += 1

print( 'FIM DE JOGO')
    