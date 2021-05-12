import os
import shutil

          
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
    return

def memberNotFound(folder, member):
    createFolder(folder)
    logFile = folder + '/missing_members.txt'
    with open(logFile, "a") as file:
        file.write(str(member)+"\n")
    return

def copyMember(path, folder, name):
    createFolder(folder)
    dst = os.path.abspath(folder + "/" + name)
    src = os.path.abspath(path + name)
    shutil.copytree(src,dst)
    return

def copyFeedback(group,folder,feedbackFile):
    feedbackFileName = os.path.split(feedbackFile)[1]
    feedbackFilePath = folder + '/' + feedbackFileName
    #4 because ".pdf" are 4 charakters
    newFeedbackFileName = feedbackFileName[:-4] + "_Gruppe_" + str(group) + feedbackFileName[-4:]
    newFeedbackFilePath = folder + '/' + newFeedbackFileName
    if not (os.path.isfile(feedbackFilePath) or os.path.isfile(newFeedbackFilePath)) :
        shutil.copy(feedbackFile,folder)
    if (os.path.isfile(feedbackFilePath) and not os.path.isfile(newFeedbackFilePath)):
        os.rename(feedbackFilePath, newFeedbackFilePath)
    return

def copyToGroups(groupsAndMembers, groupRange, path, feedbackFile=""):
    for group, members in groupsAndMembers.items():
        for member in members:
            found = False
            folder = './Korrektur/Gruppe_' + str(group)
            folder = os.path.abspath(folder)
            if (group in range(groupRange[0],groupRange[1])):
                for name in os.listdir(path):
                    if os.path.isdir(path + name) and member in name:
                        found = True
                        copyMember(path, folder, name)
                        if feedbackFile:
                            copyFeedback(group, folder, feedbackFile)
                if found == False:
                    memberNotFound(folder, member)
    return



#### This part is from https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input

def queryYesNo(question, default="no"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        choice = input(question + prompt)
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")