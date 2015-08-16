from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import random
import sys

package = 'com.mianfeia.book'
activity = 'com.chineseall.reader.ui.FlashActivity'
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

MonkeyRunner.sleep(WAITTIME * 3)

device.touch(285, 124, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME)

device.touch(81, 452, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME)

device.touch(81, 452, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME)


device.touch(178, 240, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME)

device.touch(108, 341, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME)

device.touch(85, 287, 'DOWN_AND_UP')
MonkeyRunner.sleep(WAITTIME)
start_time = time.time()
print "Current time:" + str(start_time)

end_time = start_time + 120

while time.time() < end_time:
        device.drag((300, 160), (20, 160))
        MonkeyRunner.sleep(WAITTIME)
    
print "Monkey success."