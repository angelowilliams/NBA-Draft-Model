# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:07:52 2019

@author: angelo
"""

import pandas as pd

workingDirectory = "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project"

uneditedDraftNames = [workingDirectory + "\\DraftPrelims\\Unedited Drafts\\draft2003.xlsx",
                      workingDirectory + "\\DraftPrelims\\Unedited Drafts\\draft2004.xlsx",
                      workingDirectory + "\\DraftPrelims\\Unedited Drafts\\draft2005.xlsx",
                      workingDirectory + "\\DraftPrelims\\Unedited Drafts\\draft2006.xlsx",
                      workingDirectory + "\\DraftPrelims\\Unedited Drafts\\draft2007.xlsx",
                      workingDirectory + "\\DraftPrelims\\Unedited Drafts\\draft2008.xlsx",
                      workingDirectory + "\\DraftPrelims\\Unedited Drafts\\draft2009.xlsx",
                      workingDirectory + "\\DraftPrelims\\Unedited Drafts\\draft2010.xlsx",
                      workingDirectory + "\\DraftPrelims\\Unedited Drafts\\draft2011.xlsx",
                      workingDirectory + "\\DraftPrelims\\Unedited Drafts\\draft2012.xlsx",
                      workingDirectory + "\\DraftPrelims\\Unedited Drafts\\draft2013.xlsx"]

predictedDraftNames = [workingDirectory + "\\Predicted Drafts\\draft2003.xlsx",
                       workingDirectory + "\\Predicted Drafts\\draft2004.xlsx",
                       workingDirectory + "\\Predicted Drafts\\draft2005.xlsx",
                       workingDirectory + "\\Predicted Drafts\\draft2006.xlsx",
                       workingDirectory + "\\Predicted Drafts\\draft2007.xlsx",
                       workingDirectory + "\\Predicted Drafts\\draft2008.xlsx",
                       workingDirectory + "\\Predicted Drafts\\draft2009.xlsx",
                       workingDirectory + "\\Predicted Drafts\\draft2010.xlsx",
                       workingDirectory + "\\Predicted Drafts\\draft2011.xlsx",
                       workingDirectory + "\\Predicted Drafts\\draft2012.xlsx",
                       workingDirectory + "\\Predicted Drafts\\draft2013.xlsx"]
                      
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

uneditedDraftNames = [workingDirectory + "\\DraftPrelims\\draft2019.xlsx"]
predictedDraftNames = [workingDirectory + "\\Predicted Drafts\\draft2019first.xlsx"]
mockDraftNames = [workingDirectory + "\\Mock Drafts\\draft2019.xlsx"]


uneditedDrafts = []
for uneditedDraftName in uneditedDraftNames:
    uneditedDrafts.append(pd.read_excel(uneditedDraftName))
    
predictedDrafts = []
for predictedDraftName in predictedDraftNames:
    predictedDrafts.append(pd.read_excel(predictedDraftName))
    
mockDrafts = []
for mockDraftName in mockDraftNames:
    mockDrafts.append(pd.read_excel(mockDraftName))    
    
    
def addDraftPicks(row):
    global draftPick
    draftPick += 1
    
    return draftPick


def getUnknownPlayerIndices():
    global uneditedDraft
    global predictedDraft
    
    totalCount = len(uneditedDraft.index)
    predictedCount = len(predictedDraft.index)
    
    unknownPlayerDraftPositions = []
    for i in range(totalCount):
        found = False
        playerName = uneditedDraft.iloc[i, :]["Player"]
        for k in range(predictedCount):
            if playerName == predictedDraft.iloc[k, :]["Name"]:
                found = True
        
        if not found:
            unknownPlayerDraftPositions.append(uneditedDraft.iloc[i, :]["Pk"])
            
    return unknownPlayerDraftPositions


def fixDraftPositions(row):
    global unknownPlayerDraftPositions
    global unknownCount
    
    poppedCount = 0
    for i in range(len(unknownPlayerDraftPositions)):
        i -= poppedCount
        if unknownPlayerDraftPositions[i] <= row["Predicted Draft Position"] + unknownCount:
            unknownCount += 1
            unknownPlayerDraftPositions.pop(0)
            poppedCount += 1
            
    return row["Predicted Draft Position"] + unknownCount
        

def insertEmptyRows():
    global unknownPlayerDraftPositions
    global predictedDraft
    
    while (len(unknownPlayerDraftPositions) > 0):
        draftPositionToFill = unknownPlayerDraftPositions.pop(0)
                        
        injectRow = pd.Series()
        injectRow["Name"] = "Unknown Player"
        injectRow["Predicted Draft Position"] = draftPositionToFill
        
        beginSegment = predictedDraft.iloc[:draftPositionToFill - 1, :]
        endSegment = predictedDraft.iloc[draftPositionToFill - 1:, :]

        injectRow = injectRow.to_frame().T
        
        predictedDraft = pd.concat([beginSegment, injectRow, endSegment], ignore_index=1, sort=False)
        
        
for i in range(1):
    print("Working on {} draft".format(2003 + i))

    predictedDraft = predictedDrafts[i]
    uneditedDraft = uneditedDrafts[i]
    predictedDraft = predictedDraft.sort_values(by=["Predicted 3-Year CWS"], ascending=False)
            
    draftPick = 0
    predictedDraft["Predicted Draft Position"] = predictedDraft.apply(addDraftPicks, axis=1)
    
    unknownPlayerDraftPositions = getUnknownPlayerIndices()

    unknownCount = 0
    predictedDraft["Predicted Draft Position"] = predictedDraft.apply(fixDraftPositions, axis=1)
    
    unknownPlayerDraftPositions = getUnknownPlayerIndices()
    insertEmptyRows()
    
    predictedDraft.to_excel(mockDraftNames[i])
    
print("Done!")