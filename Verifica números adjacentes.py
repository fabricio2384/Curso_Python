print("==================================================================================")
print("                    Verifica se exitem números adjacentes")
print("==================================================================================")

Valor = int(input("Digite um número: "))
Num = -1
NextNum = -1
Aux = False
#-------------------------------------------
while Valor !=0 and not Aux == True:
    Num = Valor%10
    Valor = Valor//10
    if Num == NextNum:
        Aux = True
    NextNum = Num
#---------------------------------------------   

if Aux == True:
    print("Existem números adjacentes")
    print("Números em sequencia: ",NextNum,", ",Num)
else:
    print("Não exite números adjacentes")



        

