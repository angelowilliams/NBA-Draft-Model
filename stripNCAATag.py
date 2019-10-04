# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:16:51 2019

@author: angelo
"""

import pandas as pd

workingDirectory = "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project\\SOS"

draftFileNames = [workingDirectory + "\\sos2003.xlsx",
              workingDirectory + "\\sos2004.xlsx",
              workingDirectory + "\\sos2005.xlsx",
              workingDirectory + "\\sos2006.xlsx",
              workingDirectory + "\\sos2007.xlsx",
              workingDirectory + "\\sos2008.xlsx",
              workingDirectory + "\\sos2009.xlsx",
              workingDirectory + "\\sos2010.xlsx",
              workingDirectory + "\\sos2011.xlsx",
              workingDirectory + "\\sos2012.xlsx",
              workingDirectory + "\\\sos2013.xlsx"]

draftFiles = []
for draftFileName in draftFileNames:
    draftFiles.append(pd.read_excel(draftFileName))

def removeNCAA(school):
    global draftFiles

    if school.endswith("NCAA"):
        school = school[:-5]
    
    return school
        

for i in range(11):
    print(i)
    draftFiles[i]["School"]  = draftFiles[i]["School"].apply(removeNCAA)
    draftFiles[i].to_excel(draftFileNames[i])