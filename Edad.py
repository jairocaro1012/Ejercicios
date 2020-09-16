class edad:

    a=1
    b=2
    print("Ingresa tu edad")
    global ed
    ed = int(input())
    print("Ingresa el año actual")
    global an
    an = int(input())

    def E2070():
        da=2070-an
        ned = ed+da
        print("Tu edad sera", ned)
        return ned

    E2070()




