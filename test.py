from chessPiece import ChessPiece
rook = ChessPiece("R", (3, 3))
bishop = ChessPiece("B", (3, 3))
knight = ChessPiece("N", (3, 3))
pawn = ChessPiece("P", (3, 3))
queen = ChessPiece("Q", (3, 3))
king = ChessPiece("K", (3, 3))
print([1,2,3,4])
possibleMoves = rook.findPossibleMoves()
print("bishop")
print(bishop.findPossibleMoves())
print("rook")
print(rook.findPossibleMoves())

print("Knight")
print(knight.findPossibleMoves())
print("pawn")
print(pawn.findPossibleMoves())
print("queen")
print(queen.findPossibleMoves())
print("king")
print(king.findPossibleMoves())