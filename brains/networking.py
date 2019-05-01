"""Alt netvaerks- og kommunikationsrelateret"""

import threading
import socket
import time
import json

#msg1 = createCmd("motor1", "set", 30)
#msg2 = createCmd("motor2", "set", 40)
#msg3 = createCmd("motor2", "set", 40)
#messages = 
msgid = 0
#tcp threading
class networkThread(threading.Thread):
    def __init__(self, threadID, name, s):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.s = s
    def run(self):
      with self.s:
          while True:
              
              msg1 = createCmd("motor1", "set", 2)
              #msg = input(":")
              time.sleep(2)
              #test af afsending af kommandoer
              jsonmsg = json.JSONEncoder().encode(msg1)
              self.s.sendall(jsonmsg.encode())
              data = self.s.recv(1024)
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
            print("Error: ")
            print(msg)
            print("Problem creating TCP socket")
            continue
        try:
            s.connect(sa)
        except OSError as msg:
            s.close()
            s = None
            print(msg)
            continue
        break
    return s
