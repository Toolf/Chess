import unittest
from app.Chess import *
from figures.models.rook import *
from figures.models.queen import *
from figures.models.knight import *
from figures.models.king import *
from figures.models.bishop import *
from figures.models.pawn import *
from figures.models.none import *


def show(dots:set):
    print(''.join([str(dot) for dot in dots]))

class TestMoveMethod(unittest.TestCase):

    def test_pawn(self):
        table = [
            [Color.BLACK, Color.BLACK, Color.BLACK, Color.BLACK, Color.NONE],
            [Color.NONE,  Color.BLACK, Color.WHITE, Color.NONE,  Color.BLACK],
            [Color.NONE,  Color.NONE,  Color.NONE,  Color.WHITE, Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE,  Color.NONE,  Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE,  Color.WHITE, Color.NONE],
            [Color.NONE,  Color.WHITE, Color.BLACK, Color.NONE,  Color.WHITE],
            [Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.NONE],
        ]

        #Black
        color = Color.BLACK
        self.assertEqual(pawn_movement(table, Dot(0, 1),color), ())
        self.assertEqual(pawn_movement(table, Dot(0, 2),color), ())
        self.assertEqual(set(pawn_movement(table, Dot(0, 3),color)), {Dot(1,3)})
        self.assertEqual(set(pawn_movement(table, Dot(1, 4),color)), {Dot(2, 4),Dot(3, 4)})

        #WHITE
        color = Color.WHITE
        self.assertEqual(pawn_movement(table, Dot(6, 1),color), ())
        self.assertEqual(pawn_movement(table, Dot(6, 2),color), ())
        self.assertEqual(set(pawn_movement(table, Dot(6, 3),color)), {Dot(5,3)})
        self.assertEqual(set(pawn_movement(table, Dot(5, 4),color)), {Dot(4, 4),Dot(3, 4)})

    def test_king(self):
        table = [
            [Color.BLACK,Color.NONE, Color.NONE, Color.NONE, Color.NONE],
            [Color.NONE, Color.NONE, Color.BLACK,Color.NONE, Color.NONE],
            [Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.BLACK],
            [Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.WHITE],
            [Color.NONE, Color.NONE, Color.NONE, Color.NONE, Color.NONE],
            [Color.NONE, Color.NONE, Color.WHITE,Color.NONE, Color.NONE],
            [Color.WHITE,Color.NONE, Color.NONE, Color.NONE, Color.NONE],
        ]

        #Black
        color = Color.BLACK
        self.assertEqual(set(king_movement(table, Dot(0, 0),color)), {Dot(0, 1),Dot(1,0),Dot(1,1)})
        self.assertEqual(set(king_movement(table, Dot(1, 2),color)),
                         {Dot(0,1),Dot(0,2),Dot(0,3),Dot(1,1),Dot(1,3),Dot(2,1),Dot(2,2),Dot(2,3)})
        self.assertEqual(set(king_movement(table, Dot(2, 4),color)), {Dot(1, 3),Dot(1,4),Dot(2,3),Dot(3,3)})

        #White
        color = Color.WHITE
        self.assertEqual(set(king_movement(table, Dot(6, 0),color)), {Dot(5, 0),Dot(5,1),Dot(6,1)})
        self.assertEqual(set(king_movement(table, Dot(5, 2),color)),
                         {Dot(4,1),Dot(4,2),Dot(4,3),Dot(5,1),Dot(5,3),Dot(6,1),Dot(6,2),Dot(6,3)})
        self.assertEqual(set(king_movement(table, Dot(3, 4),color)), {Dot(2, 3),Dot(3,3),Dot(4,3),Dot(4,4)})

    def test_bishop(self):
        table = [
            [Color.BLACK, Color.NONE,  Color.NONE, Color.NONE,  Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE, Color.NONE,  Color.NONE],
            [Color.NONE,  Color.BLACK, Color.NONE, Color.NONE,  Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE, Color.NONE,  Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE, Color.WHITE, Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE, Color.NONE,  Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE, Color.NONE,  Color.WHITE],
        ]
        #Black
        color = Color.BLACK
        self.assertEqual(set(bishop_movement(table, Dot(0, 0),color)),
                         {Dot(1, 1),Dot(2,2),Dot(3,3),Dot(4,4)})
        self.assertEqual(set(bishop_movement(table, Dot(2, 1),color)),
                         {Dot(1,0),Dot(1,2),Dot(0,3),Dot(3,0),Dot(3,2)})

        #White
        color = Color.WHITE
        self.assertEqual(set(bishop_movement(table, Dot(6, 4),color)),
                         {Dot(5, 3),Dot(4,2),Dot(3,1),Dot(2,0)})
        self.assertEqual(set(bishop_movement(table, Dot(4, 3),color)),
                         {Dot(3,2),Dot(3,4),Dot(5,2),Dot(6,1),Dot(5,4)})

    def test_rook(self):
        table = [
            [Color.BLACK, Color.NONE,  Color.NONE, Color.NONE,  Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE, Color.NONE,  Color.NONE],
            [Color.NONE,  Color.BLACK, Color.NONE, Color.WHITE, Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE, Color.NONE,  Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE, Color.NONE,  Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE, Color.NONE,  Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE, Color.NONE,  Color.WHITE],
        ]
        #Black
        color = Color.BLACK
        self.assertEqual(set(rook_movement(table, Dot(0, 0),color)),
                         {Dot(1, 0),Dot(2,0),Dot(3,0),Dot(4,0),Dot(5,0),Dot(6,0),
                          Dot(0,1),Dot(0,2),Dot(0,3),Dot(0,4)})
        self.assertEqual(set(rook_movement(table, Dot(2, 1),color)),
                         {Dot(1,1),Dot(0,1),
                          Dot(2,0),
                          Dot(2,2),
                          Dot(3,1),Dot(4,1),Dot(5,1),Dot(6,1)})

        #White
        color = Color.WHITE
        self.assertEqual(set(rook_movement(table, Dot(6, 4),color)),
                         {Dot(6, 0),Dot(6,1),Dot(6,2),Dot(6,3),
                          Dot(5,4),Dot(4,4),Dot(3,4),Dot(2,4),Dot(1,4),Dot(0,4)})
        self.assertEqual(set(rook_movement(table, Dot(2, 3),color)),
                         {Dot(1,3),Dot(0,3),
                          Dot(2,2),
                          Dot(2,4),
                          Dot(3,3),Dot(4,3),Dot(5,3),Dot(6,3)})

    def test_queen(self):
        table = [
            [Color.BLACK, Color.NONE,  Color.NONE, Color.NONE,  Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE, Color.NONE,  Color.NONE],
            [Color.NONE,  Color.BLACK, Color.NONE, Color.WHITE, Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE, Color.NONE,  Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE, Color.NONE,  Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE, Color.NONE,  Color.NONE],
            [Color.NONE,  Color.NONE,  Color.NONE, Color.NONE,  Color.WHITE],
        ]
        #Black
        color = Color.BLACK
        self.assertEqual(set(queen_movement(table, Dot(0, 0),color)),
                         {Dot(1, 0),Dot(2,0),Dot(3,0),Dot(4,0),Dot(5,0),Dot(6,0),
                          Dot(0,1),Dot(0,2),Dot(0,3),Dot(0,4),
                          Dot(1,1),Dot(2,2),Dot(3,3),Dot(4,4)})
        self.assertEqual(set(queen_movement(table, Dot(2, 1),color)),
                         {Dot(1,1),Dot(0,1),
                          Dot(2,0),
                          Dot(2,2),
                          Dot(3,1),Dot(4,1),Dot(5,1),Dot(6,1),
                          Dot(1,0),Dot(1,2),Dot(0,3),Dot(3,0),Dot(3,2),Dot(4,3),Dot(5,4)})

        #White
        color = Color.WHITE
        self.assertEqual(set(queen_movement(table, Dot(6, 4),color)),
                         {Dot(6, 0),Dot(6,1),Dot(6,2),Dot(6,3),
                          Dot(5,4),Dot(4,4),Dot(3,4),Dot(2,4),Dot(1,4),Dot(0,4),
                          Dot(5,3),Dot(4,2),Dot(3,1),Dot(2,0)})
        self.assertEqual(set(queen_movement(table, Dot(2, 3),color)),
                         {Dot(1,3),Dot(0,3),
                          Dot(2,2),
                          Dot(2,4),
                          Dot(3,3),Dot(4,3),Dot(5,3),Dot(6,3),
                          Dot(1,2),Dot(0,1),Dot(1,4),Dot(3,2),Dot(4,1),Dot(5,0),Dot(3,4)})

class TestSomeMethods(unittest.TestCase):
    def test_finish(self):
        gm = Chess()
        gm.next_step(7,6,5,5)
        gm.next_step(1,1,2,1)
        gm.next_step(5,5,3,4)
        gm.next_step(1,7,2,7)
        gm.next_step(3,4,2,2)

        self.assertEqual(gm.finish(),False)
        gm = Chess()
        gm.next_step(6,4,4,4)
        gm.next_step(1,4,3,4)
        gm.next_step(7,3,3,7)
        gm.next_step(0,1,2,2)
        gm.next_step(7,5,4,2)
        gm.next_step(0,6,2,5)
        gm.next_step(3,7,1,5)

        self.assertEqual(gm.finish(),True)


if __name__ == '__main__':
    unittest.main()
