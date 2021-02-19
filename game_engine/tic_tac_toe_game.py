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

    def _set_winner(self):
        for elem in self.TicTacToeGameInfo.field:
            if elem == ["X", "X", "X"]:
                self.TicTacToeGameInfo.winner_id = self.TicTacToeGameInfo.first_player_id
            elif elem == ["O", "O", "O"]:
                self.TicTacToeGameInfo.winner_id = self.TicTacToeGameInfo.second_player_id

    
        for i in range(3):
            column = []
            for j in range(3):
                column.append(self.TicTacToeGameInfo.field[j][i])
            
            if column == ["X", "X", "X"]:
                self.TicTacToeGameInfo.winner_id = self.TicTacToeGameInfo.first_player_id
            elif column == ["0", "0", "0"]:
                self.TicTacToeGameInfo.winner_id = self.TicTacToeGameInfo.second_player_id

        FirstDiagonal = []
        SecondDiagonal = []
        i = 0
        for i in range(3):
            FirstDiagonal.append(self.TicTacToeGameInfo.field[i][i])
        
        i = 0
        for i in range(3):
            SecondDiagonal.append(self.TicTacToeGameInfo.field[i][2-i])

        if FirstDiagonal == ["X", "X", "X"] or SecondDiagonal == ["X", "X", "X"]:
            self.TicTacToeGameInfo.winner_id = self.TicTacToeGameInfo.first_player_id
        
        elif FirstDiagonal == ["0", "0", "0"] or SecondDiagonal == ["0", "0", "0"]:
            self.TicTacToeGameInfo.winner_id = self.TicTacToeGameInfo.second_player_id
