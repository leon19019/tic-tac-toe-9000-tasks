from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict

from tic_tac_toe_game import TicTacToeGame
from .tic_tac_toe_common_lib import TicTacToeTurn, TicTacToeGameInfo

class AbstractTicTacToeApp(ABC):
    """Может показаться, что класс здесь не нужен и можно было бы обойтись просто несколькими
    переменными, но в какой-то момент логика обработки игр МОЖЕТ стать достаточно сложной и нам
    понадобится некоторый дополнительный функционал"""
    @abstractmethod
    def __init__(self):
        """пока не знаю, что тут будет :) """
        self._games: Dict[str, TicTacToeGame] = {}
        self._passwords: Dict[str, str] = {}
    
    @abstractmethod
    def start_game(self, player_id: str) -> TicTacToeGameInfo:
        """создаём игру, кладём в словарик (или другую вашу любимую коллекцию) с играми"""

    @abstractmethod
    def get_game_by_id(self, game_id: str, user_id: str) -> TicTacToeGameInfo:  
        """получаем игру, отдавать нужно только если юзер с таким user_id реально в неё играет,
        но проверку секретного ключа пользователя нужно делать в обработчиках запросов,
        а не здесь, но здесь мы реализуем методы, которые в этом помогут"""
    
    @abstractmethod
    def do_turn(self, turn: TicTacToeTurn, game_id: str) -> TicTacToeGameInfo:
        pass

    @abstractmethod
    def add_user(self):
        """регистрация"""
    
    @abstractmethod
    def is_autentified(self, user: UserInfo) -> bool:
        """проверка авторизации""" 
