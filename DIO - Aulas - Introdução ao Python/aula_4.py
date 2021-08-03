# a = int(input('Entre com um valor: '))
# for num in range (a+1):
#     div = 0
#     for x in range (1, num +1):
#         resto = num % x
#         if resto ==0:
#             div += 1
#     if div == 2:
#         print(num)

pri = int(input('Primeiro bimestre: '))
while pri > 10:
    pri = int(input('Você digitou errado. Primeiro bimestre: '))
seg = int(input('Segundo bimestre: '))
while seg > 10:
    seg = int(input('Você digitou errado. Segundo bimestre: '))
ter = int(input('Terceiro bimestre: '))
while ter > 10:
    ter = int(input('Você digitou errado. Terceiro bimestre: '))
qua = int(input('Quarto bimestre: '))
while qua > 10:
    qua = int(input('Você digitou errado. Quarto bimestre: '))

media = (pri + seg + ter + qua)/4
print('Media: {}'.format(media))


