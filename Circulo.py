import math


class circulo:

    def __init__(self,radio,centro):
        self.radio=radio
        self.centro=centro

    def hallararea(self):
        area= ((c1.radio)**2)*math.pi
        print(area)
        return area
    def hallar_peri(self):
        perimetro= c1.radio*math.pi
        print(perimetro)
        return perimetro

c1=circulo(radio=3,centro=5)
c1.hallararea()
c1.hallar_peri()


