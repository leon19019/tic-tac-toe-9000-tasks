import os
from game_engine import TicTacToeGame, TicTacToeTurn


def print_game_info(game: TicTacToeGame):
    game_info = game.get_game_info()
    print(f"{game_info.first_player_id} vs {game_info.second_player_id}")
    print(" - - - ")
    for row in game_info.field:
        print("|" + "|".join(row) + "|")
        print(" - - - ")
    if game_info.winner_id == "":
        print(f"{game.current_player_id()}'s turn")
    elif game_info.winner_id == "draw":
        print("Draw!")
    else:
        print(f"{game_info.winner_id}'s victory!")


def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')


if __name__ == "__main__":
    screen_clear()
    game = TicTacToeGame(
        "game",
        input("Enter first player's name: "),
        input("Enter second player's name: "))

    while game.get_game_info().winner_id == "":
        print_game_info(game)
        line = input("Enter turn's coordinates: ")
        try:
            x, y = map(int, line.split())
        except Exception:
            screen_clear()
            print("Wrong format!")
            continue
        turn = TicTacToeTurn(game.GetCurrentPlayer(), x, y)
        if not game.is_turn_correct(turn):
            screen_clear()
            print("Incorrect turn!")
            continue
        game.do_turn(turn)
        screen_clear()
    print_game_info(game)
