import datetime
import os

# hosts path for windows (uncomment the code according to your system)
hostsPath = "C:\Windows\System32\drivers\etc\hosts"

# #hosts path for linux/mac (uncomment the code according to your system)
# hostspath = "/etc/hosts"

localRedirect = "127.0.0.1"

#list for websites
webLists = [];

#ask user input for website to block
while True:
    toBlock = input("Type in the website url to block. EX.(www.google.com): ")

    if toBlock == "exit":
        break;

    webLists.append(toBlock)
    
# ask user for time interval in minutes to block the websites 
while True:
    try:
        interval = int(input("Enter the time interval in minutes to block the websites: "))
        break
    except ValueError:
        print("Invalid input. Enter a valid time interval in minutes.")

# get the current time and add the time interval to it
current_time = datetime.datetime.now()
unblock_time = current_time + datetime.timedelta(minutes=interval)

#opening the file using append + read mode
with open (hostsPath, 'a+') as f:
    f.seek(0)
    fileContent = f.read()
    #code to avoid duplication
    for web in webLists:
        if web in fileContent:
            print(web + " is already listed.")
            pass
        else:
            f.write("\n")
            f.write(localRedirect + " " + web)

print("Proceeding will exit all browsers. Unsaved progress will be lost.")
killDecision = input("Do you wish to proceed or exit browsers manually? (Y/N) ")

if killDecision.upper() == "Y":
    os.system("taskkill /im firefox.exe /f")
    os.system("taskkill /im chrome.exe /f")
    os.system("taskkill /im opera.exe /f")
    os.system("taskkill /im msedge.exe /f")


with open (hostsPath, 'r') as f:
    print(f.read())
    