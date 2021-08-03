print("==================================================================================")
print("Determina se uma sequencia é crescente ou decrescente")
print("==================================================================================")

decrescente = True 
anterior = int(input("Digite o primeiro número da sequencia: "))
valor = 1
while valor != 0 and decrescente:
    valor = int(input("Digite o próximo número da sequencia: "))
    if valor > anterior:
         decrescente = False
    anterior = valor    
if decrescente == True:
    print("A sequencia está em prdem decrescente! :-)")
else:
    print("A sequencia não está em ordem descrecente! :-(")
