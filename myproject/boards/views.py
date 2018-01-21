from django.shortcuts import render
from .models import Board


def home(request):
    boards = Board.objects.all()
    return render(
        request, 'boards/home.html', {'boards': boards}
    )


def board_topic(request, pk):
    board = Board.objects.get(pk=pk)
    return render(
        request, 'boards/topics.html', {'board': board}
    )
