'''
    Movimentos em um cubo mágico 
    U  - gira a face de cima do cubo no sentido horário.
    D  - gira a face de baixo do cubo no sentido horário.
    L  - gira a face esquerda do cubo no sentido horário.
    R  - gira a face direita do cubo no sentido horário.
    F  - gira a face da frente do cubo no sentido horário.
    B  - gira a face de trás do cubo no sentido horário.
    U' - gira a face de cima do cubo no sentido antihorário.
    D' - gira a face de baixo do cubo no sentido antihorário.
    L' - gira a face esquerda do cubo no sentido antihorário.
    R' - gira a face direita do cubo no sentido antihorário.
    F' - gira a face da frente do cubo no sentido antihorário.
    B' - gira a face de trás do cubo no sentido antihorário.
    U2 - gira a face de cima do cubo 180 graus (dois movimentos 'U' consecutivos).
    D2 - gira a face de baixo do cubo 180 graus (dois movimentos 'D' consecutivos).
    L2 - gira a face esquerda do cubo 180 graus (dois movimentos 'L' consecutivos).
    R2 - gira a face direita do cubo 180 graus (dois movimentos 'R' consecutivos).
    F2 - gira a face da frente do cubo 180 graus (dois movimentos 'F' consecutivos).
    B2 - gira a face de trás do cubo 180 graus (dois movimentos 'B' consecutivos).
'''

import numpy as np
import random 

TOP     = 0 
LEFT    = 1
FRONT   = 2
RIGHT   = 3
BACK    = 4
DOWN    = 5

class Cube():
    moves           : list          = [ "U", "D", "L", "R", "F", "B", "U'", "D'", "L'", "R'", "F'", "B'", "U2", "D2", "L2", "R2", "F2", "B2" ]
    __cube          : np.ndarray 
    __is_complete   : bool          = bool( False )  
    __score         : int           = int ( 0 )
    __moves         : int           = int ( 0 )
    __seq           : list          = list( [] )

    ''' Construtor '''
    def __init__( self, randomize : bool = False):
        self.create_cube()
        if randomize:
            self.randomize() 
        self.__is_complete = False 
        self.__moves = 0
        self.__score = 0 

    ''' Retorna o numero de movimentos feitos '''
    def get_moviments( self ):
        return self.__moves 
    
    ''' Retorna a sequencia de movimentos '''
    def get_sequence( self ):
        return self.__seq 

    ''' Cria o cubo no instanciamento da classe ou quando for refeito '''
    def create_cube( self ) -> None:
        colors = ['T', 'L', 'F', 'R', 'B', 'D']
        self.__cube = np.array([[[colors[i]] * 3 for n in range(3)] for i in range(6)])

    ''' Aleatoriza o cubo mágico '''
    def randomize( self, num_moves : int = 20  ) -> None: 
        for _ in range( num_moves ):
            move_type = random.choice( self.moves )
            self.make_move( move_type )

    ''' Reinicia o cubo '''
    def restart( self ) -> None :
        self.create_cube( )
        self.randomize( )
        self.__is_complete = False 
        self.__moves = 0
        self.__score = 0 

    ''' Verifica se o cubo esta montado '''
    def is_completed(self) -> bool:
        for i in range(6):
            center = self.__cube[i][1][1]
            for j in range(3):
                for k in range(3):
                    if self.__cube[i][j][k] != center:
                        self.__is_complete = False
                        return self.__is_complete 
        self.__is_complete = True
        return self.__is_complete

    ''' Calcula o score do cubo de acordo com a quantidade de peças posicionadas corretamente'''
    def fitness(self) -> int:
        correct_positions = 0
        for face in self.__cube:
            center = face[1][1]
            for row in face:
                for piece in row:
                    if piece == center:
                        correct_positions += 1
        self.__score = round( ( correct_positions / 54 ) *100, 2 )
        return self.__score

    ''' Printa o cubo no terminal '''
    def show(self) -> None:
        # Face superior
        for i in range(3):
            print(" "*9, end = "")
            for j in range(3):
                print(self.__cube[0][i][j], end = " ")
            print()
        # Faces laterais
        for i in range(3):
            for j in range(4):
                print(" ", end = "" )
                for k in range(3):
                    print(self.__cube[j+1][i][k], end = " " )
                print(" ", end = "" )
            print()
        # Face inferior
        for i in range(3):
            print(" "*9, end = "")
            for j in range(3):
                print(self.__cube[5][i][j], end = " ")
            print()

    ''' Faz uma movimentação no cubo '''
    def make_move( self, move_type : str = '', recursive : bool = False ) -> None:
        # Verifica se é um movimento válido 
        if move_type in self.moves:
            # Salva as faces como eram originalmente 
            Ttemp = np.copy( self.__cube[ TOP   ] ) 
            Ltemp = np.copy( self.__cube[ LEFT  ] ) 
            Ftemp = np.copy( self.__cube[ FRONT ] ) 
            Rtemp = np.copy( self.__cube[ RIGHT ] ) 
            Btemp = np.copy( self.__cube[ BACK  ] ) 
            Dtemp = np.copy( self.__cube[ DOWN  ] ) 
            # Verifica se é um movimento UP
            if 'U' in move_type:
                # Movimento U sentido Horário 
                if move_type == 'U':
                    # Rotacionar a matriz superior no sentido horário 
                    self.__cube[ TOP ] = np.rot90( Ttemp, k = 1 )
                    # Deslocar as primeiras linhas das matrizes laterais 
                    self.__cube[ LEFT  ][0] = Ftemp[0] 
                    self.__cube[ FRONT ][0] = Rtemp[0] 
                    self.__cube[ RIGHT ][0] = Btemp[0] 
                    self.__cube[ BACK  ][0] = Ltemp[0] 
                # Movimento de 180º é equivalente a dois movimento de U 
                elif move_type == 'U2':
                    self.make_move('U', recursive = True )
                    self.make_move('U', recursive = True )
                # Movimento de U no sentido anti-horário equivalente a 3 movimentos de U 
                elif move_type == "U'":
                    for i in range(3):
                        self.make_move('U', recursive = True )

            # Verifica se é um movimento DOWN
            if 'D' in move_type:
                if move_type == 'D':
                    # Rotacionar a matriz superior no sentido horário 
                    self.__cube[ DOWN ] = np.rot90( Dtemp, k = 1 )
                    # Deslocar as primeiras linhas das matrizes laterais 
                    self.__cube[ LEFT  ][2] = Ftemp[2] 
                    self.__cube[ FRONT ][2] = Rtemp[2] 
                    self.__cube[ RIGHT ][2] = Btemp[2] 
                    self.__cube[ BACK  ][2] = Ltemp[2] 
                elif move_type == 'D2':
                    self.make_move('D', recursive = True )
                    self.make_move('D', recursive = True )
                elif move_type == "D'":
                    for i in range(3):
                        self.make_move('D', recursive = True )
            
            # Verifica se é um movimento FRONT
            if 'F' in move_type:
                if move_type == 'F':
                    self.__cube[ FRONT ]    = np.rot90( Ftemp, k = 1 )
                    self.__cube[ LEFT  ][0][2] = Dtemp[0][0]
                    self.__cube[ LEFT  ][1][2] = Dtemp[0][1]
                    self.__cube[ LEFT  ][2][2] = Dtemp[0][2]
                    self.__cube[ RIGHT ][0][0] = Ttemp[2][0]
                    self.__cube[ RIGHT ][1][0] = Ttemp[2][1]
                    self.__cube[ RIGHT ][2][0] = Ttemp[2][2] 
                    self.__cube[ TOP   ][2] = [ Ltemp[0][2], Ltemp[1][2], Ltemp[2][2] ] 
                    self.__cube[ DOWN  ][0] = [ Rtemp[0][0], Rtemp[1][0], Rtemp[2][0] ] 
                elif move_type == 'F2':
                    self.make_move('F', recursive = True )
                    self.make_move('F', recursive = True )
                elif move_type == "F'":
                    for i in range(3):
                        self.make_move('F', recursive = True )
            
            # Verifica se é um movimento BACK                       
            if 'B' in move_type:
                if move_type == 'B':
                    self.__cube[ BACK ]    = np.rot90( Btemp, k = -1 )
                    self.__cube[ LEFT  ][0][0] = Ttemp[0][2]
                    self.__cube[ LEFT  ][1][0] = Ttemp[0][1]
                    self.__cube[ LEFT  ][2][0] = Ttemp[0][0]
                    self.__cube[ RIGHT ][0][2] = Dtemp[2][2]
                    self.__cube[ RIGHT ][1][2] = Dtemp[2][1]
                    self.__cube[ RIGHT ][2][2] = Dtemp[2][0]
                    self.__cube[ TOP   ][0] = [ Rtemp[2][2], Rtemp[1][2], Rtemp[0][2] ]
                    self.__cube[ DOWN  ][2] = [ Ltemp[0][0], Ltemp[1][0], Ltemp[2][0] ]
                elif move_type == "B'":
                    for i in range(3):
                        self.make_move('B', recursive = True )
                elif move_type == 'B2':
                    self.make_move('B', recursive = True )
                    self.make_move('B', recursive = True )
            
            # Verifica se é um movimento LEFT
            if 'L' in move_type:
                if move_type == 'L':
                    self.__cube[ LEFT  ]         = np.rot90( Ltemp, k = -1 )
                    self.__cube[ FRONT ][ : , 0] = Ttemp[:, 0][::-1]
                    self.__cube[ DOWN  ][ : , 0] = Ftemp[:, 0]
                    self.__cube[ BACK  ][ : , 2] = Dtemp[:, 0][::-1]
                    self.__cube[ TOP   ][ : , 0] = Btemp[:, 2][::-1]
                elif move_type == 'L2':
                    self.make_move('L', recursive = True )
                    self.make_move('L', recursive = True )
                elif move_type == "L'":
                    for i in range(3):
                        self.make_move('L', recursive = True )

            # Verifica se é um movimento RIGHT
            if 'R' in move_type:
                if move_type == 'R':
                    self.__cube[ RIGHT ]         = np.rot90( Rtemp, k = 1 )
                    self.__cube[ FRONT ][ : , 2] = Dtemp[:, 2][::-1]
                    self.__cube[ DOWN  ][ : , 2] = Btemp[:, 0]
                    self.__cube[ BACK  ][ : , 0] = Ttemp[:, 2][::-1]
                    self.__cube[ TOP   ][ : , 2] = Ftemp[:, 2] 
                elif move_type == "R'":
                    for i in range(3):
                        self.make_move('R', recursive = True )
                elif move_type == 'R2':
                    self.make_move('R', recursive = True )
                    self.make_move('R', recursive = True )
            
            # Calcula a fitness, se esta completo e o número de movimento 
            if not recursive: 
                self.fitness()
                self.is_completed() 
                self.__moves += 1
                self.__seq.append( move_type )

if __name__ == '__main__':
    from cube import Cube 

    cube = Cube( randomize = True ) 
    
    while True: 
        moviment = input( 'Faça o movimento: ' )
        cube.make_move( moviment )
        cube.show() 
        
        num_mv = cube.get_moviments() 
        fitness = cube.fitness()
        print( 'Numero de movimentos:', num_mv, '\nFitness:', fitness  )
        if num_mv > 50:
            print( 'Numero máximo de movimentos atingidos')
            break 
