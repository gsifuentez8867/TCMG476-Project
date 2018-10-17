from urllib.request import urlretrieve
import re
from datetime import datetime


URL_PATH= 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)


ERRORS = []

regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
unsuccess= re.compile("4[0-9][0-9]")
redirect= re.compile("3[0-9][0-9]")

date_format= "%d/%b/%Y"
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
	if numrequest==0:
		firstdate=datetime.strptime(parts[1],date_format)	
	numrequest+=1
	if unsuccess.match(parts[6]):
		numbad+=1
	if redirect.match(parts[6]):
		numredirect+=1	
	if parts[4] in filenames:
		filenames[parts[4]]+=1
	else:
		filenames[parts[4]]=1	
		
lastdate=datetime.strptime(parts[1],date_format)

fileparse.close()




answers=open("answers.txt","w+")
#total requests

answers.write("The total number of requests is: "+str(numrequest)+" .") 



#average per day, week, month

answers.write("The average number of requests per day was "+ str(numrequest/(lastdate-firstdate).days)+"."+"\n")
answers.write("The average number of requests per week was "+str((numrequest/(lastdate-firstdate).days)*7)+"."+"\n")
answers.write("The average number of requests per day was "+str((numrequest/(lastdate-firstdate).days)*30)+"."+"\n")


#not successful

answers.write("The percentage of total requests that were unsuccessful is: " +str(round((numbad/numrequest)*100))+ "%."+"\n")

#redirected

answers.write("The percentage of total requests that were redirected is: " +str(round((numredirect/numrequest)*100))+"%."+"\n")

#most and least requested file

mostreq=""
leastreq=""
mostint=0
leastint=numrequest
listleastreq=[]

for key,value in filenames.items():
	if value > mostint:
		mostint=value
		mostreq=key
	if value < leastint:
		leastint=value

for key,value in filenames.items():
	if value == leastint:
		listleastreq.append(key)

answers.write("The most requested file was "+str(mostreq)+"."+"\n")
answers.write("The least requested files are listed below all being requested "+str(leastint)+" time."+"\n")
for item in listleastreq:
	answers.write(item +"   ")