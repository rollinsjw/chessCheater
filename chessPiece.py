class ChessPiece:
    """"This class represents a chess piece"""
    # add a value to help with heuristics?
    def __init__(self, pieceType, position, side):

        self.pieceType = pieceType
        self.side = side
        # position is a tuple or a list? pick which one it should be
        self.position = position

    # how to take into account the position of other pieces?
    # right now this assumes that there is an empty board

    # maybe we check to see if a move is valid only if the computer wants to
    # take it this would minimize the number of times we have to check for
    # legitimacy
    # or would the computer check if this is a good move each time
    def findPossibleMoves(self):
        possibleMoves = []
        pieceType = self.pieceType
        position = self.position
        if pieceType == "N":
            moves = [(3, 2), (2, 3), (-3, 2), (3, -2), (-2, 3), (2, -3), (-2, -3), (-3, -2)]
            possibleMoves = self.findMovesRecursively(moves)
        elif pieceType == "R":
            for i in range(0, 7):
                possibleMoves.append(self.addTuples(position, (0, i)))
                possibleMoves.append(self.addTuples(position, (i, 0)))
                possibleMoves.append(self.addTuples(position, (0, -i)))
                possibleMoves.append(self.addTuples(position, (-i, 0)))
                # remove the current position of the piece
                # ToDo: remove offboard moves
        elif pieceType == "B":
            for i in range(0, 7):
                possibleMoves.append(self.addTuples(position, (i, i)))
                possibleMoves.append(self.addTuples(position, (-i, -i)))
                possibleMoves.append(self.addTuples(position, (-i, i)))
                possibleMoves.append(self.addTuples(position, (i, -i)))
        # how to deal with the diagonal move (if an opponent is there)
        # must create gameState class
        elif pieceType == "P":
            possibleMoves.append(self.addTuples(position, (0, 1)))
        elif pieceType == "Q":
            for i in range(0, 7):
                # diagonals
                possibleMoves.append(self.addTuples(position, (i, i)))
                possibleMoves.append(self.addTuples(position, (-i, -i)))
                possibleMoves.append(self.addTuples(position, (-i, i)))
                possibleMoves.append(self.addTuples(position, (i, -i)))
                # verticals and horizontals
                possibleMoves.append(self.addTuples(position, (0, i)))
                possibleMoves.append(self.addTuples(position, (i, 0)))
                possibleMoves.append(self.addTuples(position, (0, -i)))
                possibleMoves.append(self.addTuples(position, (-i, 0)))
        elif pieceType == "K":
            # diagonals
            possibleMoves.append(self.addTuples(position, (1, 1)))
            possibleMoves.append(self.addTuples(position, (-1, -1)))
            possibleMoves.append(self.addTuples(position, (-1, 1)))
            possibleMoves.append(self.addTuples(position, (1, -1)))
            # verticals and horizontals
            possibleMoves.append(self.addTuples(position, (0, 1)))
            possibleMoves.append(self.addTuples(position, (1, 0)))
            possibleMoves.append(self.addTuples(position, (0, -1)))
            possibleMoves.append(self.addTuples(position, (-1, 0)))

        # just in case the current position is not included within this,
        # you must handle that situation
        # this is janky, how can we make this better?
        try:
            count = possibleMoves.count(position)
            for i in range(0, count):
                possibleMoves.remove(position)
        except:
            error = "handled"
        # remove off Board moves
        possibleMoves = self.removeOffBoardMoves(possibleMoves)
        return possibleMoves

    # done recursively just for practice
    def findMovesRecursively(self, moves):
        move = moves.pop()
        if len(moves) == 0:
            return [self.addTuples(self.position, move)]
        else:
            newPosition = self.addTuples(self.position, move)
            if newPosition[0] >= 0 or newPosition[1] >= 0:
                return [newPosition] + self.findMovesRecursively(moves)
            else:
                return self.findMovesRecursively(moves)

    # remove offBoardMoves
    def removeOffBoardMoves(self, possibleMoves):
        i = 0
        # use a while loop so you can control the index i while modifying the
        # possible moves
        while i < len(possibleMoves):
            move = possibleMoves[i]
            if move[0] < 0 or move[1] < 0 or move[0] > 7 or move[1] > 7:
                possibleMoves.remove(move)
            else:
                i += 1
        return possibleMoves

    # function to add tuples together
    # put this in a tools class
    def addTuples(self, a, b):
        c = (a[0] + b[0], a[1] + b[1])
        return c
