from game_engine import TicTacToeGame, TicTacToeGameInfo, TicTacToeTurn


def test_scenario():
    game = TicTacToeGame(
        game_id="0001",
        first_player_id="Petya",
        second_player_id="Vasya"
    )

    assert game.get_game_info() == TicTacToeGameInfo(
        game_id="0001",
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

    assert game.is_turn_correct(
        TicTacToeTurn(
            player_id="Petya",
            x_coordinate=0,
            y_coordinate=0
        )
    ) == True

    assert game.is_turn_correct(
        TicTacToeTurn(
            player_id="Petya",
            x_coordinate=-10,
            y_coordinate=-10
        )
    ) == False

    assert game.is_turn_correct(
        TicTacToeTurn(
            player_id="Vasya",
            x_coordinate=0,
            y_coordinate=0
        )
    ) == False

    game_info = game.get_game_info()
    game_info.field[0][0] = "@"
    assert game.get_game_info() == TicTacToeGameInfo(
        game_id="0001",
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

    assert game.do_turn(
        TicTacToeTurn(
            player_id="Petya",
            x_coordinate=0,
            y_coordinate=0
        )
    ) == TicTacToeGameInfo(
        game_id="0001",
        field=[
            ["X", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[
            TicTacToeTurn(
                player_id="Petya",
                x_coordinate=0,
                y_coordinate=0
            )
        ],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id=""
    )

    assert game.get_game_info() == TicTacToeGameInfo(
        game_id="0001",
        field=[
            ["X", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[
            TicTacToeTurn(
                player_id="Petya",
                x_coordinate=0,
                y_coordinate=0
            )
        ],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id=""
    )

    assert game.is_turn_correct(
        TicTacToeTurn(
            player_id="Vasya",
            x_coordinate=0,
            y_coordinate=0
        )
    ) == False

    assert game.is_turn_correct(
        TicTacToeTurn(
            player_id="Petya",
            x_coordinate=0,
            y_coordinate=0
        )
    ) == False

    game.do_turn(TicTacToeTurn("Petya", 1, 0))
    game.do_turn(TicTacToeTurn("Vasya", 1, 0))
    game.do_turn(TicTacToeTurn("Petya", 0, 1))
    game.do_turn(TicTacToeTurn("Vasya", 1, 1))
    game.do_turn(TicTacToeTurn("Petya", 0, 2))

    assert game.get_game_info() == TicTacToeGameInfo(
        game_id="0001",
        field=[
            ["X", "X", "X"],
            ["O", "O", " "],
            [" ", " ", " "]
        ],
        sequence_of_turns=[
            TicTacToeTurn("Petya", 0, 0),
            TicTacToeTurn("Vasya", 1, 0),
            TicTacToeTurn("Petya", 0, 1),
            TicTacToeTurn("Vasya", 1, 1),
            TicTacToeTurn("Petya", 0, 2)
        ],
        first_player_id="Petya",
        second_player_id="Vasya",
        winner_id="Petya"
    )

    assert game.is_turn_correct(
        TicTacToeTurn(
            player_id="Vasya",
            x_coordinate=1,
            y_coordinate=2
        )
    ) == False

