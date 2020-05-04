#!/usr/bin/env python
# coding: utf-8

# In[17]:


# NBAMatchupData.py
# This program will import the statistics of every team
# During the 2019-2020 NBA season
# Then will use these statistics to simulate a game between two teams 
# That can be used to simulate the entire 2020 NBA postseason
# Use of NBA data permitted by fair use, being for educational purposes
# Seth Grieser 
# SES350 Final Project

import numpy as np
import pandas as pd 
import random as rnd 
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import optimize 
from scipy import ndimage
from pylab import *
from scipy.integrate import odeint

gdf = pd.read_csv('nba2020.csv')                           # Read in NBA 2019-2020 Regular Season statistics 
gdf.columns                                                # Sort excel data by columns 


lal = gdf[gdf.Team == 'LAL']                                # Assigns lal for Lakers Team Data
mem = gdf[gdf.Team == 'MEM']                                # Same, but mem for Memphis Team Data


lal.Pts.hist()                                              # Creates a histogram of Lakers PPG vs. Mem PPG 
mem.Pts.hist()                                              # By amount of games it occurs for each team

lalmeanpts = lal.Pts.mean()                                 # Mean of PPG for each team
memmeanpts = mem.Pts.mean()
lalpts = lal.Pts.std()                                      # SD of PPG for each team
mempts = mem.Pts.std()

rnd.gauss(110, 15)                                      # Assigns random gaussian distribtion of 110 PPG
                                                           # And a SD of 15 points, roughly league averages 


print("Lakers Points Mean ", lalmeanpts)
print("Lakers Points SD ", lalpts)
print("Memphis Points Mean ", memmeanpts)
print("Memphis Points SD ", mempts)

def gameSim():
    LALScore = (rnd.gauss(lalmeanpts,lalmeanpts))
    MEMScore = (rnd.gauss(memmeanpts,mempts))
    if int(round(LALScore)) > int(round(MEMScore)):
        return 1
    elif int(round(LALScore)) < int(round(MEMScore)):
        return -1
    else: return 0

def gamesSim(ns):
    gamesout = []
    team1win = 0
    team2win = 0
    tie = 0
    for i in range(ns):
        gm = gameSim()
        gamesout.append(gm)
        if gm == 1:
            team1win +=1 
        elif gm == -1:
            team2win +=1
        else: tie +=1 
    print('LAL Win ', team1win/(team1win+team2win+tie),'%')
    print('MEM Win ', team2win/(team1win+team2win+tie),'%')
    print('Tie ', tie/(team1win+team2win+tie), '%')
    return gamesout

gamesSim(7)


# In[ ]:




