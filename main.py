import os
import requests
import threading
import time


printtofile = open("responses.txt", "a")

url = input("URL OR IP\nhttp://")
url_safe = "http://" + url

def msgmgr(msg_type, content):
    if msg_type == "ERROR":
        return ("[ERROR] " + content)
    elif msg_type == "200":
        return ("[200 OK] " + content)
    elif msg_type == "401":
        return ("[401 UNAUTHORIZED] " + content)
    elif msg_type == "403":
        return ("[403 FORBIDDEN] " + content) 
    elif msg_type == "404":
        return ("[404 NOT FOUND] " + content)

def do_req(url_safe, threadnum):
    
    threadnum = 0
    while True:
        response = requests.get(url_safe)
        if response.status_code == 200:
            print(msgmgr("200", ("[" + url_safe + "]")))
        elif response.status_code == 401:
            print(msgmgr("401", ("[" + url_safe + "]")))
        elif response.status_code == 403:
            print(msgmgr("403", ("[" + url_safe + "]")))
        elif response.status_code == 404:
            print(msgmgr("404", ("[" + url_safe + "]")))
        else:
            print("[THREAD ERROR] Exiting")
            time.sleep(0.3)
            exit()
    

do_req(url_safe, 1)

