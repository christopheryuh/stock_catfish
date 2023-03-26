import numpy as np 
import pygame
import chess 

WHITE = (255,255,255)
BLACK = (0,0,0)

class Square:

# WHIDTH and HEIGHT must be WHIDTH and HEIGHT of the Squar Not the Board

#defigning the dimentions and posistion of each of the squares that make up the board
    def __init__(self, x, y, width, height):
        self.x = x 
        self.y = y 
        self.width = width
        self.height = height
        self.abs_x = x * width
        self.abs_y = y * height
        self.abs_pos  = (self.abs_pos, self.abs_y)
        self.pos = (x,y)
        self.color = 'white' if (x + y) % 2 == 0 else 'black'
        self.draw_color = (WHITE) if self.color == 'white' else (BLACK)
        self.highlight_color = (220, 208, 194) if self.color == 'white' else (0.228,10)
        self.occupying_piece  = None 
        self.coord  = self.get_coord()
        self. rect = pygame.Rect(
            self .abs_x, 
            self.abs_y, 
            self.width, 
            self.height
        )
        
    def get_coord(self):
        columns = 'abcdefgh'
        
        return columns[self.x] + str(self.y + 1)

def draw(self, display):

    if self.highlight:
        pygame.draw.rect(display, self.draw_color, self.highlight_color, self.rect)
    
    else:
        pygame.draw.rect(display, self.draw_color, self.rect)

    if self.occupying_peice != None:
        centering_rect = self.occupying_peice.img.get_rect()
        centering_rect.center = self.rect.center
        display.blit(self.occupying_peice.img, centering_rect.topleft)

#def board_two(board : np.array):

#def display(board: np.array):
    #return 


    #[16,8,8]

    #[16,8,8] - 0s and 1s
    
    #output (16,8,8), -1,1 ratings of the moves


    #np.argmax(output)
    #if move is illegal:
        #output[move] = -1
    #rinse and repeat until legal move

