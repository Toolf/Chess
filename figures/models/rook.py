from ..base.figure import Color,Dot,Figure

def rook_movement(table,position,color):
    table_len = len(table)
    line_len = len(table[0])
    result = []
    #up
    for x in range(position.x-1,-1,-1):
        if table[x][position.y] == Color.NONE:
            result.append(Dot(x,position.y))
        else:
            break
    #down
    for x in range(position.x+1,table_len):
        if table[x][position.y] == Color.NONE:
            result.append(Dot(x,position.y))
        else:
            break
    #left
    for y in range(position.y-1,-1,-1):
        if table[position.x][y] == Color.NONE:
            result.append(Dot(position.x,y))
        else:
            break
    #right
    for y in range(position.y+1,line_len):
        if table[position.x][y] == Color.NONE:
            result.append(Dot(position.x,y))
        else:
            break

    return tuple(result)

def rook_attack(table,position,color):
    enemy_color = not color
    table_len = len(table)
    line_len = len(table[0])
    result = []
    #up
    for x in range(position.x-1,-1,-1):
        if table[x][position.y] == enemy_color:
            result.append(Dot(x,position.y))
            break
        if table[x][position.y] == color:
            break
    #down
    for x in range(position.x+1,table_len):
        if table[x][position.y] == enemy_color:
            result.append(Dot(x,position.y))
            break
        if table[x][position.y] == color:
            break
    #left
    for y in range(position.y-1,-1,-1):
        if table[position.x][y] == enemy_color:
            result.append(Dot(position.x,y))
            break
        if table[position.x][y] == color:
            break
    #right
    for y in range(position.y+1,line_len):
        if table[position.x][y] == enemy_color:
            result.append(Dot(position.x,y))
            break
        if table[position.x][y] == color:
            break
    return tuple(result)

class Rook(Figure):

    def __init__(self, table):
        super().__init__(table)
        self.movement = rook_movement
        self.attack = rook_attack
