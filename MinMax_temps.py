def MinMax(temperaturas):
    print("A menor temperatura do mês foi: ",minima(temperaturas),"c.")
    print("A maior temperatura do mês foi: ",maxima(temperaturas),"c.")

def minima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min
def maxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max
def teste_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if minima(temp) != 0:
        print("Valor errado para o array ", temp)
        print("Valor esperado ", valor_esperado," Valor calculado: ",valor_calculado)
    
def testa_minima():
    print("Iniciando os testes")
    teste_pontual([0],0)
    teste_pontual([0,0,0,0,0,0,0,0],0)
    teste_pontual([0,1,2,3,4,5,6,7,8,9,10],0)
    teste_pontual([-15,-12,0,20,30],-15)
    print("Finalizando os testes")
    
