import numpy as np 
import pygame, chess

WHITE = (255,255,255)
BLACK = (0,0,0)


class Square:

    def __init__(self, x, y, width, height):
        self .x = x 
        self .y = y 
        self .width = width
        self .height = height
        self .abs_x = x * width
        self .abs_y = y * height
        self .abs_pos  = (self.abs_pos, self.abs_y)
        self .pos = (x,y)
        self .color = 'white' if (x + y) % 2 == 0 else 'black'
        self .draw_color = (WHITE) if self.color == 'white' else (BLACK)
        #something to maybe creat a highlight for possible moves
        self .occupying_piece  = None 
        self .coord  = self.get_coord()
        self . rect = pygame.Rect(
            self .abs_x, 
            self.abs_y, 
            self.width, 
            self.height
        )
        
    def get_coord(self):
        columns = 'abcdefgh'
        
        return columns[self.x]

def board_two(board : np.array):

def display(board: np.array):
    return 


    [16,8,8]

    [16,8,8] - 0s and 1s
    |
    output (16,8,8), -1,1 ratings of the moves


    np.argmax(output)
    if move is illegal:
        output[move] = -1
    rinse and repeat until legal move

