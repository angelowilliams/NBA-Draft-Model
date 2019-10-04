# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 13:31:47 2019

@author: Angelo Williams
@email : awilliams21@wooster.edu
"""

import pandas as pd
import os

# Gets this script's directory to find other files
workingDirectory = os.getcwd()

ceebName = input("Enter the name of your spreadsheet containing CEEB codes (e.g. 'ceeb_list.xlsx'): ")
ceebSchoolColName = input("Enter the name of the column in the CEEB code spreadsheet that lists the school names: ")
ceebCEEBColName = input("Enter the name of the column in the CEEB code spreadsheet that lists the school CEEBs: ")

listName = input("Enter the name of your spreadsheet containing the schools to match CEEB codes to (e.g. 'school_list.xlsx'): ")
listSchoolColName = input("Enter the name of the column in the school spreadsheet that lists the school names: ")

 
listFile = pd.read_excel(listName)
ceebFile = pd.read_excel(ceebName)

outputName = listName.split(".xlsx")[0] + "_withCEEB.xlsx"

def checkCEEB(row):
    global counter
    global ceebFile
    
    if (counter % 10 == 0):
        print(counter)
    
    counter += 1
    
    CEEB = ""
    for ceebIndex, ceebRow in ceebFile.iterrows():
        if ceebRow[ceebSchoolColName] == row[listSchoolColName]:
            CEEB = ceebRow[ceebCEEBColName]
            break
        
    row["CEEB"] = CEEB
        
    return row


counter = 1
listFile = listFile.apply(checkCEEB, axis=1)

listFile.to_excel(outputName)
