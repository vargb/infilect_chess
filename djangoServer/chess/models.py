from django.db import models
from django.http import JsonResponse
from dataclasses import dataclass
import json
from . import loggy
from .chess import getBishopMoves, getKnightMoves, getQueenMoves, getRookMoves, is_valid


# Create your models here.


@dataclass
class Pieces:
    queen: str
    bishop: str
    rook: str
    knight: str


@dataclass
class Pos:
    pos: Pieces


def getPos(request) -> Pos:
    loggy.info("getting all the pieces to dataclasses for easier use...")
    if request.method == "POST":
        try:
            # Parse json data from the request body
            if request.body:
                json_data = json.loads(request.body.decode())

                chess_data_instance = Pos(
                    pos=Pieces(
                        queen=(json_data["positions"]["Queen"]).lower(),
                        bishop=(json_data["positions"]["Bishop"]).lower(),
                        rook=(json_data["positions"]["Rook"]).lower(),
                        knight=(json_data["positions"]["Knight"]).lower(),
                    )
                )

                if (
                    is_valid(chess_data_instance.pos.queen)
                    and is_valid(chess_data_instance.pos.bishop)
                    and is_valid(chess_data_instance.pos.rook)
                    and is_valid(chess_data_instance.pos.knight)
                ):
                    return chess_data_instance
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            loggy.error("error in parsing to json", e)
            raise e
        raise KeyError

    loggy.error("return an error response, somethings up check it out")
    raise JsonResponse({"error": "Invalid request method"}, status=400)


def getMoves(getpos: Pos):
    moves = {"queen": [], "knight": [], "bishop": [], "rook": []}
    moves["knight"] = getKnightMoves(getpos.pos.knight)
    moves["queen"] = getQueenMoves(getpos.pos.queen)
    moves["bishop"] = getBishopMoves(getpos.pos.bishop)
    moves["rook"] = getRookMoves(getpos.pos.rook)
    return moves
