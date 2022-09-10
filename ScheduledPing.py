import os
from datetime import datetime, timedelta
from time import sleep

class ScheduledPing:
    pingData = [{}]


def runPingCheck():
    runTimer = float(input("Run job for (in minutes): "))
    startTime = datetime.today()
    while datetime.today() < (startTime + timedelta(minutes=runTimer)):
        os.system('ping 208.67.222.222 >> pingData.txt')
        convertPingData()
        sleep(1)

def convertPingData():
    file = open('pingData.txt')
    for line in file:
        os.system('echo ' + line)
        if "Packets: " in line:
         os.system('echo ' + line)
    return

runPingCheck()