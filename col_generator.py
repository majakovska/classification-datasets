import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter as Cnt

df1 = pd.read_csv('wta_matches_2016.csv')
df2 = pd.read_csv('wta_matches_2014.csv')
# df3 = pd.read_csv('wta_matches_2013.csv')
# df4 = pd.read_csv('wta_matches_2012.csv')

# print("Eeeee")

df = pd.concat([df1, df2])

# print(len(df))

# procenat pogodnjenog prvog servisa
df['w_1stServe%'] = 0.0
df['l_1stServe%'] = 0.0


# broj pogodjenih drugih servisa
df['w_2ndIn'] = 0.0
df['l_2ndIn'] = 0.0

#procenat osvojenih poena na prvom servisu
df['w_1stServePWon%'] = 0.0
df['l_1stServePWon%'] = 0.0



#procenat osvojenih poena na drugom servisu 
df['w_2ndServePWon%'] = 0.0
df['l_2ndServePWon%'] = 0.0

df['w_1stServeReturnPWon'] = 0.0
df['l_1stServeReturnPWon'] = 0.0

df['w_2ndServeReturnPWon'] = 0.0
df['l_2ndServeReturnPWon'] = 0.0

df['w_1stServeReturnPWon%'] = 0.0
df['l_1stServeReturnPWon%'] = 0.0


df['w_BreakPWon%'] = 0.0
df['l_BreakPWon%'] = 0.0

df['w_BreakPWon'] = 0.0
df['l_BreakPWon'] = 0.0



df['w_BreakPConverted%'] = 0.0
df['l_BreakPConverted%'] = 0.0


for index, row in df.iterrows() : 

	df.set_value(index, 'w_1stServe%', row['w_1stIn'] / row['w_svpt'])
	df.set_value(index, 'l_1stServe%', row['l_1stIn'] / row['l_svpt'])

# 	# ################################################
for index, row in df.iterrows() : 

	df.set_value(index, 'w_2ndIn', row['w_svpt'] - row['w_1stIn'])
	df.set_value(index, 'l_2ndIn', row['l_svpt'] - row['l_1stIn'])

# 	# ################################################
for index, row in df.iterrows() : 

	df.set_value(index, 'w_1stServePWon%', row['w_1stWon'] / row['w_1stIn'])
	df.set_value(index, 'l_1stServePWon%', row['l_1stWon'] / row['l_1stIn'])

# 	# ################################################

for index, row in df.iterrows() : 
	# print(row['w_2ndIn'])
	if(row['w_2ndIn']) :
		df.set_value(index, 'w_2ndServePWon%', row['w_2ndWon'] / row['w_2ndIn'])

	else :

		df.set_value(index, 'w_2ndServePWon', 1.0)

	if(row['l_2ndIn']) :

		df.set_value(index, 'l_2ndServePWon%', row['l_2ndWon'] / row['l_2ndIn'])

	else :

		df.set_value(index, 'l_2ndServePWon', 1.0)

# 	# ################################################

for index, row in df.iterrows() : 

	df.set_value(index, 'w_1stServeReturnPWon', row['l_1stIn'] - row['l_1stWon'])
	df.set_value(index, 'l_1stServeReturnPWon', row['w_1stIn'] - row['w_1stWon'])

# 	# ################################################

for index, row in df.iterrows() : 

	df.set_value(index, 'w_2ndServeReturnPWon', row['l_2ndIn'] - row['l_2ndWon'])
	df.set_value(index, 'l_2ndServeReturnPWon', row['w_2ndIn'] - row['w_2ndWon'])

# 	# ################################################

for index, row in df.iterrows() : 

	if(row['l_1stIn']) :

		df.set_value(index, 'w_1stServeReturnPWon%', row['w_1stServeReturnPWon'] / row['l_1stIn'])

	else :

		df.set_value(index, 'w_1stServeReturnPWon%', 1.0)

	if(row['w_1stIn']) :

		df.set_value(index, 'l_1stServeReturnPWon%', row['l_1stServeReturnPWon'] / row['w_1stIn'])

	else :

		df.set_value(index, 'l_1stServeReturnPWon%', 1.0)


# 	# ############################

for index, row in df.iterrows() : 

	if(row['w_bpFaced']) :

		df.set_value(index, 'w_BreakPWon%', row['w_bpSaved'] / row['w_bpFaced'])

	else :

		df.set_value(index, 'w_BreakPWon%', 1.0)


	if(row['l_bpFaced']) :

		df.set_value(index, 'l_BreakPWon%', row['l_bpSaved'] / row['l_bpFaced'])

	else :

		df.set_value(index, 'l_BreakPWon%', 1.0)

# 	# ################################################

for index, row in df.iterrows() : 


	df.set_value(index, 'w_BreakPWon', row['l_bpFaced'] - row['l_bpSaved'])
	df.set_value(index, 'l_BreakPWon', row['w_bpFaced'] - row['w_bpSaved'])


# 	# ################################################

for index, row in df.iterrows() : 

	if(row['l_bpFaced']) :

		df.set_value(index, 'w_BreakPConverted%', row['w_BreakPWon'] / row['l_bpFaced'])

	else :

		df.set_value(index, 'w_BreakPConverted%', 1.0)


	if(row['w_bpFaced']) :

		df.set_value(index, 'l_BreakPConverted%', row['l_BreakPWon'] / row['w_bpFaced'])

	else :

		df.set_value(index, 'l_BreakPConverted%', 1.0)


df.to_csv('pretprocesiran.csv', index = False)

# df_pretprocessed = pd.read_csv('pretprocesiran.csv' , delimiter=',', encoding="utf-8-sig")

# # print(df_pretprocessed['w_1stServe%'])

# colname = df_pretprocessed.columns[0]

# col_list = ['winner_rank', 'loser_rank', 'winner_rank_points', 'loser_rank_points', \
#  	'winner_age', 'loser_age', 'w_ace', 'l_ace', 'w_df', 'l_df', 'w_bpFaced', 'l_bpFaced', 'w_SvGms', \
# 	'l_SvGms', 	'w_1stServe%', 'l_1stServe%', 'w_1stServePWon%', 'l_1stServePWon%', 'w_2ndServePWon%', \
#  	'l_2ndServePWon%', 'w_BreakPWon%', 'l_BreakPWon%'
# ]

# main_df = df_pretprocessed.loc[:, col_list]

# cols_for_substraction_generated = ['ace', 'df', 'bpFaced', \
# 	'SvGms', 	'1stServe%', '1stServePWon%', '2ndServePWon%', \
#  	'BreakPWon%']

	
# for col in cols_for_substraction_generated :

# 	main_df[col + '_diff'] = main_df['w_'+col] - main_df['l_'+col]


# print(main_df.head())
