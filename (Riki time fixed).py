import datetime
import os
import time
# hosts path for windows (uncomment the code according to your system)
hostsPath = "C:\Windows\System32\drivers\etc\hosts"

# #hosts path for linux/mac (uncomment the code according to your system)
# hostspath = "/etc/hosts"

localRedirect = "127.0.0.1"

#list for websites
webLists = [];

#this is done out of the function so that their values won't restart time value once time.sleep is done on the main func.
#ask user for time interval in minutes to block the websites 
while True:
    try:
        interval = int(input("How long are the websites going to be blocked (in minutes): "))
        break
    except ValueError:
        print("Invalid input. Enter a valid time interval in minutes.")

start_time = datetime.datetime.now()
current_time = ""
# how many minutes from the current time is the end time
unblock_time = start_time + datetime.timedelta(minutes=interval)

#This is just a variable to make sure that the function of inputting a list again does not go back while waiting for time
doneInputting = False;

def webBlock():

        while True:
            global doneInputting
            current_time = datetime.datetime.now()
            if current_time < unblock_time and doneInputting == False:
                pass
            #ask for input before the while loop occurs
                while True:
                    toBlock = input("Type in the website url to block. EX.(www.google.com): ")

                    if toBlock != "exit":
                        webLists.append(toBlock)
                    else: 
                        break

                #While True loop for overall --
                while True:
                    doneInputting = True;
                    print("block sites @ ", current_time)
                    #opening the file using append + read mode
                    with open (hostsPath, 'a+') as f:
                        f.seek(0)
                        fileContent = f.read()
                        #code to avoid duplication
                        for web in webLists:
                            if web in fileContent:
                                print(web + " is already listed.")
                                #pass is removed here, tests if naa jd siyay pulos last time
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
                    break
 
            elif current_time < unblock_time and doneInputting == True:
                print("Blocking time is still on. (prints every 10 secs)")
            elif current_time >= unblock_time and doneInputting == True:
                print("BLOCK TIME PASSED. ALL SITES UNBLOCKED.")
                with open (hostsPath, 'r+') as f:
                    lines = f.readlines()
                    f.seek(0)
                    for line in lines:
                        #statement to know if there are no words in the line that belong to the weblists, 
                        # because if there are none found, the line would be written back to the hostfile, and not removed
                        if not any(web in line for web in webLists):
                            f.write(line)
                    #cuts of all lines that were not written in line 72
                    f.truncate()
                break
            time.sleep(10)


        # else:
        #     print("unblock sites")
        #     with open (hostsPath, 'r+') as f:
        #         lines = f.readlines()
        #         f.seek(0)
        #         for line in lines:
        #             #statement to know if there are no words in the line that belong to the weblists, 
        #             # because if there are none found, the line would be written back to the hostfile, and not removed
        #             if not any(web in line for web in webLists):
        #                 f.write(line)
        #         #cuts of all lines that were not written in line 72
        #         f.truncate()
        #     break
        # time.sleep(10)


#main function
if __name__ == "__main__":
    print(start_time)
    webBlock()

        
