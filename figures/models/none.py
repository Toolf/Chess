from ..base.figure import Color,Dot,Figure

class FgNone(Figure):

    def __init__(self, table):
        super().__init__(table)
        self.movement = lambda *args: tuple()
        self.attack = lambda *args: tuple()
