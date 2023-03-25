# stock_catfish
A chess bot

that probably wont be that good...


# planning

todo:
pick chess library, do we want it to do all the work? or do we want some leway

- engine will take a board and output move given the best move from a databse

engine.py
- takes saved model and rates all possible next moves, then it choses the best next move

engine _training.py
- handle all training for the bot, will not be connected to final project, just outputs a saved model file

ui.py
- takes a game state, probably an array of some sorts and puts it onto a ui


main.py

uses functions from ui and engine and makes the final product
