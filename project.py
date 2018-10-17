from urllib.request import urlretrieve
import re


URL_PATH= 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)