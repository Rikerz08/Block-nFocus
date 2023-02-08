import datetime
import os
# hosts path for windows (uncomment the code according to your system)
hostsPath = "C:\Windows\System32\drivers\etc\hosts"

# #hosts path for linux/mac (uncomment the code according to your system)
# hostspath = "/etc/hosts"

#storing websites to be blocked
webLists = []

#localhost
localRedirect = "127.0.0.1"

#we set unblock time to placeholding(1 year in minutes) value that is so long just so it's viable for the outer "if conditions" to work
#this is just to make the code run long enough to reach the asking of user input for the minutes
unblock_time = datetime.datetime.now() + datetime.timedelta(minutes=525600)

#This is just a variable to make sure that the function of inputting a list again does not go back while waiting for time to unblock
doneInputting = False;

def timeSet():

    global interval
    global start_time
    global unblock_time
        #ask user for time interval in minutes to block the websites 
    while True:
        try:
            interval = float(input("How long are the websites going to be blocked (in minutes): "))
            break
        except ValueError:
            print("Invalid input. Enter a valid time interval in minutes.")

    #initialization of start and end time are done outside of funtion so that their values will not be altered in each sleep iteration
    start_time = datetime.datetime.now()
    unblock_time = start_time + datetime.timedelta(minutes=interval)      

    print("Proceeding will exit all browsers. Unsaved progress will be lost.")
    killDecision = input("Do you wish to proceed or exit browsers manually? (Y/N) ")

    if killDecision.upper() == "Y":
        os.system("taskkill /im firefox.exe /f")
        os.system("taskkill /im chrome.exe /f")
        os.system("taskkill /im opera.exe /f")
        os.system("taskkill /im msedge.exe /f") 
        os.system("taskkill /im brave.exe /f")
    #upon the very moment of killing the browsers, we need a new current time var to be subtracted by the start time var
    #and we need to add it to the unblock time var to make up for the time that was taken while the user was still inputting data
    inputTime = datetime.datetime.now() - start_time
    #we need to update unblock time to make up for the time taken by user while inputting
    unblock_time += inputTime

def inputSites(siteList):
    global toBlock
    global doneInputting
    while True:
        toBlock = input("Type in the website url to block. EX.(www.google.com): ")
        #if there is white space, validate it
        if " " in toBlock:
            print("Please enter a valid input.")
            continue
        #append also a version without "www." and vice versa
        if toBlock != "exit" and "www." in toBlock:
            siteList.append(toBlock)
            siteList.append(toBlock.replace("www.",""))
        elif toBlock != 'exit' and "www." not in toBlock:
            siteList.append(toBlock)
            siteList.append("www." + toBlock)
        else: 
            break

def writeToHost(siteList):
    #opening the file using append + read mode
    with open (hostsPath, 'a+') as f:
        f.seek(0)
        fileContent = f.read()
        #code to avoid duplication
        for web in siteList:
            if web in fileContent:
                print(web + " is already listed.")
                #pass is removed here, tests if naa jd siyay pulos last time
            else:
                f.write("\n")
                f.write(localRedirect + " " + web)

def unBlock(siteList):
    with open (hostsPath, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            #statement to know if there are no words in the line that belong to the weblists, 
            # because if there are none found, the line would be written back to the hostfile, and not removed
            if not any(web in line for web in siteList):
                f.write(line)
        #cuts of all lines that were not written in line 72
        f.truncate()