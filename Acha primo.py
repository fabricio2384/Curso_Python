
print("==================================================================================")
print("Verifica se um número é primo")
print("==================================================================================")
def éPrimo(x):
    fator = 2
    while x % fator !=0 and fator < x/2:
        fator = fator + 1
    if x % fator ==0:
        return False
    else:
        return True
            
n = 1
while n > 0:
    n = int(input("Digite um número inteiro: "))
    if éPrimo(n):
        print(n, "é primo!")
    else:
        print(n, "não é primo!")


