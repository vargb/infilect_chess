from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import getPos, loggy, getMoves
import json
from . import loggy


# Create your views here.
@api_view(["POST"])
def listValidMoves(request, piece_name):
    try:
        getpos = getPos(request)
        loggy.info("gettin all da moves...")
        getAllMoves = getMoves(getpos)
        validMoves = getAllMoves[piece_name]

        loggy.info("removing moves that occur in other pieces")
        for key, value in getAllMoves.items():
            if key != piece_name:
                for i in value:
                    if i in validMoves:
                        validMoves.remove(i)

        loggy.info("returning reponse...")
        return JsonResponse({"ValidMoves - " + piece_name: validMoves})

    except (json.JSONDecodeError, KeyError, TypeError) as e:
        return JsonResponse({"error": "error in gettin em in dataclasses"})
