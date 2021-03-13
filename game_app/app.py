from typing import Dict
import random

from game_engine.tic_tac_toe_game import TicTacToeGame
from game_engine.tic_tac_toe_common_lib import TicTacToeGameInfo, TicTacToeTurn


class GameWithThisIdAlreadyExists(Exception):
    pass


class TicTacToeApp:
    def __init__(self):
        self._games: Dict[str, TicTacToeGame] = {}
        self._passwords: Dict[str, str] = {}

    def start_game(self, first_player_id, second_player_id, game_id = None):
        if game_id != None:
            if game_id not in self._games:
                game = TicTacToeGame(game_id, first_player_id, second_player_id)
                self._games.update({game_id:game})
                return game.TicTacToeGameInfo

            else:
                TicTacToeApp.make_game_with_random_game_id(self, first_player_id, second_player_id)

        else:
            game_id = random.randint(1000000000000000000000000000000, 12345678765436565876776656566565756687686876786745534232433345343453453532554474655756756757657657)
            game = TicTacToeGame(str(game_id), first_player_id, second_player_id)
            self._games.update({str(game_id):game})
            return game.TicTacToeGameInfo



        
                

    
    def make_game_with_random_game_id(self, first_player_id, second_player_id):
        _game_id = random.randint(1000000000000000000000000000000, 12345678765436565876776656566565756687686876786745534232433345343453453532554474655756756757657657)
        TicTacToeApp.start_game(self, first_player_id, second_player_id, _game_id)


    def is_id_free(self, game_id):
        if self._games[game_id] == None:
            return True
        else:
            return False

    def get_game_by_id(self, game_id: str):
        return self._games[game_id].TicTacToeGameInfo

    def do_turn(self, TicTacToeTurn, game_id: str):
        self._games[game_id].do_turn(TicTacToeTurn)

    def add_user(self, user_id: str, password: str):
        self._passwords[user_id] = password

    def is_autentified(self, UserInfo):
        if self._passwords[UserInfo.user_id] == UserInfo.password:
            return True
