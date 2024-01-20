from django.urls import path
from .views import listValidMoves

urlpatterns = [path("/<str:piece_name>", listValidMoves)]
