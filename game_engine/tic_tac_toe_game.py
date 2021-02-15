from copy import deepcopy
from typing import Callable, List, Optional
from .tic_tac_toe_common_lib import TicTacToeTurn, TicTacToeGameInfo, AbstractTicTacToeGame


class TicTacToeGame(AbstractTicTacToeGame):
    def __init__(
        self,
        game_id,
        first_player_id,
        second_player_id
    ):
        self._player_id = first_player_id
        self.TicTacToeGameInfo = TicTacToeGameInfo(
            game_id = game_id,
            field = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
            ],
            sequence_of_turns = [],
            first_player_id = first_player_id,
            second_player_id = second_player_id,
            winner_id = ""
        )

    def is_turn_correct(self, TicTacToeTurn):
        X = TicTacToeTurn.x_coordinate
        Y = TicTacToeTurn.y_coordinate

        if self.TicTacToeGameInfo.winner_id == "":
            if self._player_id == TicTacToeTurn.player_id:
                if (X >= 0 and X < 3) and (Y >= 0 and Y < 3):
                    if self.TicTacToeGameInfo.field[X][Y] == " ":
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


    def do_turn(self, TicTacToeTurn):
        X = TicTacToeTurn.x_coordinate
        Y = TicTacToeTurn.y_coordinate

        if self.is_turn_correct(TicTacToeTurn):
            if TicTacToeTurn.player_id == self.TicTacToeGameInfo.first_player_id:
                self.TicTacToeGameInfo.field[X][Y] = "X"
                self._player_id = self.TicTacToeGameInfo.second_player_id
            
            elif TicTacToeTurn.player_id == self.TicTacToeGameInfo.second_player_id:
                self.TicTacToeGameInfo.field[X][Y] = "O"
                self._player_id = self.TicTacToeGameInfo.first_player_id



            self.TicTacToeGameInfo.sequence_of_turns.append(TicTacToeTurn)

            self._set_winner()

            return self.TicTacToeGameInfo
        else:
            return self.TicTacToeGameInfo

    
    def get_game_info(self):
        return deepcopy(self.TicTacToeGameInfo)

    def _set_winner(self) -> None:
        if self.TicTacToeGameInfo.winner_id != "":
            return

        field = self.get_game_info().field

        for i in range(3):
            row1 = []
            row2 = []

            for j in range(3):
                row1.append(field[i][j])
                row2.append(field[j][i])

            if row1 == ["X"] * 3 or row2 == ["X"] * 3:
                self._winner_id = self.TicTacToeGameInfo.first_player_id
                return

            if row1 == ["O"] * 3 or row2 == ["O"] * 3:
                self._winner_id = self.TicTacToeGameInfo.second_player_id
                return

            if ("X" not in row1) or ("X" not in row2) or ("O" not in row1) or ("O" not in row2):
                draw = False

        row1 = []
        row2 = []
        draw = True

        for i in range(3):
            row1.append(field[i][i])
            row2.append(field[i][2 - i])

        if row1 == ["X"] * 3 or row2 == ["X"] * 3:
            self._winner_id = self.TicTacToeGameInfo.first_player_id
            return

        if row1 == ["O"] * 3 or row2 == ["O"] * 3:
            self._winner_id = self.TicTacToeGameInfo.second_player_id
            return

        if ("X" not in row1) or ("X" not in row2) or ("O" not in row1) or ("O" not in row2):
            draw = False

        if draw:
            self._winner_id = "draw"
