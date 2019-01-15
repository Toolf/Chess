class Color:
    NONE  = -1
    BLACK = 0
    WHITE = 1

class Dot:
    __slots__ = ["x", "y"]

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def in_border(self,x_max:int,y_max:int):
        return 0 <= self.x < x_max and 0 <= self.y < y_max


    def __add__(self, other):
        if isinstance(other, Dot):
            return Dot(self.x + other.x, self.y + other.y)
        return False

    def __eq__(self, other):
        if isinstance(other, Dot):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x,self.y))

    def __str__(self):
        return f"({self.x},{self.y})"


class Figure:
    __slots__ = ["table", "movement", "attack"]

    def __init__(self, table):
        self.table = table

    def get_movements(self, position_x:int,position_y:int, table=None)->tuple:
        if table == None: table = self.table
        return self.movement(self.table, Dot(position_x,position_y), self.table[position_x][position_y])

    def get_attack(self,position_x, position_y, table=None)->tuple:
        if table == None: table = self.table
        return self.attack(table, Dot(position_x,position_y), table[position_x][position_y])
