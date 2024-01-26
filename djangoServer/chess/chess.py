from . import loggy

def is_valid(position):
    col, row = position[0], int(position[1 : len(position)])
    return "a" <= col <= "h" and 1 <= row <= 8


def append_if_valid(moves, position):
    if is_valid(position):
        moves.append(position)


def getQueenMoves(initPos: str,pieceList:list) -> list:
    loggy.info("getting moves for queen")
    return getBishopMoves(initPos,pieceList) + getRookMoves(initPos,pieceList)


def getRookMoves(initPos: str,pieceList:list) -> list:
    loggy.info("getting moves for rook")
    moves = []
    col, row = initPos[0], int(initPos[1])
    
    first,second,third,fourth=True,True,True,True
    
    for i in range(1,8):
        if first:
            if (chr(ord(col)+i)+str(row)) in pieceList:
                first=False
            append_if_valid(moves,chr(ord(col)+i)+str(row))
        if second:
            if (chr(ord(col)-i)+str(row)) in pieceList:
                second=False
            append_if_valid(moves,chr(ord(col)-i)+str(row))
        if third:
            if col+str(row+i) in pieceList:
                third=False
            append_if_valid(moves,col+str(row+i))
        if fourth:
            if col+str(row-i) in pieceList:
                fourth=False
            append_if_valid(moves,col+str(row-i))

    return moves


def getBishopMoves(initPos: str,pieceList:list) -> list:
    loggy.info("getting moves for bishop")
    moves = []
    col, row = initPos[0], int(initPos[1])
    
    first,second,third,fourth=True,True,True,True
    
    for i in range(1, 8):
        if first:
            if (chr(ord(col) + i) + str(row + i)) in pieceList:
                first=False
            append_if_valid(moves, chr(ord(col) + i) + str(row + i))
        if second:
            if (chr(ord(col) + i) + str(row - i)) in pieceList:
                second=False
            append_if_valid(moves, chr(ord(col) + i) + str(row - i))
        if third:
            if (chr(ord(col) - i) + str(row + i)) in pieceList:
                third=False
            append_if_valid(moves, chr(ord(col) - i) + str(row + i))
        if fourth:
            if (chr(ord(col) - i) + str(row - i)) in pieceList:
                fourth=False
            append_if_valid(moves, chr(ord(col) - i) + str(row - i))

    return moves


def getKnightMoves(initPos: str,pieceList:dict) -> list:
    loggy.info("getting moves for knight")
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
