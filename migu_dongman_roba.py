from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import random
import sys

package = 'com.hisunflytone.android'
activity = 'com.cmdm.android.controller.InitActivity'
runComponent = package + '/' + activity

MIN_X=20
MAX_X=300
MIN_Y=80
MAX_Y=400

WAITTIME = 8
DEBUG = True

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


device.touch(160, 460, 'DOWN_AND_UP')  

MonkeyRunner.sleep(WAITTIME)   

device.touch(264, 462, 'DOWN_AND_UP') 

MonkeyRunner.sleep(WAITTIME)      

device.drag((207, 380), (40, 380))

MonkeyRunner.sleep(WAITTIME)   
 

device.startActivity(component=runComponent)
MonkeyRunner.sleep(WAITTIME)

device.touch(187, 375, 'DOWN_AND_UP')  

MonkeyRunner.sleep(WAITTIME)   

device.touch(101, 398, 'DOWN_AND_UP') 

MonkeyRunner.sleep(WAITTIME)   

device.touch(54, 132, 'DOWN_AND_UP') 

MonkeyRunner.sleep(WAITTIME)     

device.touch(88, 324, 'DOWN_AND_UP') 

MonkeyRunner.sleep(WAITTIME)    

device.touch(195, 220, 'DOWN_AND_UP') 

MonkeyRunner.sleep(WAITTIME)    
  

start_time = time.time()
print "Current time:" + str(start_time)

end_time = start_time + random.randint(50,100)


while time.time() < end_time:
    device.drag((240,300),(240,100))
    MonkeyRunner.sleep(WAITTIME)  
print "Monkey success."
