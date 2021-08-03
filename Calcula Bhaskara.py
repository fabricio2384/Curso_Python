import math 
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
delta = b**2 - 4*a*c
print("DElta: ",delta)
if delta < 0:
    print("Inexiste raizes reais")
elif delta == 0:
    x0 = (-b/(2*a))
    print("Raiz X: ",x0)
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("Raiz X1: ",x1, "Raiz X2: ",x2)
