#!/usr/bin/python

"""  IDTscan  is a tool written in python for Web-audit and penetration testing .
It scan a host for discover  local and remote files inclusion vulnerabilities  fastly !!

The author isn't responable for all damages caused by tool
Author:Had1x aka H11
licence: GNU GPL V3

Requirements :
-requests module


Installing requests in Debian-based distribution :
sudo apt-get install python-pip
pip install requests

Usage:
./idtscan.py https://www.domain-name.com
 """


import sys
import time
try:
    import requests
except ImportError:
    print ("please install requests module with pip ")
    sys.exit()

if  len(sys.argv) != 2:
    print ("Usage : python IDTscan.py  https://www.domain.com ")
elif len(sys.argv) == 2:
    domain = sys.argv[1]
    include_url = ((domain) + "/index.php?page=https://www.google.com")
    directory_traversal_url = ((domain) + "/index.php?page=.../.../.../.../etc/passwd")
    print ("_____ _____ _______")
    print(" |_    _| __ \__  __| ")
    print (" | | | |  | | | |___  ___ __ _ _ __    ")
    print (" | | | |  | | | / __|/ __/ _` | '_ \ ")                  
    print (" | |_| |__| | | \__ \ (_| (_| | || | ")
    print (" |__ __|____ /|_|___/\___\__,_|_||_| ")
    print ("")
    print ("author: Had1X ")
    time.sleep(2)
    print ("")
    print ("[+] scanning : ",(domain),"...")
    print ("scanning for remote file inclusion  vulnerability ...")
    r = requests.get(include_url)
    if (r.status_code) == (requests.codes.ok):
        time.sleep(2)
        print ("[+] remote file inclusion vulnerability was discovered:\n ",(include_url))
        print ("[+] OWASP docs : https://www.owasp.org/index.php/Testing_for_Remote_File_Inclusion ")
        
        time.sleep(2)
    else:
        print (" [-] remote files inclusion vulnerability was no discovered ")
      
        time.sleep(2)
        print ("")
        print ("scanning host for local file inclusion vulnerability ... ")
        time.sleep(2)
        d  = requests.get(directory_traversal_url)
        if (d.status_code)  == (requests.codes.ok):
           print (" [+] local file inclusion  was discovered :\n",(directory_traversal_url))
           print (" OWASP docs : https://www.owasp.org/index.php/Testing_for_Local_File_Inclusion ")
           
           time.sleep(3)
           
        else:
         print ("[-]local files inclusion vulnerability was no discovered ")
         
         time.sleep(3)
         
                
        

                                      
                                      
