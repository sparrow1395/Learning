# It's time for chess

chess_players = {"Carlsen, Magnus": 1865, "Firouzja, Alireza": 2804, "Ding, Liren": 2799,
                 "Caruana, Fabiano": 1792, "Nepomniachtchi, Ian": 2773}

new_chess = {elo: f'{name.split(",")[0]}. {name.split(",")[1][1]}' for name, elo
             in chess_players.items() if elo > 2000}
print(new_chess)
