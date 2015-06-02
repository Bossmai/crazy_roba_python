from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import random
import sys
package = 'com.qihoo.haosou'
activity = 'com.qihoo.haosou.activity.SplashActivity'
runComponent = package + '/' + activity

DEBUG = False
TOTAL_DURATION = 300

MIN_X=10
MAX_X=300
MIN_Y=310
MAX_Y=350



print "Wait For connection..."

if DEBUG == True:
    device = MonkeyRunner.waitForConnection()
    WAITTIME = 2
else:
    device = MonkeyRunner.waitForConnection(300, sys.argv[1])
    WAITTIME = 10

print "Connected."
device.startActivity(component=runComponent)

MonkeyRunner.sleep(WAITTIME * 5)


print "Close Start activity."
device.touch(160, 352, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME * 4)

print "Go Into 1st news."
device.touch(111, 332, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME * 4)


for i in range(0, 5):
    print "Drag down."
    device.drag((160, 260), (160, 100))
    MonkeyRunner.sleep(WAITTIME * 2)

print "Go back."
device.touch(81, 456, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME * 4)

print "Go Into 3rd news."
device.touch(232, 339, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME * 4)


for i in range(0, 5):
    print "Drag down."
    device.drag((160, 260), (160, 100))
    MonkeyRunner.sleep(WAITTIME * 2)

print "Go back."
device.touch(81, 456, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME * 4)

print "Start random click."
start_time = time.time()
print "Current time:" + str(start_time)

end_time = start_time + 300

while time.time() < end_time:     
    x = random.randint(MIN_X, MAX_X)
    y = random.randint(MIN_Y, MAX_Y)
    device.touch(x, y, 'DOWN')
    MonkeyRunner.sleep(2)
    device.touch(x, y, 'UP')
    print "Monkey touch in (" + str(x) + ", " + str(y) + ")"
    MonkeyRunner.sleep(WAITTIME * 2)    
        
    x1 = random.randint(MIN_X, MAX_X)
    y1 = random.randint(MIN_Y, MAX_Y)
    x2 = random.randint(MIN_X, MAX_X)
    y2 = random.randint(MIN_Y, MAX_Y)
    device.drag((x1, y1), (x2, y2))
    print "Monkey drag from (" + str(x1) + ", " + str(y1) + ") to (" + str(x2) + ", " + str(y2) + ")"
    print "Remain time: " + (str(end_time - time.time()))
    MonkeyRunner.sleep(WAITTIME * 2)
    
    if random.randint(0, 5) % 5 == 0:
        print "Go back."
        device.touch(81, 456, 'DOWN_AND_UP')
print "Monkey success."