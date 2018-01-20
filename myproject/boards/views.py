from django.shortcuts import render
from django.http import HttpResponse
import pdb

from .models import Board


def home(request):
    boards_list = Board.objects.all()
    boards_names = list()

    for board in boards_list:
        boards_names.append(board.name)

    html_response = '<br>'.join(boards_names)

    return HttpResponse(html_response)
