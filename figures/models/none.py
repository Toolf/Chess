from ..base.figure import Color,Dot,Figure

class FgNone(Figure):

    def get_movements(self, position_x,position_y):
        return tuple()

    def get_attack(self,position_x,position_y):
        return tuple()
