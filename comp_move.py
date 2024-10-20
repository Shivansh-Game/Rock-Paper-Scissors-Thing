import pandas as pd
import random  


class Ai:
    def __init__(self):
        self.choices = {1:3, 2:1, 3:2}
        self.rock_stat = {"Total" : 0, "After Win" : 0, "After Loss": 0, "After Draw": 0}
        self.paper_stat = {"Total" : 0, "After Win" : 0, "After Loss": 0, "After Draw": 0}
        self.scissors_stat = {"Total" : 0, "After Win" : 0, "After Loss": 0, "After Draw": 0}
        self.most_total = None
        self.most_after_win = None
        self.most_after_loss = None
        self.most_after_draw = None
        self.max_total = None
        self.max_after_win = None
        self.max_after_loss = None
        self.max_after_draw = None
        

    def calculate_move(self, move_record, runs):
        last_round_outcome = None
        Choice = None
    
        if move_record.loc[len(move_record) - 2].loc["Win"]:
            last_round_outcome = "win"
        elif move_record.loc[len(move_record) - 2].loc["Loss"]:
            last_round_outcome = "loss"
        else:
            last_round_outcome = "draw"
    
        if runs <= 20:
            print("Here")
            for i in range(len(move_record)):
                if move_record.loc[i].loc["Move_selected"] == 3:
                    self.scissors_stat["Total"] += 1
                    if move_record.loc[i].loc["Win"]:
                        self.scissors_stat["After Win"] += 1
                    if move_record.loc[i].loc["Loss"]:
                        self.scissors_stat["After Loss"] += 1
                    if move_record.loc[i].loc["Draw"]:
                        self.scissors_stat["After Draw"] += 1
    
                if move_record.loc[i].loc["Move_selected"] == 2:
                    self.paper_stat["Total"] += 1
                    if move_record.loc[i].loc["Win"]:
                        self.paper_stat["After Win"] += 1
                    if move_record.loc[i].loc["Loss"]:
                        self.paper_stat["After Loss"] += 1
                    if move_record.loc[i].loc["Draw"]:
                        self.paper_stat["After Draw"] += 1
    
                if move_record.loc[i].loc["Move_selected"] == 1:
                    self.rock_stat["Total"] += 1
                    if move_record.loc[i].loc["Win"]:
                        self.rock_stat["After Win"] += 1
                    if move_record.loc[i].loc["Loss"]:
                        self.rock_stat["After Loss"] += 1
                    if move_record.loc[i].loc["Draw"]:
                        self.rock_stat["After Draw"] += 1
    
                if self.rock_stat["Total"] > self.paper_stat["Total"] and self.rock_stat["Total"] > self.scissors_stat["Total"]:
                    self.most_total = 1
                elif self.paper_stat["Total"] > self.scissors_stat["Total"]:
                    self.most_total = 2
                else:
                    self.most_total = 3 
    
                if self.rock_stat["After Win"] > self.paper_stat["After Win"] and self.rock_stat["After Win"] > self.scissors_stat["After Win"]:
                    self.most_after_win = 1
                elif self.paper_stat["After Win"] > self.scissors_stat["After Win"]:
                    self.most_after_win = 2
                else:
                    self.most_after_win = 3 
    
                if self.rock_stat["After Loss"] > self.paper_stat["After Loss"] and self.rock_stat["After Loss"] > self.scissors_stat["After Loss"]:
                    self.most_after_loss = 1
                elif self.paper_stat["After Loss"] > self.scissors_stat["After Loss"]:
                    self.most_after_loss = 2
                else:
                    self.most_after_loss = 3 
    
                if self.rock_stat["After Draw"] > self.paper_stat["After Draw"] and self.rock_stat["After Draw"] > self.scissors_stat["After Draw"]:
                    self.most_after_draw = 1
                elif self.paper_stat["After Draw"] > self.scissors_stat["After Draw"]:
                    self.most_after_draw = 2
                else:
                    self.most_after_draw = 3

        self.max_total = max(self.rock_stat["Total"], self.paper_stat["Total"], self.scissors_stat["Total"])
        self.max_after_win = max(self.rock_stat["After Win"], self.paper_stat["After Win"], self.scissors_stat["After Win"])
        self.max_after_loss = max(self.rock_stat["After Loss"], self.paper_stat["After Loss"], self.scissors_stat["After Loss"])
        self.max_after_draw = max(self.rock_stat["After Draw"], self.paper_stat["After Draw"], self.scissors_stat["After Draw"])    
            
        if last_round_outcome == "win": 
            Choice = self.choices[self.most_after_win]
            '''if self.most_total == self.most_after_win:
                Choice = self.choices[self.most_after_win]
            else:
                Choice = self.choices[self.most_total] if random.randint(1,4) == 3 else self.choices[self.most_after_win] '''
        
        if last_round_outcome == "loss": 
            Choice = self.choices[self.most_after_loss]
            '''if self.most_total == self.most_after_loss:
                Choice = self.choices[self.most_after_loss]
            else:
                Choice = self.choices[self.most_total] if random.randint(1,4) == 3 else self.choices[self.most_after_loss] '''
        
        if last_round_outcome == "draw": 
            Choice = self.choices[self.most_after_draw]
            '''if self.most_total == self.most_after_draw:
                Choice = self.choices[self.most_after_draw]
            else:
                Choice = self.choices[self.most_total] if random.randint(1,4) == 3 else self.choices[self.most_after_draw] '''
        return Choice