import numpy as np 
import pandas as pd

df = pd.read_csv('pretprocesiran.csv' , delimiter=',', encoding="utf-8-sig")

# print(df_pretprocessed['w_1stServe%'])

# colname = df.columns[0]

col_list = ['winner_rank', 'loser_rank', 'winner_rank_points', 'loser_rank_points', \
 	'winner_age', 'loser_age', 'w_ace', 'l_ace', 'w_df', 'l_df', 'w_bpFaced', 'l_bpFaced', 'w_SvGms', \
	'l_SvGms', 	'w_1stServe%', 'l_1stServe%', 'w_1stServePWon%', 'l_1stServePWon%', 'w_2ndServePWon%', \
 	'l_2ndServePWon%', 'w_BreakPWon%', 'l_BreakPWon%'
]

main_df = df.loc[:, col_list]

cols_for_substraction_generated = ['ace', 'df', 'bpFaced', \
	'SvGms', 	'1stServe%', '1stServePWon%', '2ndServePWon%', \
 	'BreakPWon%']

cols_for_substraction_original = ['rank', 'rank_points', 'age']

length = int(len(main_df)/2)

for col in cols_for_substraction_generated :

	main_df.loc[:length, col + '_diff'] = main_df['w_'+col] - main_df['l_'+col]
	main_df.loc[length:, col + '_diff'] = main_df['l_'+col] - main_df['w_'+col]


for col in cols_for_substraction_original :

	main_df.loc[:length, col + '_diff'] = main_df['winner_'+col] - main_df['loser_'+col]
	main_df.loc[length:, col + '_diff'] = main_df['loser_'+col] - main_df['winner_'+col]


main_df.loc[:length, 'outcome'] = 'yes'
main_df.loc[length:, 'outcome'] = 'no'


diff_df = main_df.iloc[:, 22:]

print(diff_df.columns)

diff_df.to_csv('substracted.csv', index = False)