import math

class triangulo:

    def __init__(self,lado1,lado2,lado3,base,altura):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
        self.base=base
        self.altura=altura

    def hallararea(self):
        area=(t1.base*t1.altura)/2
        print(area)
        return area
    def hallar_perimetro(self):
        peri=t1.lado1+t1.lado2+t1.lado3
        print(peri)
        return peri

t1=triangulo(lado1=1,lado2=2,lado3=3,base=3,altura=5)
t1.hallararea()
t1.hallar_perimetro()