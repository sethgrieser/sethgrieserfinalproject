#!/usr/bin/env python
# coding: utf-8

# In[1]:


# NBAPlayoffSimulation.py
# This program will run the seven game playoff series between every team
# Uisng team data from 2019-2020 NBA season
# This team will take the data from the NBA MatchupData pyhton file
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
import NBAMatchData.py


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




