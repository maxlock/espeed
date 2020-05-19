from machine import Pin
import utime
import micropython
micropython.alloc_emergency_exception_buf(100)

class Lane:
    def __init__(self,laneNumber,lanePin):
        self.laneNumber = laneNumber
        self.lanePin = lanePin
        self.lapTimestamp = 0
        self.lastLapTimestamp = 0
        self.lapComplete = False
        self.gpio = Pin(self.lanePin, Pin.IN, Pin.PULL_UP)
        self.gpio.irq(trigger=Pin.IRQ_FALLING,handler=self.handler,hard=True)
        print("initialised lane",self.laneNumber,"on pin",self.lanePin)
    
    def handler(self,t):
        now = utime.ticks_us()
        if utime.ticks_diff(now,self.lapTimestamp) > 5e5:
            if self.lapTimestamp == 0:
                self.lastLapTimestamp = now
                self.lapTimestamp = now
            else:
                self.lastLapTimestamp = self.lapTimestamp
                self.lapTimestamp = now
                self.lapComplete = True

    def lapTime(self):
        if (self.lapTimestamp-self.lastLapTimestamp) > 0:
            return (self.lapTimestamp-self.lastLapTimestamp)/1e6
        else:
            return ((1073741824-self.lapTimestamp)+self.lastLapTimestamp)/1e6

    def isLapBegun(self):
        if self.lapTimestamp == 0:
            return False
        else:
            return True

    def isLapComplete(self):
        if self.lapComplete:
            self.lapComplete = False
            return True

    def reset(self):
        self.lapTimestamp = 0
        self.lastLapTimestamp = 0
        self.lapComplete = False

    def number(self):
        return self.laneNumber
