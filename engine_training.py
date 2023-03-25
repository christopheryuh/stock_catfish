import numpy as np
import torch
import chess

board = chess.Board()

num_to_letter ={0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h"}
letter_to_num ={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}

def board_to_array(board):
    x = np.zeros((14,8,8))
    for x in range(8):
        for y in range(8):
            space = num_to_letter[x]+str(y+1)
            piece = board.piece_at(chess.parse_square(space))
            if piece != None:
                print(space,piece,piece.color)

board_to_array(board)
