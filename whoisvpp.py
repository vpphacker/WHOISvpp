#!/usr/bin/python
import os
import sys
import time

# You Don't become a coder by changing credits #

print("\033[95m     ")
os.system("clear")

os.system('figlet Whois VPP')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)
print("\033[93m+---------------------------------------------+")
slowprint("| coded by:VPP Hacker                         |")
slowprint("| Date : 24/06/2019                           |")
slowprint("| Contact Me on Instagram : VPP Hacker        |")
slowprint("| Subscribe My YouTube Channel : VPP Hacker   |")
slowprint("|                   ^_^                       |")
print("+---------------------------------------------+")

print('''\033[96m
[01] Start Whois
[02] Exit
''')
z = input("\033[96mEnter What You Want : ")

if (z == 1) :
             os.system("clear")
             def slowprint(s):
                 for c in s + '\n':
                     sys.stdout.write(c)
                     sys.stdout.flush()
                     time.sleep(6. / 100)
             slowprint("[!] Loading Whois Server............................")
             time.sleep(4)
             os.system("clear")
             os.system("figlet WHOISVPP")
             print("\033[93m+----------------------------------------------+")
             slowprint("|      Now  Enter ip or website like           |")
             slowprint("|        127.0.0.1 or example.com              |")
             print("+----------------------------------------------+")
             print("          ")
             ip = raw_input("# Enter Ip or Domain : ")
             print("\033[96m+----------------------------------------+")
             os.system("whois %s" % (ip))
             print("\033[92m+-----------------------------------+")
             print("| Support Us By Subscribing Channel |")
             print("+-----------------------------------+")
             sys.exit()
if (z == 2) :
             print("See You Next Time")
             print("If You Want Hacking Tutorial Then visit my channel")
             sys.exit()
else :print ("\n[!] ERROR : Enter Valid Number")

