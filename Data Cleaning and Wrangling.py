# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 01:04:25 2019

@author: DEBJYOTA
"""
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

#set  working direcotry

os.chdir("E:\\Python Data Analysis")

#import the dataset into panda data frame

Finalcial_Data = pd.read_csv("Future-500-Data.csv")



#Transform Inception to Category value like Factor in R
Finalcial_Data["Inception"]=Finalcial_Data["Inception"].astype("category")
Finalcial_Data["ID"]=Finalcial_Data["ID"].astype("category")

print(Finalcial_Data.info())
print(Finalcial_Data.describe())

Finalcial_Data.head(30)

#Transform  Expese ,Reveune Growth from object to number
#Replace nan values in panda before make them int 
#Remove Dollars,$ % from respectve columns
Finalcial_Data["Expenses"]=Finalcial_Data["Expenses"].str.replace(" Dollars","")
Finalcial_Data["Expenses"]=Finalcial_Data["Expenses"].str.replace(",","")
Finalcial_Data["Revenue"]=Finalcial_Data["Revenue"].str.replace("$","")
Finalcial_Data["Revenue"]=Finalcial_Data["Revenue"].str.replace(",","")
Finalcial_Data["Growth"]=Finalcial_Data["Growth"].str.replace("%","")

Finalcial_Data["Expenses"]=Finalcial_Data["Expenses"].astype("int")

Finalcial_Data["Expenses"]


