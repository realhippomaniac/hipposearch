#!/usr/bin/python
import os,sys
os.system("clear")
print("[#] Welcome to hippodns [#]")
def prompt():
 try:
    ah = raw_input("hippo@1337tools~$: ")
    if "help" in ah[0:]:
        print("help: brings this window")
        print("asn: asn lookup")
        print("shodan: searches shodan with a specified query")
        print("feirce: searches subdomains")
        print("portscan: nmaps with default scripts and version")

        prompt()
       elif "shodan" in ah[0:]:
        print("[+] Searching Shodan [+]")
        print("+-+-+-+-+-+-+-+-+-+-+-+")
        shodan(ah)
        print("+-+-+-+-+-+-+-+-+-+-+-+\n")
        prompt()
    elif "asn" in ah[0:]:
        asnlookup(ah)
        prompt()
    elif "quit" in ah or "q" in ah:
        quit()
    elif "nmap" in ah[0:]:
        portscan(ah)
        prompt()
    elif "fierce" in ah:
        fierce(ah)
        prompt()
    elif "clear" in ah[0:]:
        os.system("clear")
        prompt()
    else: 
        prompt()
 except KeyboardInterrupt:
     sys.exit()
 except:
     prompt()
def fierce(ah):
    os.system("fierce -dns %s" % ah[7:])
def portscan(ah):
    os.system("nmap %s -sV -sC -v" % ah[5:])
def shodan(ah):
    os.system("python shodanorgsearch.py %s | sort | uniq -u" % ah[7:])
def asnlookup(ah):
    os.system("python asnlookup.py %s" % ah[4:])
def quit():
    sys.exit()
prompt()
