import wifimgr
import usocket
from lane import Lane

wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass

addr = usocket.getaddrinfo('0.0.0.0', 8266)[0][-1]
server = usocket.socket()
server.bind(addr)
server.setblocking(0)
server.listen(1)
(socket,sockaddr) = server.accept()

print('listening')
lanes = []

#for laneNumber,lanePin in enumerate(req):
#    lanes.append(Lane(int(laneNumber),int(lanePin)))

while True:
    d = socket.readline()
    print(str(d))

#    for alane in lanes:
#        if alane.isLapComplete():
#            print(alane.number(),alane.lapTime())
#            conn.sendall(str(alane.number())+','+str(alane.lapTime())+'\n')

#conn.close()
