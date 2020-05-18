import wifimgr
from lane import Lane

wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass

lanePins = [4,5]

lanes = []
for laneNumber,lanePin in enumerate(lanePins):
    lanes.append(Lane(laneNumber,lanePin))

while True:
    for alane in lanes:
        if alane.isLapBegun:
            if alane.isLapComplete():
                print(alane.number(),alane.lapTime()/1e6)
