#define FALSE 0
#define TRUE 1

struct piece {
    char *name;
    char id[2];
    int value;
    int x_movement;
    int y_movement;
    int x_pos;
    int y_pos;
    char first_moviment;
};


struct piece creat_pawn( int x, int y, char id ){
    struct piece pawn;
    pawn.name = "PAWN";
    pawn.id[0] = 'p';
    pawn.id[1] = id;
    pawn.value = 1;
    pawn.x_movement = TRUE;
    pawn.y_movement = FALSE;
    pawn.x_pos = x;
    pawn.y_pos = y;
    pawn.first_moviment = TRUE;
    return  pawn;
}

struct piece creat_rock( int x, int y, char id ){
    struct piece rock;
    rock.name = "ROCK";
    rock.id[0] = 't';
    rock.id[1] = id;
    rock.value = 5;
    rock.x_movement = TRUE;
    rock.y_movement = FALSE;
    rock.x_pos = x;
    rock.y_pos = y;
    rock.first_moviment = TRUE;
    return rock;
}

struct piece creat_knight( int x, int y, char id){
    struct piece knight;
    knight.name = "KNIGHT";
    knight.id[0] = 'c';
    knight.id[1] = id;
    knight.value = 3;
    knight.x_movement = TRUE;
    knight.y_movement = TRUE;
    knight.x_pos = x;
    knight.y_pos = y;
    knight.first_moviment = TRUE;
    return knight;
}

struct piece creat_bishop(  int x, int y, char id){
    struct piece bishop;
    bishop.name = "BISHOP";
    bishop.id[0] = 'b';
    bishop.id[1] = id;
    bishop.value = 3;
    bishop.x_movement = TRUE;
    bishop.y_movement = TRUE;
    bishop.x_pos = x;
    bishop.y_pos = y;
    bishop.first_moviment = TRUE;
    return bishop;
}

struct piece creat_queen( int x, int y, char id){
    struct piece queen;
    queen.name = "QUEEN";
    queen.id[0] = 'd';
    queen.id[1] = id;
    queen.value = 9;
    queen.x_movement = TRUE;
    queen.y_movement = FALSE;
    queen.x_pos = x;
    queen.y_pos = y;
    queen.first_moviment = TRUE;
    return queen;
}

struct piece creat_king( int x, int y, char id){
    struct piece king;
    king.name = "KING";
    king.id[0] = 'r';
    king.id[1] = id;
    king.value = 100;
    king.x_movement = TRUE;
    king.y_movement = FALSE;
    king.x_pos = x;
    king.y_pos = y;
    king.first_moviment = TRUE;
    return king;
}

struct piece creat_empty_piece( int x, int y, char id){
    struct piece empty_piece;
    empty_piece.name = "EMPTY";
    empty_piece.id[0] = 'e';
    empty_piece.id[1] = id;
    empty_piece.value = 0;
    empty_piece.x_movement = FALSE;
    empty_piece.y_movement = FALSE;
    empty_piece.x_pos = x;
    empty_piece.y_pos = y;
    empty_piece.first_moviment = FALSE;
    return empty_piece;
}

void creat_pieces( struct piece *color_pieces, char id, int color ){
    int pawn_pos, real_pos;
    int i = 0;

    if (color == TRUE){
        pawn_pos = 1;
        real_pos = 0;
    }else if (color == FALSE){
        pawn_pos = 6;
        real_pos = 7;
    }

    for ( i=0; i<8; i++)
        color_pieces[i] = creat_pawn(pawn_pos, i, id);

    color_pieces[i++] = creat_rock  ( real_pos, 0, id );
    color_pieces[i++] = creat_knight( real_pos, 1, id );
    color_pieces[i++] = creat_bishop( real_pos, 2, id );
    color_pieces[i++] = creat_king  ( real_pos, 3, id );
    color_pieces[i++] = creat_queen ( real_pos, 4, id );
    color_pieces[i++] = creat_bishop( real_pos, 5, id );
    color_pieces[i++] = creat_knight( real_pos, 6, id );
    color_pieces[i++] = creat_rock  ( real_pos, 7, id );

}

