# API

# What do we send

To start new game:

```json
    {"first_player_id":"Name", "second_player_id":"Name", "game_id":123}
```

When someone is doing moition:

```json
    TicTacToeGameInfo
```

# What server is sending to us

When someone is making move server is cheching does he have same data with client

```json
    TicTacToeGameInfo
```