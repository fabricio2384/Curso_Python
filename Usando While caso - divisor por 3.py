print("==================================================================================")
print("Programa para contar a quantidade de digitos de um dado número e a soma dos mesmos")
print("==================================================================================")


soma = 0
i = 0
valor = int(input("Digite um valor: "))
part_int_div = valor
#rest_div = valor
while part_int_div != 0:
     rest_div =  part_int_div% 10
     part_int_div = part_int_div // 10     
     soma = soma + rest_div
     i = i + 1

print("Quantidade de digitos é: ",i," , E a soma é: ",soma)

            
