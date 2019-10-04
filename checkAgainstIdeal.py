# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:43:58 2019

@author: angelo
"""


import pandas as pd

workingDirectory = "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project"

idealDraftNames = [workingDirectory + "\\Ideal Drafts\\draft2003.xlsx",
                       workingDirectory + "\\Ideal Drafts\\draft2004.xlsx",
                       workingDirectory + "\\Ideal Drafts\\draft2005.xlsx",
                       workingDirectory + "\\Ideal Drafts\\draft2006.xlsx",
                       workingDirectory + "\\Ideal Drafts\\draft2007.xlsx",
                       workingDirectory + "\\Ideal Drafts\\draft2008.xlsx",
                       workingDirectory + "\\Ideal Drafts\\draft2009.xlsx",
                       workingDirectory + "\\Ideal Drafts\\draft2010.xlsx",
                       workingDirectory + "\\Ideal Drafts\\draft2011.xlsx",
                       workingDirectory + "\\Ideal Drafts\\draft2012.xlsx",
                       workingDirectory + "\\Ideal Drafts\\draft2013.xlsx"]

actualDraftNames = [workingDirectory + "\\DraftPrelims\\draft2003.xlsx",
                       workingDirectory + "\\DraftPrelims\\draft2004.xlsx",
                       workingDirectory + "\\DraftPrelims\\draft2005.xlsx",
                       workingDirectory + "\\DraftPrelims\\draft2006.xlsx",
                       workingDirectory + "\\DraftPrelims\\draft2007.xlsx",
                       workingDirectory + "\\DraftPrelims\\draft2008.xlsx",
                       workingDirectory + "\\DraftPrelims\\draft2009.xlsx",
                       workingDirectory + "\\DraftPrelims\\draft2010.xlsx",
                       workingDirectory + "\\DraftPrelims\\draft2011.xlsx",
                       workingDirectory + "\\DraftPrelims\\draft2012.xlsx",
                       workingDirectory + "\\DraftPrelims\\draft2013.xlsx"]
                      
mockDraftNames = [workingDirectory + "\\Mock Drafts\\draft2003.xlsx",
                  workingDirectory + "\\Mock Drafts\\draft2004.xlsx",
                  workingDirectory + "\\Mock Drafts\\draft2005.xlsx",
                  workingDirectory + "\\Mock Drafts\\draft2006.xlsx",
                  workingDirectory + "\\Mock Drafts\\draft2007.xlsx",
                  workingDirectory + "\\Mock Drafts\\draft2008.xlsx",
                  workingDirectory + "\\Mock Drafts\\draft2009.xlsx",
                  workingDirectory + "\\Mock Drafts\\draft2010.xlsx",
                  workingDirectory + "\\Mock Drafts\\draft2011.xlsx",
                  workingDirectory + "\\Mock Drafts\\draft2012.xlsx",
                  workingDirectory + "\\Mock Drafts\\draft2013.xlsx"]

idealDrafts = []
for idealDraftName in idealDraftNames:
    idealDrafts.append(pd.read_excel(idealDraftName))
    
actualDrafts = []
for actualDraftName in actualDraftNames:
    actualDrafts.append(pd.read_excel(actualDraftName))
    
mockDrafts = []
for mockDraftName in mockDraftNames:
    mockDrafts.append(pd.read_excel(mockDraftName))    
    

for i in range(11):
    print("Working on {} draft".format(2003 + i))

    idealDraft = idealDrafts[i]
    actualDraft = actualDrafts[i]
    mockDraft = mockDrafts[i]

    idealDraft = idealDraft.sort_values(by=["Name"], ascending=True)
    actualDraft = actualDraft.sort_values(by=["Player"], ascending=True)
    mockDraft = mockDraft.sort_values(by=["Name"], ascending=True)

    count = 0;
    totalActualDist = 0;
    totalMockDist = 0;
    for idealIdx, idealRow in idealDraft.iterrows():
        playerName = idealRow["Name"]
        if playerName == "Unknown Player":
            continue
        
        idealPk = idealRow["Predicted Draft Position"]
        
        found = False
        for actualIdx, actualRow in actualDraft.iterrows():
            if actualRow["Player"] == playerName:
                found = True
                actualPk = actualRow["Pk"]
                break
        
        for mockIdx, mockRow in mockDraft.iterrows():
            if mockRow["Name"] == playerName:
                found = True
                mockPk = mockRow["Predicted Draft Position"]
                break        

        if not found:
            print("===========")
            print(playerName)
            print("===========")
  
        if abs(idealPk - mockPk) > 40:
            print(playerName)
            
        totalActualDist += abs(idealPk - actualPk)
        totalMockDist += abs(idealPk - mockPk)
        count += 1
        
    actualAvgPkDist = float(totalActualDist) / count
    mockAvgPkDist = float(totalMockDist) / count
    
    print(actualAvgPkDist)
    print(mockAvgPkDist)
    
print("Done!")