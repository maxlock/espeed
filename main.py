from machine import Pin
import utime
import wifimgr
import lane
import micropython
micropython.alloc_emergency_exception_buf(100)

wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D


lanePins = [4,5]

lanes = []
for laneNumber,lanePin in enumerate(lanePins):
    lanes.append(Lane(laneNumber,lanePin))

while True:
    for lane in lanes:
        if lane.isLapBegun:
            if lane.isLapComplete():
                print(lane.number(),lane.lapTime()/1e6)
