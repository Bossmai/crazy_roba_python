from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import random
import sys
package = 'cn.kuwo.player'
activity = 'cn.kuwo.player.activities.EntryActivity'
runComponent = package + '/' + activity

MIN_X=10
MAX_X=300
MIN_Y=310
MAX_Y=350



isDebug = True


print "Wait For connection..."
if isDebug == True:
    device = MonkeyRunner.waitForConnection()
    WAITTIME = 2
else:
    device = MonkeyRunner.waitForConnection(300, sys.argv[1])
    WAITTIME = 10

print "Connected."
device.startActivity(component=runComponent)

MonkeyRunner.sleep(WAITTIME * 5)


print "Close menu."
device.touch(43, 43, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME * 4)



print "Close float window."
device.touch(43, 43, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME * 4)


print "Go Into Daily play."
device.touch(160, 293, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME * 4)

print "Close floating tips."
device.touch(160, 293, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME * 4)


print "Play music."
device.touch(68, 159, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME * 4)

print "Close Play tips."
device.touch(222, 274, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME * 4)

print "Go back."
device.touch(16, 405, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME * 4)


print "Go back again."
device.touch(16, 405, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME * 4)

print "Start random click."
start_time = time.time()
print "Current time:" + str(start_time)

end_time = start_time + 500

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
    MonkeyRunner.sleep(WAITTIME)
print "Monkey success."
