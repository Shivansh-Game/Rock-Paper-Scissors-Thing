import pandas as pd
import random
from comp_move import Ai 

running = True
weapons = {1:3, 2:1, 3:2}
runs = 0
move_record = pd.DataFrame(columns=["Move_selected", "Comp_move", "Win", "Loss", "Draw"])
moves = ["Rock", "Paper", "Scissors"]

computer = Ai()

while running: 
    ask = int(input("What Shall Be Your Weapon For The Duel?: \n 1: Rock \n 2: Paper \n 3: scissors \n Select using the numbers: "))
    if runs < 20:
        Comp_ask = random.randint(1,3)
    else:
        Comp_ask = computer.calculate_move(move_record, runs)
    loss = weapons[Comp_ask] == ask
    win = weapons[ask] == Comp_ask

    move_record.loc[runs] = [ask, Comp_ask, win, loss, True if not win and not loss else False]
    if win: 
        print("Victory")
    elif loss:
        print("Loss")
    else: 
        print("Valiant duel ends in a draw")

    print(move_record)
    runs += 1