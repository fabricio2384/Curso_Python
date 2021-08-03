print("=======================================================================================================")
print("Programa para ler uma lista de palavras e devolver a de menor tamanho com a primeira letra em maiusculo")
print("=======================================================================================================")



def LerDados():
        i = 1
     
        string = []
        Valor = input("Digite uma palavra: ")
        while Valor != '1':
            string.append(Valor)
            Valor = input("Digite uma palavra: ")
            string = [item.strip().capitalize() for item in string]
        Min = string[0]
        while i < len(string):
            if (string[i]) < Min:
                Min = string[i]
            i = i + 1

        return print("Nomes inseridos:\n",string,"\n Nome com menor número de caracteres nesta lista",Min)
            

'''
def minima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min'''
