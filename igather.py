#!/usr/bin/env python

from urllib2 import *
from colorama import *
from sys import *
from time import *
from os import *

tme = strftime("%S:%M:%H")

system("clear")

def banner():
    print "\033[1;36m$ \033[1;32mInformation Gathering By GhostDecoded"
    print
def banner():
    print "\033[1;36m$ \033[1;32mkunjungi www.androhackerz81.zone.id"
    print

    
    
def whois():
    url = "http://api.hackertarget.com/whois/?q=" +target
    data = urlopen(url).read()
    print "\033[1;36m[ # ] WHOIS >>>\033[1;32m\n",data
    print
    
def nmap():
    url = "http://api.hackertarget.com/nmap/?q=" +target
    data = urlopen(url).read()
    print "\033[1;36m[ # ] NMAP >>>\033[1;32m\n",data
    print
    
def geoip():
    url = "http://api.hackertarget.com/geoip/?q=" +target
    data = urlopen(url).read()
    print "\033[1;36m[ # ] GEOIP >>>\033[1;32m\n",data
    print
  
def zone():
    url = "http://api.hackertarget.com/zonetransfer/?q=" +target
    data = urlopen(url).read()
    print "\033[1;36m[ # ] ZONE TRANSFER >>>\033[1;32m\n",data
    print

def reverse():
    url = "http://api.hackertarget.com/reverseiplookup/?q=" +target
    data = urlopen(url).read()
    print "\033[1;36m[ # ] REVERSE IP LOOKUP >>>\033[1;32m\n",data
    print 
    
def dns():
    url = "http://api.hackertarget.com/dnslookup/?q=" +target
    data = urlopen(url).read()
    print "\033[1;36m[ # ] DNS LOOKUP >>>\033[1;32m\n",data
    print
    
def sub():
    url = "http://api.hackertarget.com/subnetcalc/?q=" +target
    data = urlopen(url).read()
    print "\033[1;36m[ # ] SUBNET CALCULATE >>>\033[1;32m\n",data
    print
    
def head():
    url = "http://api.hackertarget.com/httpheaders/?q=" +target
    data = urlopen(url).read()
    print "\033[1;36m[ # ] HTTP HEADERS >>>\033[1;32m\n",data
    print
    
def host():
    url = "http://api.hackertarget.com/hostsearch/?q=" +target
    data = urlopen(url).read()
    print "\033[1;36m[ # ] HOST SEARCH >>>\033[1;32m\n",data
    print
    
##########################################Fuck You##############   

banner()
print
target = raw_input("Enter Your Host Target Or Ip : ")
print
print "\033[1;36m[+] \033[0mStarting At [ %s ]" % tme
print "\033[1;36m[*] \033[0mPlease Wait..."
sleep(4)
print

##############################Result######################

whois()
nmap()
geoip()  
zone()
reverse() 
dns()
sub()
head()
host()
##############################Holy Shit###################