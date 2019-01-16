from ..base.figure import Color,Dot,Figure

def pawn_movement(table,position,color):
    table_len = len(table)
    if color == Color.BLACK:
        if position.x == 1 \
                and table[position.x+1][position.y] == Color.NONE \
                and table[position.x+2][position.y] == Color.NONE:
            return position + Dot(1, 0),position + Dot(2,0)
        if table[position.x+1][position.y] == Color.NONE:
            return position + Dot(1, 0),
    if color == Color.WHITE:
        if position.x == table_len-2 \
                and table[position.x-1][position.y] == Color.NONE \
                and table[position.x-2][position.y] == Color.NONE:
            return position + Dot(-1,0), position + Dot(-2,0)
        if table[position.x-1][position.y] == Color.NONE:
            return position + Dot(-1,0),
    return ()

def pawn_attack(table,position,color):
    table_len = len(table)
    line_len = len(table[0])
    if color == Color.BLACK:
        return tuple(position + Dot(1,y)
                     for y in (-1,1)
                     if (position+Dot(1,y)).in_border(table_len,line_len)
                     and table[position.x+1][position.y + y] == Color.WHITE)
    if color == Color.WHITE:
        return tuple(position + Dot(-1,y)
                     for y in (-1,1)
                     if (position+Dot(-1,y)).in_border(table_len,line_len)
                     and table[position.x-1][position.y + y] == Color.BLACK)
    return ()


class Pawn(Figure):

    def __init__(self, table):
        super().__init__(table)
        self.movement = pawn_movement
        self.attack = pawn_attack
