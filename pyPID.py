## Evan Grissino
## 1/15/2016
## Pyhton PID controller

class PID(object):

    def __init__(self, P = 2.0, I = 0.0, D = 1.0, Derivator = 0, Integrator=0, Integrator_max=500, Integrator_min=-500):
        
        self.Kp = P
        self.Ki = I
        self.Kd = D
        
        self.Derivator = Derivator
        self.Integrator=Integrator
        self.Integrator_max=Integrator_max
        self.Integrator_min=Integrator_min

        self.gain = 1

        self.set_point=0.0
        self.error=0.0

    def update(self, current_value):

        last_error = self.error
        
        self.error = self.set_point - current_value
        
        self.Derivator = last_error - self.error

        self.Integrator = self.Integrator + self.error
        
        if self.Integrator > self.Integrator_max:
            self.Integrator = Self.Integrator_max
        elif self.Integrator < self.Integrator_min:
            self.Integrator = Self.Integrator_min

        self.P_value = self.Kp * self.error
        self.I_value = self.Ki * self.Integrator
        self.D_value = self.Kd * self.Derivator

        pid = self.P_value + self.I_value + self.D_value

        #print self.Integrator

        return pid

    def setPoint(self,set_point):
        """
        Initilize the setpoint of PID
        """
        self.set_point = set_point
        self.Integrator=0
        self.Derivator=0

    def setGain(self, new_gain_value):
        self.gain = new_gain_value

    def setIntegrator(self, Integrator):
            self.Integrator = Integrator

    def setDerivator(self, Derivator):
            self.Derivator = Derivator

    def setKp(self,P):
            self.Kp=P

    def setKi(self,I):
            self.Ki=I

    def setKd(self,D):
            self.Kd=D

    def getPoint(self):
            return self.set_point

    def getError(self):
            return self.error

    def getIntegrator(self):
            return self.Integrator

    def getDerivator(self):
            return self.Derivator
