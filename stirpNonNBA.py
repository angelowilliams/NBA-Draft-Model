# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:00:52 2019

@author: angelo
"""

import pandas as pd

workingDirectory = "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project"

draftFileNames = [workingDirectory + "\\DraftPrelims\\draft2003.xlsx",
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

draftFiles = []
for draftFileName in draftFileNames:
    draftFiles.append(pd.read_excel(draftFileName))

fileToStripName = workingDirectory + "\\collegeInfo.xlsx"
outputFileName = workingDirectory + "\\collegeInfoAllNBA.xlsx"
fileToStripNameField = "Name"

fileToStrip = pd.read_excel(fileToStripName)

def checkIfDrafted(row):
    global draftFiles

    for draftFile in draftFiles:   
        for draftIndex, draftRow in draftFile.iterrows():
            if row[fileToStripNameField] == draftRow["Player"]:
                print(row[fileToStripNameField])
                return 1
        
    return 0


fileToStrip["Found"] = fileToStrip.apply(checkIfDrafted, axis=1)
fileToStrip.drop(fileToStrip[fileToStrip["Found"] == 0].index, inplace=True)

fileToStrip.to_excel(outputFileName)
