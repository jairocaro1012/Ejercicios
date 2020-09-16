import math

class punto:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def hadi(self,p2):
        r=math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)
        print(r)
        return r


p1=punto(2,3)
p2=punto(4,4)
p1.hadi(p2)
