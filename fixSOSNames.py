# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:07:52 2019

@author: angelo
"""

import pandas as pd

nameFile = pd.read_excel("C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\SOS\\fixedNames.xlsx")

sosFileNames = ["C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\SOS\\sos2003.xlsx",
            "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\SOS\\sos2004.xlsx",
            "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\SOS\\sos2005.xlsx",
            "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\SOS\\sos2006.xlsx",
            "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\SOS\\sos2007.xlsx",
            "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\SOS\\sos2008.xlsx",
            "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\SOS\\sos2009.xlsx",
            "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\SOS\\sos2010.xlsx",
            "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\SOS\\sos2011.xlsx",
            "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\SOS\\sos2012.xlsx",
            "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\SOS\\sos2013.xlsx"]

sosFiles = []
for sosFileName in sosFileNames:
    sosFiles.append(pd.read_excel(sosFileName))
    
    
def fixCollegeName(row):
    global nameFile
    
    for nameRow, nameRow in nameFile.iterrows():
        if row["School"] == nameRow["SOS Name"]:
            print(row["School"])
            row["School"] = nameRow["Draft Name"]
            break
        
    return row["School"]


for file in sosFiles:
    file["School"] = file.apply(fixCollegeName, axis=1)

for i in range(11):
    sosFiles[i].to_excel(sosFileNames[i])


    global unknownCounter
    global currentPick
    
    outputRow = pd.Series(index = ["Draft Year", "Draft Position", "Name", "College",
                                        "Actual NBA BPM", "College SOS", "College BPM", "College WS",
                                        "Height", "Weight", "Wingspan", "Scout Ranking", "Predicted NBA BPM",
                                        "Predicted Draft Position"])
     
    print(predictedDraft["Predicted NBA BPM"])

    found = False
    for predictedIndex, predictedRow in predictedDraft.iterrows():
        if row[currentPick, "Player"] == predictedRow["Name"]:
            found = True
            
            outputRow = predictedRow;
            print("==")
            print(outputRow["Predicted Draft Position"])
            outputRow["Predicted Draft Position"] = currentPick + unknownCounter
            print(outputRow["Predicted Draft Position"])
            break
        
    if not found:
        print(row["Player"])
        outputRow[:]
        outputRow["Name"] = "Unknown Player"
        outputRow["Predicted Draft Position"] = currentPick
        unknownCounter += 1