
class palindormo:
    def leer():
        global palabra
        print("Ingrese la palabra a porbra")
        palabra=input();

    def voltear():
        global palabra_dos
        palabra_dos=palabra[::-1]
        print(palabra_dos)

    def compara():
        global total,i
        total=0;
        i=0;
        for i in range(len(palabra)):
            if palabra[i]==palabra_dos[i]:
                total=total+1;

    def resultados():
        if total==len(palabra):
            print("Es palindromo")
        elif total!=len(palabra):
            print("No es palindroma")


    leer()
    voltear()
    compara()
    resultados()