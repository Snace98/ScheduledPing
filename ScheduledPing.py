import os
from datetime import datetime, timedelta
from time import sleep

from generateHtml import generateHtml

pingData = {
    'packets': [],
    'minimum': [],
    'maximum': [],
    'average': []
}

def runPingCheck():
    runTimer = float(input("Run job for (in minutes): "))
    startTime = datetime.today()
    while datetime.today() < (startTime + timedelta(minutes=runTimer)):
        os.system('ping 208.67.222.222 >> pingData.txt')
        sleep(5)
    convertPingData()
    generateHtml(pingData)

def convertPingData():
    file = open('pingData.txt')
    for line in file:
        if "Packets: " in line:
         pingData['packets'].append(line)
        if "Minimum" in line:
            minMaxAvg(line)

    os.system('echo ' + debugHelper('packets', ''))
    os.system('echo ' + debugHelper('minimum', ''))
    os.system('echo ' + debugHelper('maximum', ''))
    os.system('echo ' + debugHelper('average', ''))
    return

def minMaxAvg(line):
    minMaxAvgArr = line.split(',')
    pingData['minimum'].append(minMaxAvgArr[0])
    pingData['maximum'].append(minMaxAvgArr[1])
    pingData['average'].append(minMaxAvgArr[2])

    

def debugHelper(prop, myString):
    for x in pingData[prop]:
        myString += x
    return myString

runPingCheck()