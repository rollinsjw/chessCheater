class GameState:
    def __init__(self):
        # replace all of the pieces with actual chessPieces
        # is it quicker to keep it like this, or put chessPiece objects into the board
        # this allows the list to be smaller in memory, but requires a check to
        # see what type of piece it is
        # should I represent each piece as a number? even smaller in memory
        # how to represent ownership of a piece?

        # thoughts:
        # assign the value of a piece to its name ie: a pawn = a 1
        # this would simplify the heuristics as to access the value of a piece
        # you would just have to compare the names in a piece swap to decide
        # who would win that exchange
        self.board = [[04, 03, 02, 01000, 08, 02, 03, 04], [01, 01, 01, 01, 01, 01, 01, 01], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], ["P", "P", "P", "P", "P", "P", "P", "P"], ["R", "N", "B", "K", "Q", "B", "N", "K"]]
    # A move is a list of two tuples, the piece to be moved, and its location
    # to move to
    # first tuple is the current location of the piece to be moved
    # the legality of the move has already been checked when building the tree
    # this allows you to remove illegal moves (ie: going on top of your own
    # piece), offboard moves are taken care of in chessPiece.py
    # branches with illigal moves are trimmed and aren't searched
    def makeMove(self, board, move):
        # declare lists of the move spaces
        piece = [move[0][0], move[0][1]]
        moveTo = [move[1][0], move[1][1]]
        # make the move
        board[moveTo[0]][moveTo[1]] = board[piece[0]][piece[1]]
        board[piece[0]][piece[1]] = 0
        return board


    def checkMoveLegality(self, board, move):
