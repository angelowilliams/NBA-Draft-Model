# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:07:52 2019

@author: angelo
"""

import pandas as pd

infoFile = pd.read_excel("C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\collegeInfo.xlsx")

def fixCollege(row):
    global infoFile
    
    found = False
    for infoIndex, infoRow in infoFile.iterrows():
        if row["Player"] == infoRow["Name"]:
            found = True
            row["College"] = infoRow["Final School"]
            break
        
    if not found:
        print(row["Player"])
        
    return row["College"]


draftFiles = []
draftFileNames = ["draft2003", "draft2004", "draft2005", "draft2006", "draft2007", "draft2008", "draft2009", "draft2010", "draft2011", "draft2012", "draft2013"]
for fileName in draftFileNames:
    draftFiles.append(pd.read_excel("C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\DraftPrelims\\{0}.xlsx".format(fileName)))

i = 0
for file in draftFiles:
    i += 1
    print(i)
    file["College"] = file.apply(fixCollege, axis=1)
    file["Draft Year"] = i + 2002

for i in range(11):
    draftFiles[i].to_excel("C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\DraftPrelims\\{0}.xlsx".format(draftFileNames[i]))
