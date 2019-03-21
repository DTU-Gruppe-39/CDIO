#Kode der skal køre på ev3
#Fungere som en server hvor "brains" kan forbinde til
#Klienten "brains" sender kommandoer til serveren(ev3) og
#de bliver tilføjet en liste.
#Det er et dictionary der indeholder felterne:
#cmdid - et unikt id for hver ny kommando
#cmdtype - get/set/custom - skal en sensor aflæses eller en motor startes.
#cmdname - en bestemt motor, sensor eller lignende
#cmdstate - init, running, done - hvilken state kommandoen er i - er motor f.eks. i gang at køre
#
#TODO:
#cmdHandler skal bindes til ev3dev's objekter

import sys
import json
import socket

HOST = None
PORT = 6000

actionslist = []


def cmdHandler(cmd):
    #hvis det er en sensorvalue der skal læses
    if cmd["cmdtype"] == "get":
        #her skal være kode til handle
        pass
    #hvis det er en motor der skal sættes i gang
    elif cmd['cmdtype'] == "set":
        pass
    #custom commands - hvis vi har en bestemt
    #handling der bare skal hardcodes.
    elif cmd['cmdtype'] == "custom":
        pass


def tcpServer(PORT, s):

    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                                  socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except OSError as msg:
            s = None
            continue
        try:
            s.bind(sa)
            s.listen(1)
        except OSError as msg:
            s.close()
            continue
        break
    return(s)

def queueAction(msg):
    actionslist.append(msg)





def main():
    s = None

    sockettcp = tcpServer(PORT, s)
    if sockettcp == None:
        print("Could not open socket on port: ", PORT)
        sys.exit(1)
    else:
        print(sockettcp)

    while True:
    #    laver socket der er klar til at modtage forbindelse
        print("Waiting for client")
        conn, addr = sockettcp.accept()
        #with conn:
        print(addr, "connected")
        while True:
            try:
                data = conn.recv(1024)
                if data.decode() == "bye":
                    print("Client disconnected")
                    break
                else:
                    msg = json.loads(data)
                    conn.send(b'OK')
                    queueAction(msg)
                    for i in actionslist:
                        print("cmdId:", i['id'], "cmdtype:", i['cmdtype'], "cmdname:", i['cmdname'], "cmdstate:", i['cmdstate'])
                    if not data: break
            except:
                print("Client disconnected")
                break




if __name__ == "__main__":
    main()
