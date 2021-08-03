
print("==================================================================================")
print("Calculo fatorial de qualquer número")
print("==================================================================================")


Entrada = 1
while Entrada != "0":
    Resultado = 1
    Entrada = int(input("Digite um valor: "))
    i = Entrada
    while i != 1 :
        Resultado = Resultado * i
        i = i - 1
    print("-------------------------")
    print("Fatorial de ",Entrada," é: ",Resultado)    
    print("-------------------------")



            
