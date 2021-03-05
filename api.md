# API

### GET: /api/game_info?game_id=1&user_id=10
Что делать, если этот пользователь не играет в эту игру?

**response:**
```json
{
    "game_id": 1,
    "field": [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ],
    "sequence_of_turns": [],
    "first_player_id": "10",
    "second_player_id": "20",
    "winner_id": ""
}
```

### POST: /api/sign_up
**request:**
```json
{
  "user_name": "Vasya",
  ...
}
```

**response**
```json
{
  "user_name": "Vasya",
  "user_id": "af056ec7-4f62-4a38-b860-076d5b5d7ea4",
  "token": "9a5adaf4-9353-4d28-b1e7-f4c8753dea10"
}
```
