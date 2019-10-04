# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:07:52 2019

@author: angelo
"""

import pandas as pd


workingDirectory = "C:\\Users\\angel\\OneDrive - The College of Wooster\\College\\Semester2\\Math Modelling\\Final Project"

averageWingspan = 77.78746

statsFileName = workingDirectory + "\\CollegeStats.xlsx"
infoFileName = workingDirectory + "\\CollegeInfo.xlsx"

statsFile = pd.read_excel(statsFileName)
infoFile = pd.read_excel(infoFileName)

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

outputFileNames = [workingDirectory + "\\Drafts\\draft2003.xlsx",
               workingDirectory + "\\Drafts\\draft2004.xlsx",
               workingDirectory + "\\Drafts\\draft2005.xlsx",
               workingDirectory + "\\Drafts\\draft2006.xlsx",
               workingDirectory + "\\Drafts\\draft2007.xlsx",
               workingDirectory + "\\Drafts\\draft2008.xlsx",
               workingDirectory + "\\Drafts\\draft2009.xlsx",
               workingDirectory + "\\Drafts\\draft2010.xlsx",
               workingDirectory + "\\Drafts\\draft2011.xlsx",
               workingDirectory + "\\Drafts\\draft2012.xlsx",
               workingDirectory + "\\Drafts\\draft2013.xlsx"]

nbaSeasonFileNames = [workingDirectory + "\\NBA Seasons\\season2003.xlsx",
                      workingDirectory + "\\NBA Seasons\\season2004.xlsx",
                      workingDirectory + "\\NBA Seasons\\season2005.xlsx",
                      workingDirectory + "\\NBA Seasons\\season2006.xlsx",
                      workingDirectory + "\\NBA Seasons\\season2007.xlsx",
                      workingDirectory + "\\NBA Seasons\\season2008.xlsx",
                      workingDirectory + "\\NBA Seasons\\season2009.xlsx",
                      workingDirectory + "\\NBA Seasons\\season2010.xlsx",
                      workingDirectory + "\\NBA Seasons\\season2011.xlsx",
                      workingDirectory + "\\NBA Seasons\\season2012.xlsx",
                      workingDirectory + "\\NBA Seasons\\season2013.xlsx",
                      workingDirectory + "\\NBA Seasons\\season2014.xlsx",
                      workingDirectory + "\\NBA Seasons\\season2015.xlsx",
                      workingDirectory + "\\NBA Seasons\\season2016.xlsx"]

def addSOS(row):
    global sosFile
    
    found = False
    for sosIndex, sosRow in sosFile.iterrows():
        if row["College"] == sosRow["School"]:
            found = True
            row["College SOS"] = sosRow["SOS"]
            break
        
    if not found:
        print("Could not find school for SOS: " + row["College"])
        row["College SOS"] = "N/A"
        
    return row

    
def addStats(row):
    global statsFile
    
    found = False
    rowList = []
    for statsIndex, statsRow in statsFile.iterrows():
        if row["Name"] == statsRow["PlayerName"]:
            found = True
            rowList.append(statsRow)
            break
        
    if not found:
        print("College stats not found for " + row["Name"])
        
    lastYearRow = rowList[0]
    for statsRow in rowList:
        if lastYearRow["TermYear"] > statsRow["TermYear"]:
            lastYearRow = statsRow

    
    row = pd.concat([row, lastYearRow.loc["GP": "3FGA"], lastYearRow.loc["OWS": "Estimated DBPM"]])
    
    return row
    

def addInfo(row):
    global infoFile
    global averageWingspan
    
    found = False
    wingspan = "Not Available"
    for infoIndex, infoRow in infoFile.iterrows():
        if row["Name"] == infoRow["Name"]:
            found = True
            
            position = infoRow["Pos"]
            height = infoRow["Hght\n(inches)"]
            weight = infoRow["Wght"]
            wingspan = infoRow["Avg Predicted Wingspan (inches"]
            
            break
        
    if not found:
        print("College info not found for " + row["Name"])

    if wingspan == "Not Available":
        wingspan = averageWingspan
    
    isGuard = 0
    isForward = 0
    isCenter = 0
    if position == "G":
        isGuard = 1
    elif position == "F":
        isForward = 1
    elif position == "C":
        isCenter = 1
        
    row["Guard"] = isGuard
    row["Forward"] = isForward
    row["Center"] = isCenter

    row["Height"] = height
    row["Weight"] = weight
    row["Wingspan"] = wingspan
    
    return row


def addCWS(row):
    global seasonFile1
    global seasonFile2
    global seasonFile3
    global seasonAvgWS1
    global seasonAvgWS2
    global seasonAvgWS3
    global seasonAvgWS481
    global seasonAvgWS482
    global seasonAvgWS483
    global seasonStdWS1
    global seasonStdWS2
    global seasonStdWS3
    global seasonStdWS481
    global seasonStdWS482
    global seasonStdWS483
    
    seasons = [seasonFile1, seasonFile2, seasonFile3]
    avgWSs = [seasonAvgWS1, seasonAvgWS2, seasonAvgWS3]
    avgWS48s = [seasonAvgWS481, seasonAvgWS482, seasonAvgWS483]
    stdWSs = [seasonStdWS1, seasonStdWS2, seasonStdWS3]
    stdWS48s = [seasonStdWS481, seasonStdWS482, seasonStdWS483]

    
    CWS = 0;
    for i in range(3):
        seasonFile = seasons[i]
        avgWS = avgWSs[i]
        avgWS48 = avgWS48s[i]
        stdWS = stdWSs[i]
        stdWS48 = stdWS48s[i]

        found = False
        for seasonIndex, seasonRow in seasonFile.iterrows():
            if row["Name"] == seasonRow["Player"]:
                found = True;
                CWS += (seasonRow["WS"] / avgWS)
                CWS += (seasonRow["WS/48"] / avgWS48)
                break
            
        if not found:
            CWS += ((avgWS - stdWS) / avgWS)
            CWS += ((avgWS48 - stdWS48) / avgWS48)
                
        
    row["3-year CWS"] = CWS
    
    return row
    

for i in range(11):
    print("NOW WORKING ON {} DRAFT".format(2003+i))
    
    draftFileName = draftFileNames[i]
    outputFileName = outputFileNames[i]
    sosFileName = sosFileNames[i]
    
    draftFile = pd.read_excel(draftFileName)
    sosFile = pd.read_excel(sosFileName)
    outputFile = pd.DataFrame()
    
    seasonFile1 = pd.read_excel(nbaSeasonFileNames[i])
    seasonFile2 = pd.read_excel(nbaSeasonFileNames[i + 1])
    seasonFile3 = pd.read_excel(nbaSeasonFileNames[i + 2])
    seasonAvgWS1 = seasonFile1["WS"].mean()
    seasonAvgWS2 = seasonFile2["WS"].mean()
    seasonAvgWS3 = seasonFile3["WS"].mean()
    seasonAvgWS481 = seasonFile1["WS/48"].mean()
    seasonAvgWS482 = seasonFile2["WS/48"].mean()
    seasonAvgWS483 = seasonFile3["WS/48"].mean()
    seasonStdWS1 = seasonFile1["WS"].std()
    seasonStdWS2 = seasonFile1["WS"].std()
    seasonStdWS3 = seasonFile1["WS"].std()
    seasonStdWS481 = seasonFile1["WS/48"].std()
    seasonStdWS482 = seasonFile2["WS/48"].std()
    seasonStdWS483 = seasonFile3["WS/48"].std()

    
    print("Adding draft data")
    outputFile["Draft Year"] = draftFile["Draft Year"]
    outputFile["Draft Position"] = draftFile["Pk"]
    outputFile["Name"] = draftFile["Player"]
    outputFile["College"] = draftFile["College"]
    
    #Add blank columns
    outputFile["Predicted 3-Year CWS"] = ""
    outputFile["Predicted Draft Position"] = ""

    print("Adding 3-year CWS")
    outputFile = outputFile.apply(addCWS, axis=1)
    
    print("Adding college info")
    outputFile = outputFile.apply(addInfo, axis=1)
    
    print("Adding SOS data")
    outputFile = outputFile.apply(addSOS, axis=1)
    
    print("Adding college stats")
    outputFile = outputFile.apply(addStats, axis=1)

    print("Creating output")
    outputFile.to_excel(outputFileName)
    print("Done\n")
    