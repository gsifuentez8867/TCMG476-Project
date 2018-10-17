from urllib.request import urlretrieve
import re


URL_PATH= 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)


ERRORS = []

regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")


fileparse= open(LOCAL_FILE)
for line in fileparse:
	current=fileparse.readline()
	parts= regex.split(current)
	if len(parts) < 7:
		continue
		
		numrequest+=1
		
		
fileparse.close()