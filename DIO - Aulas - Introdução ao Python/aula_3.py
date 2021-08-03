# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior número é {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))
# print('Final do programa')


# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre ocm o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b == 0:
#     print("Foi digitado um número par")
# else:
#     print("nenhum número par foi digitado")

pri = int(input('Primeiro bimestre: '))
if pri > 10:
    pri = int(input('Você digitou errado. Primeiro bimestre: '))
seg = int(input('Segundo bimestre: '))
if seg > 10:
    seg = int(input('Você digitou errado. Segundo bimestre: '))
ter = int(input('Terceiro bimestre: '))
if ter > 10:
    ter = int(input('Você digitou errado. Terceiro bimestre: '))
qua = int(input('Quarto bimestre: '))
if qua > 10:
    qua = int(input('Você digitou errado. Quarto bimestre: '))

media = (pri + seg + ter + qua)/4
print('Media: {}'.format(media))
