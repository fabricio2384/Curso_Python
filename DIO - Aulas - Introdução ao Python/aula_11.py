lista =     [1,10]
try:
    divisao = 10/1
    numero = lista[1]
    x = a
except ZeroDivisionError:
    print('Não é possivel realizar divisão por zero')
except IndexError:
    print('Erro ao acessar um indice invalido na lista')
except BaseException as ex:
    print('erro desconhecido. Erro: {}'.format(ex))