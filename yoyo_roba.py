from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import random
import sys

package = 'com.yoyoxiaomi.assistant'
activity = 'com.yoyoxiaomi.assistant.MainActivity'
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

device.touch(200, 280, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME * 2)

device.touch(90, 450, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME * 2)

print "hello"

print "Monkey success."