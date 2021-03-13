from typing import Dict
import random

from game_engine import TicTacToeGame, TicTacToeGameInfo, TicTacToeTurn


class GameWithThisIdAlreadyExists(Exception):
    pass


class TicTacToeApp:
    def __init__(self):
        self._games: Dict[str, TicTacToeGame] = {}
        self._passwords: Dict[str, str] = {}

    def start_game(self, first_player_id: str, second_player_id: str, game_id):
        if self.is_id_free(game_id):
            game = TicTacToeGame(game_id, first_player_id, second_player_id)
            self._games[game_id] = game
            return game.TicTacToeGameInfo

        else:
            raise GameWithThisIdAlreadyExists


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