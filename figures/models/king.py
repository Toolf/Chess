from ..base.figure import Color,Dot,Figure

def king_movement(table, position, color):
    table_len = len(table)
    line_len = len(table[0])
    return tuple(position + Dot(x, y)
                 for x in range(-1, 2) for y in range(-1, 2)
                 if (position + Dot(x, y)).in_border(table_len, line_len) and table[position.x + x][
                     position.y + y] == Color.NONE)


def king_attack(table, position, color):
    enemy_color = not color
    table_len = len(table)
    line_len = len(table[0])
    return tuple(position + Dot(x, y)
                 for x in range(-1, 2) for y in range(-1, 2)
                 if (position + Dot(x, y)).in_border(table_len, line_len)
                 and table[position.x + x][position.y + y] == enemy_color)


class King(Figure):

    def __init__(self, table):
        super().__init__(table)
        self.movement = king_movement
        self.attack = king_attack
