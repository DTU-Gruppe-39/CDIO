#Kode der skal køre på maskine med webcam forbundet
#TODO:
#OpenCV kode
#MEGET

import socket
import sys
import time
import json
import os
import threading

msgid = 0
#Hvis server og klient skal køre på samme maskine
HOST = "127.0.0.1"
PORT = 6000
BTNDELAY = 0.2


#tcp threading
class networkThread(threading.Thread):
   def __init__(self, threadID, name, s):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

      with s:
          while True:
              #msg = input(":")
              time.sleep(2)
              msg1 = createCmd("driveleft", "set", "motor")
              jsonmsg = json.JSONEncoder().encode(msg1)
              s.sendall(jsonmsg.encode())
              data = s.recv(1024)
              print(data)



#funktion der returnere kommando
def createCmd(cmdname, cmdtype, cmdvalue=None, cmdstate="init"):
    #global
    global msgid
    msgid +=1
    message = {
        "id": msgid,
    "cmdname": cmdname,
    "cmdtype": cmdtype,
    "cmdvalue": cmdvalue,
    "cmdstate": cmdstate
    }

    return message


def tcpClient(dstHOST, dstPORT):
    HOST = dstHOST    # The remote host
    PORT = dstPORT    # The same port as used by the server
    s = None
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except OSError as msg:
            s = None
            continue
        try:
            s.connect(sa)
        except OSError as msg:
            s.close()
            s = None
            continue
        break
    return s

#print('Received', repr(data))



def main():
    try:
        tcpclient = tcpClient(HOST, PORT)
        if tcpclient == None:
            print("Could not connect")
            sys.exit(1)
        else:
            tcpthread = networkThread(1, "tcp socket", tcpclient)
            while True:
                time.sleep(2)
                print("Testing threading")
                #get key
                pass
    except KeyboardInterrupt:
        print("Exiting..")
        #tcpclient.sendall("bye".encode()
        tcpclient.close()
        time.sleep(1)
        sys.exit(0)




if __name__ == "__main__":

    main()
