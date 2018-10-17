from urllib.request import urlretrieve
import re


URL_PATH= 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)


ERRORS = []

regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
unsuccess= re.compile("4[0-9][0-9]")
redirect= re.compile("3[0-9][0-9]")

filenames = {}

numrequest=0
numbad=0
numredirect=0


fileparse= open(LOCAL_FILE)
for line in fileparse:
	current=fileparse.readline()
	parts= regex.split(current)
	if len(parts) < 7:
		continue
		
		numrequest+=1
	if unsuccess.match(parts[6]):
		numbad+=1
	if redirect.match(parts[6]):
		numredirect+=1	
	if parts[4] in filenames:
		filenames[parts[4]]+=1
	else:
		filenames[parts[4]]=1	
fileparse.close()




answers=open("answers.txt","w+")
#total requests

answers.write("The total number of requests is: "+str(numrequest)+" .") 



#average per day, week, month



#not successful

answers.write("The percentage of total requests that were unsuccessful is: " +str(round((numbad/numrequest)*100))+ "%."+"\n")

#redirected

answers.write("The percentage of total requests that were redirected is: " +str(round((numredirect/numrequest)*100))+"%."+"\n")

#most and least requested file