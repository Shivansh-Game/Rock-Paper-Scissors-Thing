import pandas as pd
import random
from comp_move import Ai 

running = True
weapons = {1:3, 2:1, 3:2}
runs = 0
move_record = pd.DataFrame(columns=["Move_selected", "Comp_move", "Win", "Loss", "Draw"])
moves = ["Rock", "Paper", "Scissors"]
auto_ask = None

computer = Ai()

while running: 
    ask = 1 if runs == 0 else auto_ask
    if runs < 20:
        Comp_ask = random.randint(1,3)
    else:
        Comp_ask = computer.calculate_move(move_record, runs)
    loss = weapons[Comp_ask] == ask
    win = weapons[ask] == Comp_ask

    move_record.loc[runs] = [ask, Comp_ask, win, loss, True if not win and not loss else False]
    if win: 
        print("Victory")
        auto_ask = 1
    elif loss:
        print("Loss")
        auto_ask = 3
    else: 
        print("Valiant duel ends in a draw")
        auto_ask = 2

    print(move_record)


    runs += 1

    if runs == 59: 
        break