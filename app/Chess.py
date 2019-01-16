from figures.mainFigure import *
from figures.base.figure import Color

import pprint
import copy


class Chess:
    __slots__ = ["table", "black_team", "white_team", "size", "step", "figures"]

    def __init__(self):

        self.table = [
            [Color.BLACK, Color.BLACK, Color.BLACK, Color.BLACK, Color.BLACK, Color.BLACK, Color.BLACK, Color.BLACK],
            [Color.BLACK, Color.BLACK, Color.BLACK, Color.BLACK, Color.BLACK, Color.BLACK, Color.BLACK, Color.BLACK],
            [Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE],
            [Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE],
            [Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE],
            [Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE],
            [Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE],
            [Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE],
        ]
        self.size = 8
        self.step = Color.WHITE
        self.figures = {
            "rook": Fg_rook(self.table),
            "knight": Fg_knight(self.table),
            "bishop": Fg_bishop(self.table),
            "queen": Fg_queen(self.table),
            "king": Fg_king(self.table),
            "pawn": Fg_pawn(self.table)
        }
        self.black_team = [[0, 0, "rook"], [0, 7, "rook"],
                           [0, 1, "knight"], [0, 6, "knight"],
                           [0, 2, "bishop"], [0, 5, "bishop"],
                           [0, 3, "queen"], [0, 4, "king"],
                           [1, 0, "pawn"], [1, 1, "pawn"], [1, 2, "pawn"], [1, 3, "pawn"],
                           [1, 4, "pawn"], [1, 5, "pawn"], [1, 6, "pawn"], [1, 7, "pawn"]]
        self.white_team = [[7, 0, "rook"], [7, 7, "rook"],
                           [7, 1, "knight"], [7, 6, "knight"],
                           [7, 2, "bishop"], [7, 5, "bishop"],
                           [7, 3, "queen"], [7, 4, "king"],
                           [6, 0, "pawn"], [6, 1, "pawn"], [6, 2, "pawn"], [6, 3, "pawn"],
                           [6, 4, "pawn"], [6, 5, "pawn"], [6, 6, "pawn"], [6, 7, "pawn"]]



    def next_step(self, start_x:int, start_y:int, finish_x:int, finish_y:int) -> bool:
        if self.finish():
            return False
        el = self.get_element(start_x, start_y)
        el_type = self.get_element_type(start_x,start_y)
        if not el:
            return False
        #moves
        if self.step == self.get_color(start_x, start_y) \
                and any([dot.x == finish_x and dot.y == finish_y for dot in el_type.get_movements(start_x, start_y)]):
            el[0], el[1] = finish_x, finish_y
            self.table[finish_x][finish_y] = self.table[start_x][start_y]
            self.table[start_x][start_y] = Color.NONE
            self.step = not self.step
            return True
        #attack
        if self.step == self.get_color(start_x, start_y) \
            and any([dot.x == finish_x and dot.y == finish_y for dot in el_type.get_attack(start_x, start_y)]):
            for index in range(len(self.black_team)):
                enemy = self.black_team[index]
                if enemy[0] == finish_x and enemy[1] == finish_y:
                    del self.black_team[index]
                    break

            for index in range(len(self.white_team)):
                enemy = self.white_team[index]
                if enemy[0] == finish_x and enemy[1] == finish_y:
                    del self.white_team[index]
                    break
            el[0], el[1] = finish_x,finish_y
            self.table[finish_x][finish_y] = self.table[start_x][start_y]
            self.table[start_x][start_y] = Color.NONE
            self.step = not self.step
            return True

        return False

    def get_table(self):
        return copy.deepcopy(self.table)

    def get_element(self, x:int, y:int):
        for el in self.black_team:
            if el[0] == x and el[1] == y:
                return el
        for el in self.white_team:
            if el[0] == x and el[1] == y:
                return el
        return None

    def get_element_type(self, x:int, y:int):
        el = self.get_element(x, y)
        if not el:
            return None
        return self.figures[el[2]]

    def get_color(self, x: int, y: int):
        return self.table[x][y]

    def get_state(self):
        state = [[' '] * self.size for i in range(self.size)]
        chars = {
            "king_black": '♚',
            "queen_black": '♛',
            "rook_black": '♜',
            "bishop_black": '♝',
            "knight_black": '♞',
            "pawn_black": '♟',
            "king_white": '♔',
            "queen_white": '♕',
            "rook_white": '♖',
            "bishop_white": '♗',
            "knight_white": '♘',
            "pawn_white": '♙',

        }
        for el in self.black_team:
            state[el[0]][el[1]] = chars[el[2] + "_black"]

        for el in self.white_team:
            state[el[0]][el[1]] = chars[el[2] + "_white"]

        return state

    def step_to_the_king(self,x:int,y:int,table=None,enemy_team=None)->bool:
        if table == None:
            table = self.table
        if enemy_team == None:
            color = table[x][y]
            enemy_team = self.white_team if color == Color.BLACK else self.black_team
        for el in enemy_team:
            if any([dot.x == x and dot.y == y
                    for dot in self.get_element_type(el[0],el[1]).get_attack(el[0],el[1],table=table)]):
                return True
        return False

    def finish(self) -> bool:
        table = copy.deepcopy(self.table)#just in case
        enemy_color: int = int(Color.WHITE if self.step == Color.BLACK else Color.BLACK)
        team = self.black_team if self.step == Color.BLACK else self.white_team
        enemy_team = self.white_team if self.step == Color.BLACK else self.black_team
        king = [el for el in team if el[2] == "king"][0]
        if self.step_to_the_king(king[0],king[1],table):
            for el in team:
                el_type = self.get_element_type(el[0],el[1])
                can_move_to = set(el_type.get_movements(el[0],el[1])) | set(el_type.get_attack(el[0],el[1]))
                table[el[0]][el[1]] = Color.NONE
                tmp = None
                for position in can_move_to:
                    if table[position.x][position.y] == enemy_color:
                        for i in range(len(enemy_team)):
                            if enemy_team[i][0] == position.x and enemy_team[i][1] == position.y:
                                tmp = enemy_team[i]
                                del enemy_team[i]
                                break

                    table[position.x][position.y] = self.step
                    if not self.step_to_the_king(king[0] if el!=king else position.x,
                                                   king[1] if el!=king else position.y,
                                                   table,enemy_team):
                        if tmp:
                            enemy_team.append(tmp)
                        return False
                    if tmp:
                        enemy_team.append(tmp)
                        table[position.x][position.y] = enemy_color
                    else:
                        table[position.x][position.y] = Color.NONE

                    tmp = None

                table[el[0]][el[1]] = self.step
        else:
            return False
        return True

if __name__ == "__main__":
    """
    gm = Chess()
    while True:
        command = input("command:").split()
        if command[0] == "exit":
            break
        elif command[0] == "state":
            print('\n'.join([''.join(line) for line in gm.get_state()]))
        elif command[0] == "move":
            try:
                gm.next_step(int(command[1]),int(command[2]),int(command[3]),int(command[4]))
            except ValueError:
                print("value error")
            except IndexError:
                print("index err")
        elif command[0] == "color":
            try:
                print(gm.get_color(int(command[1]),int(command[2])))
            except:
                print("fuck u")
        elif command[0] == "finish":
            print(gm.finish())
    """
    gm = Chess()
    gm.next_step(6,4,4,4)
    gm.next_step(1,4,3,4)
    gm.next_step(7,3,3,7)
    gm.next_step(0,1,2,2)
    gm.next_step(7,5,4,2)
    gm.next_step(0,6,2,5)
    gm.next_step(3,7,1,5)
    print(gm.finish())
