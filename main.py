import os
import pandas as pd
import re
from glob import glob
from collections import defaultdict
from group_distribution import queryYesNo
from group_distribution import copyToGroups


# Adjust column names of the .xlsx here
#########################
kuerzelCol = "u-Kürzel"
groupCol = "Gruppe"
headerRow = 1
##########################


def userDialog():
    # Group distribution excel-file input
    print("\n")
    myFilesPaths = glob(r'.\*.xlsx')
    if len(myFilesPaths) >= 1:
        for x in range(len(myFilesPaths)):
            print(str(x),":",myFilesPaths[x])
    else:
        print("\nMake sure there is an excel file in this folder")
        exit()
    while True:
        try:
            fileNum = int(input("Select the Excel file with the number above: "))
            if (fileNum < len(myFilesPaths)):
                df = pd.read_excel(myFilesPaths[fileNum], header=headerRow)
                break
            else:
                print("Wrong file number try again")
        except ValueError:
            print("Please enter an integer")

    # Select the group range to move
    print("\n")
    while True:
        try:
            groupCorrect = input("Input the range of the groups you have to correct in format int, int: ")
            groupStrings = groupCorrect.split(',')
            if (2 == len(groupStrings)):
                groupRange = [int(x) for x in groupStrings]
                groupRange.sort()
                groupRange[1] += 1
                break
            else:
                print("More or less than 2 comma separated values")
        except ValueError:
            print("Please enter an integer")

    # Source folder input
    print("\n")
    sourceFolder = glob('*/')
    if len(sourceFolder) >= 1:
        for x in range(len(sourceFolder)):
            print(str(x),":",sourceFolder[x])
    else:
        print("\nMake sure there is a subdirectory with the all documentations")
        exit()
    while True:
        try:
            folderNum = int(input("Select the Path to the Folder that contains the documentations with the number above: "))
            if (folderNum < len(sourceFolder)):
                path = sourceFolder[folderNum]
                break
            else:
                print("Wrong folder number try angain")
        except ValueError:
            print("Please enter an integer")

    # Choice whether feedback file is wanted in group folders
    print("\n")
    if queryYesNo("Do you want a copy of an evaluation sheet in every group folder?"):
        feedbackPath = glob(r'.\*.pdf')
        if len(feedbackPath) >= 1:
            for x in range(len(feedbackPath)):
                print(str(x),":",feedbackPath[x])
        else:
            print("\nMake sure there is a PDF file in the main folder")
            exit()
        while True:
            try:
                feedbackNum = int(input("Select the feedback pdf with the number above: "))
                if (feedbackNum < len(feedbackPath)):
                    feedbackFile = os.path.abspath(feedbackPath[feedbackNum])
                    break
                else:
                    print("Wrong feedback number try angain")
            except ValueError:
                print("Please enter an integer")
    else:
        feedbackFile = ""
    return df, groupRange, path, feedbackFile




if __name__ == "__main__":
    df, groupRange, path, feedbackFile = userDialog()

    if kuerzelCol not in df or groupCol not in df:
        raise ValueError("Specified columns not found, adjust groupCol, kuerzelCol names or headerRow in main.py")
    groupsAndMembers = defaultdict(list)

    for index, row in df.iterrows():
        # TODO define this with regex
        groupId = re.findall(r"\d{1,3}|$", str(row[groupCol]))[0]
        try:
            groupId = int(groupId)
        except ValueError:
            groupId = 0
        kuerz = re.findall(r"^u[a-z]{4}|$", row[kuerzelCol])[0]
        groupsAndMembers[groupId].append(kuerz)

    # Copy documents to group folders
    copyToGroups(groupsAndMembers, groupRange, path, feedbackFile)
    print("Finished")