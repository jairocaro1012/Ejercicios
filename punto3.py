def leer():
    global palabra, descom
    print("Ingrese la palabra a descomponer")
    palabra=input()


def descomponer():
    d1=palabra[0];
    d2=palabra[len(palabra)-1]
    print("Primera letra = ",d1)
    print("ultima letra  = ",d2)

leer()
descomponer()