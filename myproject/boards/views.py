from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Board


def home(request):
    boards = Board.objects.all()
    return render(
        request, 'boards/home.html', {'boards': boards}
    )


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(
        request, 'boards/topics.html', {'board': board}
    )


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(
        request, 'boards/new_topic.html', {'board': board}
    )
