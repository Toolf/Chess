import pygame
from Chess import Chess
import pprint

pygame.init()

display_width = 600
display_height = 600
MAP_SIZE = 8
part = (display_width/MAP_SIZE,display_height/MAP_SIZE)
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))
gameAPI = Chess()
image = {
    "♔" : pygame.image.load("image/king_white.png"),
    "♘": pygame.image.load("image/knight_white.png"),
    "♕": pygame.image.load("image/queen_white.png"),
    "♖": pygame.image.load("image/rook_white.png"),
    "♙": pygame.image.load("image/pawn_white.png"),
    "♗": pygame.image.load("image/bishop_white.png"),
    "♚" : pygame.image.load("image/king_black.png"),
    "♞": pygame.image.load("image/knight_black.png"),
    "♛": pygame.image.load("image/queen_black.png"),
    "♜": pygame.image.load("image/rook_black.png"),
    "♟": pygame.image.load("image/pawn_black.png"),
    "♝": pygame.image.load("image/bishop_black.png")
}


rect1 = pygame.Rect((0, 0, 30, 30))



def background(display:pygame.Surface):
    colors = (255,142,24),(183,96,8)
    for i in range(MAP_SIZE):
        for k in range(MAP_SIZE):
            pygame.draw.rect(display,colors[(i+k)%2],(part[0]*k,part[1]*i,part[0]*(k+1),part[1]*(i+1)))

def chess_render(table,display:pygame.Surface,focus_element = None):
    for i,line in enumerate(table):
        for k,el in enumerate(line):
            if el in "♔♕♖♗♘♙♚♛♜♝♞♟":
                if focus_element and focus_element[0] == i and focus_element[1] == k:
                    mouse = pygame.mouse.get_pos()
                    display.blit(image[el], (mouse[0]-20,mouse[1]-20))
                else:
                    display.blit(image[el],(part[0]*k+10,part[1]*i+10))



background(gameDisplay)
chess_render(gameAPI.get_state(),gameDisplay)

focus_element = []# real position, next position
move = False
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            focus_element = [int(mouse[1]//part[1]),int(mouse[0]//part[0])]
            move = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            next_step = [int(mouse[1]//part[1]),int(mouse[0]//part[0])]
            gameAPI.next_step(*focus_element,*next_step)
            focus_element = None
            move = False
            if gameAPI.finish():
                print("FINISH GAME")
            pprint.pprint(gameAPI.table)


    background(gameDisplay)
    chess_render(gameAPI.get_state(),gameDisplay,focus_element)
    pygame.display.update()



    clock.tick(30)
