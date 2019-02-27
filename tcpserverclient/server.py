# Echo server program
import socket
import sys
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev.ev3 import *


HOST = None               # Symbolic name meaning all available interfaces
PORT = 5000              # Arbitrary non-privileged port
s = None
lcd = Screen()
lcd.clear()
sound = Sound()
ultra = UltrasonicSensor()
ultra.mode = 'US-DIST-CM'

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
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:       
        data = conn.recv(1024)
        lcd.clear() 
        lcd.draw.text((10, 5), data)
        sound.speak()
        lcd.update()
        conn.send(b'OK')
        print(ultra.value())
        #conn.send(bytes[ultra.value()])
        #if not data: break
      