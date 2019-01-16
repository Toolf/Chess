from ..base.figure import Color,Dot,Figure

def queen_movement(table,position,color):
    table_len = len(table)
    line_len = len(table[0])
    result = []
    #like Bishop#
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

    #like Rook#
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
    return result

def queen_attack(table,position,color):
    enemy_color = not color
    table_len = len(table)
    line_len = len(table[0])
    result = []
    #like Bishop#
    #right up
    for i in range(1,min(table_len - position.x,table_len - position.y)):
        if table[position.x+i][position.y+i] == enemy_color:
            result.append(Dot(position.x+i,position.y+i))
            break
        if table[position.x+i][position.y+i] == color:
            break
    #right down
    for i in range(1,min(table_len - position.x,position.y+1)):
        if table[position.x+i][position.y-i] == enemy_color:
            result.append(Dot(position.x+i,position.y-i))
            break
        if table[position.x+i][position.y-i] == color:
            break
    #left up
    for i in range(1,min(position.x+1,table_len - position.y)):
        if table[position.x-i][position.y+i] == enemy_color:
            result.append(Dot(position.x-i,position.y+i))
            break
        if table[position.x-i][position.y+i] == color:
            break
    #left down
    for i in range(1,min(position.x+1,position.y+1)):
        if table[position.x-i][position.y-i] == enemy_color:
            result.append(Dot(position.x-i,position.y-i))
            break
        if table[position.x-i][position.y-i] == color:
            break

    #like Rook
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
    return result

class Queen(Figure):

    def __init__(self, table):
        super().__init__(table)
        self.movement = queen_movement
        self.attack = queen_attack
