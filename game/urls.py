from django.urls import path
from game import views

urlpatterns = [
    path('', views.mainView),
    path('save_game/', views.save_game, name='save_game'),
    path('waiting_room/', views.GameListView.as_view(), name='games_view'),
    path('game/<int:pk>', views.game_room, name='game_start')
]
