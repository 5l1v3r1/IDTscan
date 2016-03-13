
"""  IDTscan(Include and Directory Traversal scanner ) is a script written in python for Web-audit and penetration testing .
It scan a host for discover  include and directory traversal vulnerabilities  fastly !!

The author isn't responable for all damages caused by script
Author:Had1x aka H11
licence: GNU GPL V3

Requirements :
-requests module
-python version + 3.0

Installing requests in Debian-based distribution :
sudo apt-get install python-pip
pip install requests

Usage:
python IDTscan.py https://www.domain-name.com
./IDTscan.py https://www.domain-name.com  """


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
    print ("scanning for include vulnerability ...")
    r = requests.get(include_url)
    if (r.status_code) == (requests.codes.ok):
        time.sleep(2)
        print ("[+] include vulnerability was discovered:\n ",(include_url))
        include_vuln = True
        time.sleep(2)
    else:
        print (" [-] include vulnerability was no discovered ")
        include_vuln = False
        time.sleep(2)
        print ("")
        print (" scanning host for directory traversal  vulnerability ... ")
        time.sleep(2)
        d  = requests.get(directory_traversal_url)
        if (d.status_code)  == (requests.codes.ok):
           print (" [+] directory traversal vulnerability was discovered :\n",(directory_traversal_url))
           dir_trav_vuln = True
           time.sleep(3)
           print ("")
        else:
         print ("[-]directory traversal vulnerability was no discovered ")
         dir_trav_vuln = False
         time.sleep(3)
         print ("")

    if (include_vuln) == True and (dir_trav_vuln) == True :
        print ("[*] host : ",(domain))
        print ("[+]Include vulnerability : Yes ")
        print  ("[+]Directory traversal vulnerability :  Yes ")
        time.sleep(3)
        sys.exit()
    elif (include_vuln) == False  and (dir_trav_vuln) ==  False :
        print ("[*]host ",(domain))
        print ("[-]Include vulnerability : No ")
        print  ("[-]Directory traversal vulnerability : No ")
        time.sleep(3)
        sys.exit()
    elif (include_vuln)  == True and (dir_trav_vuln) == False :
        print ("[*] host ",(domain))
        print ("[+]Include vulnerability : Yes ")
        print ("[-]Directory traversal : No ")
        time.sleep(3)
        sys.exit()
    else:
        print ("host : ",(domain))
        print ("[-]Include vulnerability : No ")
        print ("")
        print ("[+]Directory traversal vulnerabilty : Yes")
        print (" page : ",(directory_traversal_url))
        time.sleep(3)
        sys.exit()
                
        

                                      
                                      
