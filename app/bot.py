from Chess import *
import copy
import figures.mainFigure

import time

class ChessBot:
    mass = {
        "king": 100,
        "queen": 9,
        "rook": 5,
        "bishop": 7,
        "knight": 6,
        "pawn": 3,
    }

    def best_step(self,game,team,enemy_team,step=1,max_depth=3):
        """
        :argument step is 1 when move bot else 0
        """
        if max_depth == 1:

            char_to_names = {val:key for key,val in game.chars.items()}
            sum = 0
            table = game.get_table()
            #print('\n'.join([''.join(line) for line in game.get_state()]))
            for i,line in enumerate(game.get_state()):
                for k,el in enumerate(line):
                    if el in char_to_names:
                        sum += self.mass[char_to_names[el].split('_')[0]]*(1 if any([fg[0]==i and fg[1]==k for fg in team]) else -1)
            return sum,[]
        next_step_val = []
        step_team = team if step else enemy_team

        for el in step_team:
            el_type = game.get_element_type(el[0],el[1])
            can_move_to = set(el_type.get_movements(el[0],el[1])) | set(el_type.get_attack(el[0],el[1]))
            last_state = copy.copy(el)

            for position in can_move_to:
                el[0],el[1] = position.x,position.y
                next_step_val.append((self.best_step(game,team,enemy_team,int(not step),max_depth-1)[0],last_state,position))
            el[0],el[1] = last_state[0],last_state[1]
        if step:
            best = tuple([float("-inf"),])
            for el in next_step_val:
                if el[0] > best[0]:
                    best = el
        else:
            best = ([float("inf"),])
            for el in next_step_val:
                if el[0] < best[0]:
                    best = el
        #print(best)
        return best

if __name__ == "__main__":
    print("in bot")
