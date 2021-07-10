import re
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
url = str.strip(sys.argv[-1])
newfile=url+"\n"
count=0
stream = os.popen('echo '+url+' | ~/go/bin/hakrawler | grep '+url)
output = stream.read()
f = open(dir_path+"/urls.txt", "w")
f.write(output)
f.close()
with open(dir_path+"/urls.txt", 'r') as f:
    for line in f:
        line=line.replace("[href]","")
        line=line.replace("[form]","")
        if str.strip(line) in newfile:
            pass
        else:
            newfile=newfile+str.strip(line)+"\n"
            count=count+1
            stream = os.popen('x8 -u "'+str.strip(line)+'" -w wordlist.txt -o output/out'+str(count)+'.txt')
            output = stream.read()


f = open(dir_path+"/urls.txt", "w")
f.write(newfile)
f.close()
print("Completed!!\nCheck urls.txt file and output folder for x8 results\n")
stream=os.popen('tail -n +1 output/*')
output=stream.read()
print(str(output))