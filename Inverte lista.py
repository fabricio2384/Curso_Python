
print("==================================================================================")
print("Inverte uma sequencia de números de uma lista")
print("==================================================================================")

print("Esse programa imprime uma sequencia de números com final 0")
print("em ordem inversa da digitada, aperte 1 para finalizar o programa")
print("----------------------------------------------------------------")

list_entrada = []
list_saida = []
n = 0
i = 0
while n != 1:
    n = int(input("Digite um número: "))
    if (n%10) == 0:
        list_entrada.append(n)
#list_num.reverse()
x = (len(list_entrada)-1)
i=0
list_saida = list_entrada
list_saida = 0
print(" Lista: ",list_entrada)
while x != 0:
    x = x-1
    list_saida[i] = list_entrada[x-i]
    print("out :",list_saida[i], "in :",list_entrada[x])
    print("i :",i, "x :",x)
print(" Lista Inversa: ",list_saida, "x: ",x,"i: ", i)    
   



