#include <stdio.h>
#include <stdlib.h>

#include "pieces.h"
#include "moves.h"

#define WHITE  1
#define BLACK -1

struct piece board[8][8];

struct piece white[16];
struct piece black[16];

int main(){

    creat_pieces( &white, 'b', TRUE  );
    creat_pieces( &black, 'p', FALSE );

    int l, c;
    for (l=0; l<8; l++)
        for (c=0; c<8; c++)
            board[l][c] = creat_empty_piece(l, c, 'p');

    int p;
    for (p=0; p<16; p++)
        for (l=0; l<8; l++)
            for (c=0; c<8; c++)
                if( white[p].x_pos == l && white[p].y_pos == c)
                    board[l][c] = white[p];
                else if (black[p].x_pos == l && black[p].y_pos == c)
                    board[l][c] = black[p];

    for (l=0; l<8; l++){
        printf("[%i] ", l+1);
        for (c=0; c<8; c++)
            printf("[%c%c]", board[l][c].id[0],board[l][c].id[1]);
        printf("\n");
    }


    return 0;

}
