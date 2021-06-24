
import RPi.GPIO as GPIO  
import time
GPIO.setmode(GPIO.BCM)
delayt = .1
counter = 0 # this variable will be used to store the ldr value
ldr = 4 #ldr is connected with GPIO 4
 
led1 = 5 #led is connected with GPIO 5
led2= 31 #led is connected with GPIO 31
led3= 35 #led is connected with GPIO 35
led4= 37 #led is connected with GPIO 37
 
#set up I/O functions
GPIO.setup(led1, GPIO.OUT) 
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
 
# keep led off by default
GPIO.output(led1, False) 
GPIO.output(led2, False)
GPIO.output(led3, False)
GPIO.output(led4, False)
 
pwm_led1 = GPIO.PWM( led1, 50) # 50Hz PWM Frequency
pwm_led2 = GPIO.PWM( led2, 50)
pwm_led3 = GPIO.PWM( led3, 50)
pwm_led4 = GPIO.PWM( led4, 50)
pwm_led.start(100)  #0 is completely off and 100 is completely on
def rc_time (ldr):
    count = 0
 
    #Output on the pin for
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, False)
    time.sleep(delayt)
 
    #Change the pin back to input
    GPIO.setup(ldr, GPIO.IN)
 
    #Count until the pin goes high
    while (GPIO.input(ldr) == 0):
        count += 1
 
    return count
 
 
#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    #while True:
  x1= input('Enter the value ')
  x2= input('Enter the value ')
  while True:
      
    inval1=50
    inval2=70
    inval3=100
    print("Ldr Value:")
    counter = rc_time(ldr)
    print(value)
 
 
    if ( counter < x1 ):
            print("Lights are at 50 percent intensity")
            pwm_led1.ChangeDutyCycle(inval1)
            pwm_led2.ChangeDutyCycle(inval1)
    if (x1 < counter < x2):
        
        print("Lights are at 70 percent intensity")
        pwm_led1.ChangeDutyCycle(inval2)
        pwm_led2.ChangeDutyCycle(inval2)
        pwm_led3.ChangeDutyCycle(inval2)
    if (counter > x2):
        Print ("Lights are completely on")
        pwm_led1.ChangeDutyCycle(inval3)
        pwm_led2.ChangeDutyCycle(inval3)
        pwm_led3.ChangeDutyCycle(inval3)
        pwm_led4.ChangeDutyCycle(inval3) 
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
