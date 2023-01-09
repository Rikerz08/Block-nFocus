# storing absolute directory of hosts file to a path var
hostspath = "C:\Windows\System32\drivers\etc\hosts"

#list for websites
webLists = [];

#ask user input for website to block
while True:
    toBlock = input("Type in the website url to block. EX.(www.google.com): ")

    if toBlock == "exit":
        break;

    webLists.append("127.0.0.1 " + toBlock)

#opening the file using append + read mode
with open (hostspath, 'a') as f:
    f.write("\n")
    f.write('\n'.join(webLists))

with open (hostspath, 'r') as f:
    print(f.read())
    
    