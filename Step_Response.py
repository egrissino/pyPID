## Evan Grissino
## 20/01/17
## PID Step Responses
## 2.x only

from matplotlib.pyplot import *
from pyPID import *

def critical_response():
    p = PID()
    p.setPoint(1)
    current = 0
    data = []

    for i in range(1, 5):
        if i > 2:
            i -= 2
            
        p.setPoint(i)
        for _ in range(100):
            current += p.update(current) / 10
            data.append(current)

    plot(data)
    show()

def under_response():
    p = PID()

    p.setKp(3.0)
    p.setKi(1.0)
    p.setKd(1.0)
    
    p.setPoint(1)
    current = 0
    data = []

    for i in range(1, 5):
        if i > 2:
            i -= 2
            
        p.setPoint(i)
        for _ in range(100):
            current += p.update(current) / 10
            data.append(current)

    plot(data)
    show()
