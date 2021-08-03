def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o elemento ["+ str(i) + "][" + str(j)+"]: "))
            if j ==0:
                linha.append("|"+str(valor))
            elif j ==(num_colunas-1):
                linha.append(str(valor)+"|")
            else:
                linha.append(valor)
        matriz.append(linha)
       # ler_linha = (str(linha))
    return matriz
    





    
#    return ler_linha
    







    
def le_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    return cria_matriz(lin,col)

#'if i == 0:'
 #'               linha.append("|"+str(valor))'
# '           elif i == (num_colunas-1):'
#               linha.append(str(valor)+"|"+"\r" )'''''
           # print( ", ".join( repr(e) for e in matriz ) )
