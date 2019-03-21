#Kode der skal køre på maskine med webcam forbundet
#TODO:
#OpenCV kode
#MEGET

import sys
import time
import json
import os
import threading
import vision
import networking


#Hvis server og klient skal køre på samme maskine
HOST = "127.0.0.1"
PORT = 6000

ballarray = []



#print('Received', repr(data))



def main():

    try:
        tcpclient = networking.tcpClient(HOST, PORT)
        if tcpclient == None:
            print("Could not connect")
            sys.exit(1)
        else:
            tcpthread = networking.networkThread(1, "tcp socket", tcpclient)
            #visionthread = vision.visionThread(1, "vision")
            tcpthread.start()
            vision.imageCapture(ballarray)
        #    visionthread.start()
        #    visionthread.start()
            while True:
                vision.imageCapture(ballarray)
                #get key
    except KeyboardInterrupt:
        print("Exiting..")
        #tcpclient.sendall("bye".encode()
        tcpclient.close()
        time.sleep(1)
        sys.exit(0)




if __name__ == "__main__":

    main()
