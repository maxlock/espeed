#import wifimgr
import uselect,usocket
#from lane import Lane

#wlan = wifimgr.get_connection()
#if wlan is None:
#    print("Could not initialize the network connection.")
#    while True:
#        pass

server = usocket.socket()
addr = usocket.getaddrinfo('0.0.0.0', 8266)[0][-1]
server.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
server.bind(addr)
server.listen(1)
server.setblocking(0)

poll = uselect.poll()
poll.register(server, uselect.POLLIN)
sockets = {}
sockets[server.fileno()] = server

#for laneNumber,lanePin in enumerate(req):
#    lanes.append(Lane(int(laneNumber),int(lanePin)))

#    for alane in lanes:
#        if alane.isLapComplete():
#            print(alane.number(),alane.lapTime())
#            conn.sendall(str(alane.number())+','+str(alane.lapTime())+'\n')

def doCommand(data):
    print(data)
    return(b'hello')

while True:
    for fd, event in poll.poll():

        if event == uselect.POLLIN:
            if fd.fileno() == server.fileno():
                client, addr = server.accept()
                poll.register(client, uselect.POLLIN)
                sockets[client.fileno()] = client
                client.send(b"espeed lane node\r\n")
            else:
                client = sockets[fd.fileno()]
                data = client.readline()
                if len(data) == 0 or data == b'disclientnect':
                    poll.modify(client, uselect.POLLOUT)
                else:
                    client.send(doCommand(data))

        elif event == uselect.POLLOUT:
            client = sockets[fd.fileno()]
            sockets.pop(fd.fileno())
            client.send(b"goodbye!")
            poll.unregister(client)
            client.close()


