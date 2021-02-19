 
from .tic_tac_toe_abstract_app import AbstractTicTacToeApp
from tic_tac_toe_game import TicTacToeGame
import random
from typing import Dict

class TicTacToeApp(AbstractTicTacToeApp):
    def __init__(self):
        self._games: Dict[str, TicTacToeGame] = {}
        self._passwords: Dict[str, str] = {}

    def start_game(self, first_player_id: str, second_player_id: str, game_id = random.randint(0,1000000000000000000000000000000000000000000000000000000000000000000000)):
        if self.is_id_free:
            game = TicTacToeGame(game_id, first_player_id, second_player_id)
            self._games[game_id] = game
            return game.TicTacToeGameInfo
        elif self.is_id_free == False:
            game_id = random.randint(0,1000000000000000000000000000000000000000000000000000000000000000000000)
            game = TicTacToeGame(game_id, first_player_id, second_player_id)
            self._games[game_id] = game
            return game.TicTacToeGameInfo

    def is_id_free(self, game_id):
        if self._games[game_id] == None:
            return True
        else:
            return False


    def get_game_by_id(self, game_id: str, user_id: str):
        if self._games[game_id].TicTacToeGameInfo.first_player_id == user_id or self._games[game_id].TicTacToeGameInfo.second_player_id:
            return self._games[game_id].TicTacToeGameInfo

    def do_turn(self, TicTacToeTurn, game_id: str):
        self._games[game_id].do_turn(TicTacToeTurn)

    def add_user(self, user_id: str, password: str):
        self._passwords[user_id] = password

    def is_autentified(self, UserInfo):
        if self._passwords[UserInfo.user_id] == UserInfo.password:
            return True