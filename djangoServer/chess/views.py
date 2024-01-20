from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import getPos, loggy, getMoves
import json


# Create your views here.
@api_view(["POST"])
def listValidMoves(request, piece_name):
    try:
        getpos = getPos(request)
        getAllMoves = getMoves(getpos)
        validMoves = getAllMoves[piece_name]
        for key, value in getAllMoves.items():
            if key != piece_name:
                for i in value:
                    if i in validMoves:
                        validMoves.remove(i)

        return JsonResponse({"ValidMoves - " + piece_name: validMoves})

    except (json.JSONDecodeError, KeyError, TypeError) as e:
        return JsonResponse({"error": "error in gettin em in dataclasses"})
