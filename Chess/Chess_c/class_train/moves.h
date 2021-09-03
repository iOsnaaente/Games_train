#define EQUAL 0
#define OTHER 1
#define EMPTY 2

#define FALSE 0
#define TRUE  1

#define WHITE  1
#define BLACK -1

/// Calcula as posicoes validas para movimentar \return FALSE para invalido, TRUE para valido
char posicao_valida( struct piece **board, int signal, int x, int y ){
    int signal_aux = signal > 0 ? WHITE : BLACK ;
    if ( board[x][y].value * signal_aux > 0 )
        return EQUAL;
    else if ( board[x][y].value * signal_aux < 0  )
        return OTHER;
    else
        return EMPTY;
}


void move_piece ( struct piece **board_game, struct piece *piece_to_move, int x, int y ){
    struct piece aux;
    aux = board_game[x][y];
    board_game[x][y] = *piece_to_move;
    *piece_to_move = aux;
}


void move_pawn (struct piece **board, struct piece *pawn, int x_goal, int y_goal){
    struct piece aux;

    int x_pos = pawn->x_pos;
    int y_pos = pawn->y_pos;

    x_goal;
    x_pos;

    int signal = pawn->id[1] == 'b' ? WHITE : BLACK;

    /// Peao anda y++ ou y+2 e para matar x++ ou x--
    if ( y_goal == y_pos){

        if ( x_pos+signal == x_goal && posicao_valida(&board, signal, x_pos+signal, y_pos ) == EMPTY ) {
            move_piece(&board, &pawn, x_pos+signal, y_pos);

        }else if ( pawn->first_moviment == TRUE && x_pos+2*signal == x_goal){
            if (posicao_valida(&board, signal, x_pos+2*signal, y_pos ) == EMPTY && posicao_valida(&board, signal, x_pos+signal, y_pos ) == EMPTY ){
                pawn->first_moviment = FALSE;
                move_piece(&board, &pawn, x_pos+2*signal, y_pos);
            }
        }

    }else if( y_goal == y_pos+1){
        if ( x_pos+signal == x_goal && posicao_valida(&board, signal, x_pos+signal, y_pos+1 ) == OTHER ) {
            move_piece(&board, &pawn, x_pos+signal, y_pos+1);
        }

    }else if ( y_goal == y_pos-1 ){
        if ( x_pos+signal == x_goal && posicao_valida(&board, signal, x_pos+signal, y_pos-1 ) == OTHER ) {
            move_piece(&board, &pawn, x_pos+signal, y_pos-1);
        }
    }

}

