from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import random
import sys

package = 'com.duokan.reader'
activity = 'com.duokan.reader.DkReaderActivity'
runComponent = package + '/' + activity

MIN_X=20
MAX_X=300
MIN_Y=80
MAX_Y=350

WAITTIME = 10
DEBUG = False

print "Wait For connection..."
if DEBUG == True:
    device = MonkeyRunner.waitForConnection()
    WAITTIME = 5
else:
    WAITTIME = 8
    device = MonkeyRunner.waitForConnection(300, sys.argv[1])

print "Connected."
device.startActivity(component=runComponent)

MonkeyRunner.sleep(WAITTIME * 2)

device.touch(175, 394, 'DOWN_AND_UP')
MonkeyRunner.sleep(WAITTIME)

device.touch(88, 394, 'DOWN_AND_UP')
MonkeyRunner.sleep(WAITTIME)

if random.randint(0, 1) % 2 == 0:
    if random.randint(0, 1) % 2 == 0:
        device.touch(52, 326, 'DOWN_AND_UP')
        MonkeyRunner.sleep(WAITTIME)
    else:
        device.touch(150, 340, 'DOWN_AND_UP')
        MonkeyRunner.sleep(WAITTIME)

for i in range(0, 25):
    device.drag((300, 240), (60, 240))
    MonkeyRunner.sleep(WAITTIME)
    
device.touch(79, 459, 'DOWN_AND_UP')
MonkeyRunner.sleep(WAITTIME)

device.touch(245, 405, 'DOWN_AND_UP')
MonkeyRunner.sleep(WAITTIME)
start_time = time.time()
print "Current time:" + str(start_time)

end_time = start_time + 60

while time.time() < end_time:
    if random.randint(0, 1) % 2 == 0:
        x1 = random.randint(MIN_X, MAX_X)
        y1 = random.randint(MIN_Y, MAX_Y)
        x2 = random.randint(MIN_X, MAX_X)
        y2 = random.randint(MIN_Y, MAX_Y)
        device.drag((x1, y1), (x2, y2))
        print "Monkey drag from (" + str(x1) + ", " + str(y1) + ") to (" + str(x2) + ", " + str(y2) + ")"
    if random.randint(0, 1) % 2 == 0:
        x = random.randint(MIN_X, MAX_X)
        y = random.randint(MIN_Y, MAX_Y)
        device.touch(x, y, 'DOWN')
        MonkeyRunner.sleep(2)
        device.touch(x, y, 'UP')
        print "Monkey touch in (" + str(x) + ", " + str(y) + ")"
    if random.randint(0, 5) % 5 == 0:
        device.touch(87, 468, 'DOWN_AND_UP')
        print "go back"
    print "Remain time: " + (str(end_time - time.time()))
    MonkeyRunner.sleep(WAITTIME)
print "Monkey success."
'''

device.drag((300,240),(20,240))

MonkeyRunner.sleep(WAITTIME)

start_time = time.time()
print "Current time:" + str(start_time)

end_time = start_time + 300

while time.time() < end_time:
    if random.randint(0, 1) % 2 == 0:
        x1 = random.randint(MIN_X, MAX_X)
        y1 = random.randint(MIN_Y, MAX_Y)
        x2 = random.randint(MIN_X, MAX_X)
        y2 = random.randint(MIN_Y, MAX_Y)
        device.drag((x1, y1), (x2, y2))
        print "Monkey drag from (" + str(x1) + ", " + str(y1) + ") to (" + str(x2) + ", " + str(y2) + ")"
    if random.randint(0, 1) % 2 == 0:
        x = random.randint(MIN_X, MAX_X)
        y = random.randint(MIN_Y, MAX_Y)
        device.touch(x, y, 'DOWN')
        MonkeyRunner.sleep(2)
        device.touch(x, y, 'UP')
        print "Monkey touch in (" + str(x) + ", " + str(y) + ")"
    print "Remain time: " + (str(end_time - time.time()))
    MonkeyRunner.sleep(WAITTIME)
print "Monkey success."
'''