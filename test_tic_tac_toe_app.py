from game_app import TicTacToeApp
from game_engine import TicTacToeGameInfo, TicTacToeTurn

def test_1():
    app = TicTacToeApp()
    game_id_PV = app.start_game("Petya", "Vasya").game_id
    assert len(game_id_PV) > 30
    assert app.get_game_by_id(game_id_PV) == TicTacToeGameInfo(
        game_id = game_id_PV,
        field=[
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id=""
    )
    game_id_PV2 = app.start_game("Petya2", "Vasya2").game_id
    assert game_id_PV2 != game_id_PV
    assert len(game_id_PV2) > 30
    arr = list()
    arr.append(game_id_PV)
    arr.append(game_id_PV2)
    game_id_now =' '
    for _ in range(1000):
        game_id_now = app.start_game("Petya", "Vasya").game_id
        assert len(game_id_now) > 30
        for j in arr:
            assert game_id_now != j
        arr.append(game_id_now)
    app.do_turn(TicTacToeTurn("Petya", 0, 0), game_id_PV)
    app.do_turn(TicTacToeTurn("Vasya", 0, 1), game_id_PV)
    app.do_turn(TicTacToeTurn("Petya", 1, 0), game_id_PV)
    app.do_turn(TicTacToeTurn("Vasya", 1, 1), game_id_PV)
    app.do_turn(TicTacToeTurn("Petya", 0, 2), game_id_PV)
    app.do_turn(TicTacToeTurn("Vasya", 2, 0), game_id_PV)
    app.do_turn(TicTacToeTurn("Petya", 2, 1), game_id_PV)
    app.do_turn(TicTacToeTurn("Vasya", 2, 2), game_id_PV)
    app.do_turn(TicTacToeTurn("Petya", 1, 2), game_id_PV)
    assert app.get_game_by_id(game_id_PV) == TicTacToeGameInfo(
        game_id = game_id_PV,
        field=[
            ["X", "O", "X"],
            ["X", "O", " "],
            ["O", "X", "O"]
        ],
        sequence_of_turns=[
            TicTacToeTurn("Petya", 0, 0),
            TicTacToeTurn("Vasya", 0, 1),
            TicTacToeTurn("Petya", 1, 0),
            TicTacToeTurn("Vasya", 1, 1),
            TicTacToeTurn("Petya", 0, 2),
            TicTacToeTurn("Vasya", 2, 0),
            TicTacToeTurn("Petya", 2, 1),
            TicTacToeTurn("Vasya", 2, 2)
        ],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id="Draw"
    )
    assert app.get_game_by_id(game_id_PV2) == TicTacToeGameInfo(
        game_id = game_id_PV2,
        field=[
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[],
        first_player_id="Petya2",
        second_player_id="Vasya2",
        winner_id=""
    )
    app.do_turn(TicTacToeTurn("Petya2", 0, 0), game_id_PV2)
    app.do_turn(TicTacToeTurn("Vasya", 0, 1), game_id_PV2)
    app.do_turn(TicTacToeTurn("Vasya2", 0, 1), game_id_PV2)
    app.do_turn(TicTacToeTurn("Petya2", 1, 0), game_id_PV2)
    app.do_turn(TicTacToeTurn("Vasya2", 1, 1), game_id_PV2)
    app.do_turn(TicTacToeTurn("Petya2", 2, 0), game_id_PV2)
    app.do_turn(TicTacToeTurn("Vasya2", 2, 0), game_id_PV2)
    app.do_turn(TicTacToeTurn("Petya2", 2, 1), game_id_PV2)
    app.do_turn(TicTacToeTurn("Vasya2", 2, 2), game_id_PV2)
    app.do_turn(TicTacToeTurn("Petya2", 1, 2), game_id_PV2)
    assert app.get_game_by_id(game_id_PV2) == TicTacToeGameInfo(
        game_id = game_id_PV2,
        field=[
            ["X", "O", " "],
            ["X", "O", " "],
            ["X", " ", " "]
        ],
        sequence_of_turns=[
            TicTacToeTurn("Petya2", 0, 0),
            TicTacToeTurn("Vasya2", 0, 1),
            TicTacToeTurn("Petya2", 1, 0),
            TicTacToeTurn("Vasya2", 1, 1),
            TicTacToeTurn("Petya2", 2, 0),
        ],
        first_player_id="Petya2",
        second_player_id="Vasya2",
        winner_id="Petya2"
    )
    assert app.get_game_by_id(arr[3]) == TicTacToeGameInfo(
        game_id = arr[3],
        field=[
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id=""
    )
