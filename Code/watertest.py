import datetime
import RPi.GPIO as GPIO 
import time 
from relayhandler import controlrelay 
GPIOPin= 7 
controlrelay(GPIOPin,0)
while True:
    now = datetime.datetime.now()  
    day=int(time.strftime("%w"))   
    if  day==1  or day==3  or day==5 or day==6 : 
        if now.hour ==14  and now.minute == 52 and now.second < 12 :  
          controlrelay(GPIOPin,1)
        else: 
          controlrelay(GPIOPin,0)
    #time.sleep(0.2)







