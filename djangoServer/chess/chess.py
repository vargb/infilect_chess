from .models import loggy
from . import loggy


def is_valid(position):
    col, row = position[0], int(position[1 : len(position)])
    return "a" <= col <= "h" and 1 <= row <= 8


def append_if_valid(moves, position):
    if is_valid(position):
        moves.append(position)


def getQueenMoves(initPos: str) -> list:
    loggy.info("getting moves for queen")
    return getBishopMoves(initPos) + getRookMoves(initPos)


def getRookMoves(initPos: str) -> list:
    loggy.info("getting moves for rook")
    moves = []
    col, row = initPos[0], int(initPos[1])

    for i in range(1, 8):
        append_if_valid(moves, chr(ord(col) + i) + str(row))
        append_if_valid(moves, chr(ord(col) - i) + str(row))
        append_if_valid(moves, col + str(row + i))
        append_if_valid(moves, col + str(row - i))

    return moves


def getBishopMoves(initPos: str) -> list:
    loggy.info("getting moves for bishop")
    moves = []
    col, row = initPos[0], int(initPos[1])

    for i in range(1, 8):
        append_if_valid(moves, chr(ord(col) + i) + str(row + i))
        append_if_valid(moves, chr(ord(col) + i) + str(row - i))
        append_if_valid(moves, chr(ord(col) - i) + str(row + i))
        append_if_valid(moves, chr(ord(col) - i) + str(row - i))

    return moves


def getKnightMoves(initPos: str) -> list:
    loggy.info("gettin moves for knight")
    moves = []
    col, row = initPos[0], int(initPos[1])

    knight_moves = [
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1),
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
    ]

    for move in knight_moves:
        new_col, new_row = ord(col) + move[0], row + move[1]
        new_position = chr(new_col) + str(new_row)
        append_if_valid(moves, new_position)

    return moves
