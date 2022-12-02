# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 07:46:36 2022

@author: Will Kew
@email: will.kew[at]gmail.com
"""


import numpy as np
import pandas as pd

dataloc = r'D:\Coding\AoC22\day2/'

df = pd.read_csv(dataloc+'input.txt',sep=' ',names=['Play','Counter'])

values = {'A':1,#Rock
          'B':2,#Paper
          'C':3,#Scissors
          'X':1,#Rock
          'Y':2,#Paper
          'Z':3, #Scissors
          'loss':0,
          'draw':3,
          'win':6}


# this is really inefficient but its only 2500 rows so who cares
for index, data in df.iterrows():
    df.loc[index,'Play_pt'] = values[data['Play']]
    df.loc[index,'Counter_pt'] = values[data['Counter']]
    # If they play rock and you play scissors, you lose
    if (data['Play'] == 'A') & (data['Counter'] == 'Z'):
        result = 'loss'
    # if they play paper and you play rock, you lose
    elif (data['Play'] == 'B') & (data['Counter'] == 'X'):
        result = 'loss'
    # if they play scissors and you play Paper, you lose
    elif (data['Play'] == 'C') & (data['Counter'] == 'Y'):
        result = 'loss'
    # if they play rock and you play paper, you win
    elif (data['Play'] == 'A') & (data['Counter'] == 'Y'):
        result = 'win'
    # if they play paper and you play scissors, you win
    elif (data['Play'] == 'B') & (data['Counter'] == 'Z'):
        result = 'win'
    # if they play scissors and you play rock, you win
    elif (data['Play'] == 'C') & (data['Counter'] == 'X'):
        result = 'win'
    else:
        result = 'draw'
    df.loc[index,'result'] = result
    df.loc[index,'result_pt'] = values[result]
    
df['YourScore'] = df['Counter_pt']+df['result_pt']

print(df['YourScore'].sum())


## Part 2


new_values = {'A':1,#Rock
          'B':2,#Paper
          'C':3,#Scissors
          'X':0,#loss
          'Y':3,#draw
          'Z':6 #win
          }

df2 = pd.read_csv(dataloc+'input.txt',sep=' ',names=['Play','Counter'])

# this is really inefficient but its only 2500 rows so who cares
for index, data in df2.iterrows():
    df2.loc[index,'Play_pt'] = new_values[data['Play']]
    #now 'my' column is the result of the match
    df2.loc[index,'result_pt'] = new_values[data['Counter']]
    
    #If you have to lose:
    if data['Counter'] == 'X':
        if data['Play'] == 'A': countplay = 'C' #rock/scissors
        elif data['Play'] == 'B': countplay = 'A' #paper/rock
        elif data['Play'] == 'C': countplay = 'B' #scissors/paper
    #If you have to draw:
    elif data['Counter'] == 'Y':
        if data['Play'] == 'A': countplay = 'A' # rock/rock
        elif data['Play'] == 'B': countplay = 'B' # paper/paper
        elif data['Play'] == 'C': countplay = 'C' # scissors/scissors
    #If you have to win: 
    elif data['Counter'] == 'Z':
        if data['Play'] == 'A': countplay = 'B' # rock/paper
        elif data['Play'] == 'B': countplay = 'C' #paper/scissors
        elif data['Play'] == 'C': countplay = 'A' #scissors/rock
    df2.loc[index,'countplay'] = countplay
    df2.loc[index,'countplay_pt'] = new_values[countplay]

   
df2['YourScore'] = df2['countplay_pt']+df2['result_pt']

print(df2['YourScore'].sum())