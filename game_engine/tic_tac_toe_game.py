from typing import Callable
from copy import deepcopy

from tic_tac_toe_common_lib import TicTacToeGameInfo, TicTacToeTurn, AbstractTicTacToeGame

class TicTacToeGame(AbstractTicTacToeGame):
    def __init__(self, game_id: str, first_player_id: str, second_player_id: str,
                 strategy: Callable[[TicTacToeGameInfo], TicTacToeTurn] = None) -> None:
        self.__game_id = game_id
        self.__first_player_id = first_player_id
        self.__second_player_id = second_player_id
        self.__winner_id = ""
        self.__strategy = strategy
        self.__turns = []

    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        pass

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        pass

    def get_game_info(self) -> TicTacToeGameInfo:
        result = TicTacToeGameInfo(
            game_id=self.__game_id,
            field=[
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ],
            sequence_of_turns=deepcopy(self.__turns),
            first_player_id=self.__first_player_id,
            second_player_id=self.__second_player_id,
            winner_id=self.__winner_id
        )
        for turn in self.__turns:
            if turn.player_id == self.__first_player_id:
                ch = "X"
            else:
                ch = "O"
            result.field[turn.x_coordinate][turn.x_coordinate] = ch
        return result