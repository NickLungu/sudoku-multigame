import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import SudokuGame


def mainView(request):
    return render(request,'index.html')


def game_room(request, pk):
    game = get_object_or_404(SudokuGame, pk=pk)
    return render(request, 'index.html', {'state':game.puzzle_state})


def save_game(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        game_state = data.get('game_state')

        if game_state:
            # Assuming you have a 'state' field in your SudokuModel
            SudokuGame.objects.create(puzzle_state=game_state)

            return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})


class GameListView(ListView):
    model = SudokuGame
    template_name = "waiting_room.html"
    context_object_name = 'games'


