from game_app.app import TicTacToeApp

app = TicTacToeApp()
game_id_PV = app.start_game("Petya", "Vasya")
print(game_id_PV)