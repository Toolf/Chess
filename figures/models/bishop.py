from ..base.figure import Color,Dot,Figure

def bishop_movement(table,position,color):
    table_len = len(table)
    line_len = len(table[0])
    result = []
    #right up
    for i in range(1,min(table_len - position.x,line_len - position.y)):
        if table[position.x+i][position.y+i] == Color.NONE:
            result.append(Dot(position.x+i,position.y+i))
        else:
            break
    #right down
    for i in range(1,min(table_len - position.x,position.y+1)):
        if table[position.x+i][position.y-i] == Color.NONE:
            result.append(Dot(position.x+i,position.y-i))
        else:
            break
    #left up
    for i in range(1,min(position.x+1,line_len - position.y)):
        if table[position.x-i][position.y+i] == Color.NONE:
            result.append(Dot(position.x-i,position.y+i))
        else:
            break
    #left down
    for i in range(1,min(position.x+1,position.y+1)):
        if table[position.x-i][position.y-i] == Color.NONE:
            result.append(Dot(position.x-i,position.y-i))
        else:
            break
    return tuple(result)

def bishop_attack(table,position,color):
    enemy_color = not color
    table_len = len(table)
    result = []
    #right up
    for i in range(1,min(table_len - position.x,table_len - position.y)):
        if table[position.x+i][position.y+i] == enemy_color:
            result.append(Dot(position.x+i,position.y+i))
            break
    #right down
    for i in range(1,min(table_len - position.x,position.y+1)):
        if table[position.x+i][position.y-i] == enemy_color:
            result.append(Dot(position.x+i,position.y-i))
            break
    #left up
    for i in range(1,min(position.x+1,table_len - position.y)):
        if table[position.x-i][position.y+i] == enemy_color:
            result.append(Dot(position.x-i,position.y+i))
            break
    #left down
    for i in range(1,min(position.x+1,position.y+1)):
        if table[position.x-i][position.y-i] == enemy_color:
            result.append(Dot(position.x-i,position.y-i))
            break
    return tuple(result)


class Bishop(Figure):

    def __init__(self, table):
        super().__init__(table)
        self.movement = bishop_movement
        self.attack = bishop_attack
