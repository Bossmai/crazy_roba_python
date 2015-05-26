from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import random
import sys

package = 'com.tencent.android.qqdownloader'
activity = 'com.tencent.assistant.activity.SplashActivity'
runComponent = package + '/' + activity

MIN_X=20
MAX_X=300
MIN_Y=80
MAX_Y=400

WAITTIME = 10

print "Wait For connection..."
device = MonkeyRunner.waitForConnection()
#device = MonkeyRunner.waitForConnection(300, sys.argv[1])

print "Connected."
device.startActivity(component=runComponent)

MonkeyRunner.sleep(WAITTIME * 5)


device.touch(276, 48, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME)

device.touch(160, 93, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME)

device.touch(155, 280, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME)

device.touch(273, 108, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME)




start_time = time.time()
print "Current time:" + str(start_time)

end_time = start_time + 600


while time.time() < end_time:
    device.touch(221, 303, 'DOWN_AND_UP')

    MonkeyRunner.sleep(WAITTIME * 2)
    
    device.touch(80, 458, 'DOWN_AND_UP')

    MonkeyRunner.sleep(WAITTIME * 2)
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