from ..base.figure import Color,Dot,Figure

def knight_movement(table,position,color):
    table_len = len(table)
    line_len = len(table[0])
    result = []
    #up right
    move_position = (position + Dot(-1,2))
    if move_position.in_border(table_len,line_len) and table[move_position.x][move_position.y] == Color.NONE:
        result.append(move_position)
    move_position = (position + Dot(-2,1))
    if move_position.in_border(table_len,line_len) and table[move_position.x][move_position.y] == Color.NONE:
        result.append(move_position)

    #down right
    move_position = (position + Dot(1,2))
    if move_position.in_border(table_len,line_len) and table[move_position.x][move_position.y] == Color.NONE:
        result.append(move_position)
    move_position = (position + Dot(2,1))
    if move_position.in_border(table_len,line_len) and table[move_position.x][move_position.y] == Color.NONE:
        result.append(move_position)

    #up left
    move_position = (position + Dot(-1,-2))
    if move_position.in_border(table_len,line_len) and table[move_position.x][move_position.y] == Color.NONE:
        result.append(move_position)
    move_position = (position + Dot(-2,-1))
    if move_position.in_border(table_len,line_len) and table[move_position.x][move_position.y] == Color.NONE:
        result.append(move_position)

    #down left
    move_position = (position + Dot(1,-2))
    if move_position.in_border(table_len,line_len) and table[move_position.x][move_position.y] == Color.NONE:
        result.append(move_position)
    move_position = (position + Dot(2,-1))
    if move_position.in_border(table_len,line_len) and table[move_position.x][move_position.y] == Color.NONE:
        result.append(move_position)
    return tuple(result)

def knight_attack(table,position,color):
    enemy_color = not color
    table_len = len(table)
    line_len = len(table[0])
    result = []
    #up right
    move_position = (position + Dot(-1,2))
    if move_position.in_border(table_len,line_len) and table[move_position.x][move_position.y] == enemy_color:
        result.append(move_position)
    move_position = (position + Dot(-2,1))
    if move_position.in_border(table_len,line_len) and table[move_position.x][move_position.y] == enemy_color:
        result.append(move_position)

    #down right
    move_position = (position + Dot(1,2))
    if move_position.in_border(table_len,line_len) and table[move_position.x][move_position.y] == enemy_color:
        result.append(move_position)
    move_position = (position + Dot(2,1))
    if move_position.in_border(table_len,line_len) and table[move_position.x][move_position.y] == enemy_color:
        result.append(move_position)

    #up left
    move_position = (position + Dot(-1,-2))
    if move_position.in_border(table_len,line_len) and table[move_position.x][move_position.y] == enemy_color:
        result.append(move_position)
    move_position = (position + Dot(-2,-1))
    if move_position.in_border(table_len,line_len) and table[move_position.x][move_position.y] == enemy_color:
        result.append(move_position)

    #down left
    move_position = (position + Dot(1,-2))
    if move_position.in_border(table_len,line_len) and table[move_position.x][move_position.y] == enemy_color:
        result.append(move_position)
    move_position = (position + Dot(2,-1))
    if move_position.in_border(table_len,line_len) and table[move_position.x][move_position.y] == enemy_color:
        result.append(move_position)
    return tuple(result)

class Knight(Figure):

    def __init__(self, table):
        super().__init__(table)
        self.movement = knight_movement
        self.attack = knight_attack
