# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 03:11:47 2019

@author: angelo
"""

import pandas as pd

train_data = "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\DraftPrelims\\2003-2013DraftPrelim.xlsx"
#test_data = "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\DraftPrelims\\2014-2015DraftPrelim.xlsx"
#player_info = "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\FinalPlayerInfo.xlsx"
#player_stats = "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\FinalBPM.xlsx"
output_sheet = "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\outputSheet.xlsx"

NUM_ROWS_TRAIN = 448
NUM_ROWS_TEST = 83
NUM_ROWS_INFO = 7669
NUM_ROWS_STATS = 22808

trainList = pd.read_excel(train_data)
#testList = pd.read_excel(test_data)
#infoList = pd.read_excel(player_info)
#statsList = pd.read_excel(player_stats)

print(trainList)
print(trainList.iloc[1, 1])
#print(trainList.iloc[0, 1])
#print(trainList.iloc[0, 20])
#print(trainList.iloc[0, 3])

# Step 1:
# Take Draft Year, Made NBA, Draft Position, NBA Performance Rating, Name
# from trainList
for i in range(NUM_ROWS_TRAIN):
    i += 1
    output_sheet.iloc[i, 0] = trainList.iloc[i, 22]
    output_sheet.iloc[i, 1] = 1
    output_sheet.iloc[i, 2] = trainList.iloc[i, 1]
    output_sheet.iloc[i, 3] = trainList.iloc[i, 20]
    output_sheet.iloc[i, 4] = trainList.iloc[i, 3]

# Step 2:
# Match name with FinalBPM name, get College WS, College Adjusted BPM, and
# College PER


# Step 3 (add after preliminary results):
# Match name with FinalPlayerInfo name, get Position, Scouting Report,
# Height, Wingspan, Age

"""
removeCount = 0
for i in range(NUM_ROWS_ENTRY):
    i -= removeCount
    if not pd.notna(entryList.iloc[i, 15]):
        entryList.drop(entryList.index[i], inplace=True)
        removeCount += 1

entryList.to_excel("C:\\Users\\angel\\OneDrive\\College\\Work\\ESSA\DataEntryWithCEEBs.xlsx")

entryList = pd.read_excel("C:\\Users\\angel\\OneDrive\\College\\Work\\ESSA\\IBDPandCounselorsDataEntry.xlsx")

removeCount = 0
for i in range(NUM_ROWS_ENTRY):
    i -= removeCount
    if pd.notna(entryList.iloc[i, 15]):
        entryList.drop(entryList.index[i], inplace=True)
        removeCount += 1

"""

statsList.to_excel("C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\outputSheet.xlsx")