import sys, time
import RPi.GPIO as G
G.setmode(G.BCM)

class Motor():

  #Set GPIOs for motors
  def _init_(self):

        # GPIOs controllers for motors
        G.setup(5,G.OUT)
        G.setup(6,G.OUT)
        #G.setup(13,G.OUT) # front
        #G.setup(19,G.OUT) # back

        #PWM for motors
        G.setup(18,G.OUT)
        G.setup(23,G.OUT)
        #G.setup(24,G.OUT)
        #G.setup(25,G.OUT)

        #Frequency operation
        self.pwm_m1 = G.PWM(18,100)
        self.pwm_m2 = G.PWM(23,100)
        #self.pwm_m3 = G.PWM(24,100)
        #self.pwm_m4 = G.PWM(25,100)

        #Starts PWM cycle
        self.pwm_m1.start(0)
        self.pwm_m2.start(0)
        #self.pwm_m3.start(0)
        #self.pwm_m4.start(0)

#Velocity control
def set_velocity(self, speed):

        # M1
        #speed = M1*speed
        self.pwm_m1.ChangeDutyCycle(speed)
        self.pwm_m1.stop()

        # M2
        #speed = M2*speed
        self.pwm_m2.ChangeDutyCycle(speed)
        self.pwm_m2.stop()

        # M3
        """
        speed = M3*speed
        self.pwm_m3.ChangeDutyCycle(speed)
        self.pwm_m3.stop()

        # M4
        self.pwm_m4.ChangeDutyCycle(speed)
        self.pwm_m4.stop()
        """

def stop(self):
        G.output(5,False)
        G.output(6,False)
        #G.output(13,False)
        #G.output(19,False)
