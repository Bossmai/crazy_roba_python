from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import random
import sys

package = 'com.ifeng.news2'
activity = 'com.ifeng.news2.activity.SplashActivity'
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

MonkeyRunner.sleep(WAITTIME * 3)

device.drag((160, 300),(160, 150))

start_time = time.time()
print "Current time:" + str(start_time)

end_time = start_time + 300

while time.time() < end_time:
    for j in range(3):
        for i in range(5):
            if random.randint(0, 1) % 2 == 0:
                device.drag((160, 300),(160, 150))
                MonkeyRunner.sleep(WAITTIME)
                
        x = random.randint(MIN_X, MAX_X)
        y = random.randint(MIN_Y, MAX_Y)
        device.touch(x, y, 'DOWN')
        MonkeyRunner.sleep(2)
        device.touch(x, y, 'UP')
        print "Monkey touch in (" + str(x) + ", " + str(y) + ")"
        MonkeyRunner.sleep(WAITTIME)    
        
        for i in range(5):
            if random.randint(0, 1) % 2 == 0:
                device.drag((160, 300),(160, 150))
                MonkeyRunner.sleep(WAITTIME)
                
        device.touch(83, 457, 'DOWN')
        MonkeyRunner.sleep(2)
        device.touch(83, 457, 'UP')
        MonkeyRunner.sleep(WAITTIME)
print "Monkey success."
