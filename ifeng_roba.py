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
DEBUG = False

print "Wait For connection..."
if DEBUG == True:
    device = MonkeyRunner.waitForConnection()
    WAITTIME = 5
else:
    WAITTIME = randomint(3, 7)
    device = MonkeyRunner.waitForConnection(300, sys.argv[1])

print "Connected."
device.startActivity(component=runComponent)

MonkeyRunner.sleep(WAITTIME * 2)

device.touch(220, 275, 'DOWN_AND_UP')

MonkeyRunner.sleep(WAITTIME)

for i in range(0, random.randint(3, 5)):
    for j in range(0, random.randint(0, 3)):    
        device.drag((160, 300), (160, 100))  
        MonkeyRunner.sleep(WAITTIME) 
    device.touch(220, 268, 'DOWN_AND_UP')
    MonkeyRunner.sleep(WAITTIME) 
    for k in range(0, random.randint(0, 5)):    
        device.drag((160, 300), (160, 100))  
        MonkeyRunner.sleep(WAITTIME) 
    device.touch(85, 458, 'DOWN_AND_UP')
    MonkeyRunner.sleep(WAITTIME) 

start_time = time.time()
print "Current time:" + str(start_time)

end_time = start_time + random.randint(5, 60)

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
