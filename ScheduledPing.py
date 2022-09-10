import os
from time import sleep

class ScheduledPing:
    pingData = [{}]


def runPingCheck():
    while True:
        os.system('ping 208.67.222.222 >> pingData.txt')
        convertPingData()
        sleep(60)

def convertPingData():
    print('converting')
    file = open('pingData.txt')
    for line in file:
        os.system('echo' + line)
        print('converting')
    return

runPingCheck()