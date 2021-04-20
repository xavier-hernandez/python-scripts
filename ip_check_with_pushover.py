import requests
import os.path
from chump import Application
from os import path
from IPy import IP

AppToken = "PUSHOVER_APP_TOKEN"
UserKey = "PUSHOVER_USER_KEY"
currentIpFile = "/root/current_public_ip.txt"
request_ip = requests.get("https://www.whatismyip.biz/external_ip.php").text

def getOldIP(ip):    
    if path.isfile(currentIpFile):
        f = open(currentIpFile, "rt")
        old_ip = f.read()
        f.close()
    else:
        f = open(currentIpFile, "w")
        f.write(ip)
        f.close()
    return old_ip

def storeCurrentIP(ip):
    f = open(currentIpFile, "w")
    f.write(public_ip)
    f.close()

try:
    #try and parse result, is it an IP address?
    IP(request_ip)
    public_ip = request_ip
except:
    print("no IP address retrieved") 
    public_ip = "127.0.0.1"

old_ip = getOldIP(public_ip)

if old_ip != public_ip:
    app = Application(AppToken)
    user = app.get_user(UserKey)
    message = user.create_message(title="IP Change", message="new IP address {}".format(public_ip), priority=1)
    message.send()
    storeCurrentIP(public_ip)


