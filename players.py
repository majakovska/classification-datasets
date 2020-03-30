import numpy as np 
import pandas as pd


df = pd.read_csv('pretprocesiran.csv' , delimiter=',', encoding="utf-8-sig")

grouped_df = df.groupby(
    ['winner_id']
).agg(
    {
        # find the min, max, and sum of the duration column
        'w_ace': "mean",
        'w_df': "mean",
        'w_bpFaced': "mean",
        'w_SvGms': "mean",
        'w_1stServe%': "mean",
        'w_1stServePWon%': "mean",
        'w_2ndServePWon%': "mean", 
        'w_BreakPWon%' : "mean",
        
        'winner_age' : "max",
        'winner_rank' : "max",
        'winner_rank_points' : "max"
    }
)

grouped_df.to_csv('grouped_players.csv')


player1 = grouped_df.ix[201311]
player2 = grouped_df.ix[201320]

print(player1 - player2)


#Izvlacimo jednog igraca da mozemo da plotujemo raspodelu za njega

my_player = grouped_df.ix[201311]

my_player.to_csv('one_player_data.csv')