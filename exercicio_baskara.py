# -*- coding: utf-8 -*-
from cmath import sqrt

a =  int(input ("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
c = int(input("Digite o valor de c:"))
delta = b**2 - 4*a*c
x1 = ((-b + sqrt(delta)) / (2*a))
x2 = ((-b - sqrt(delta)) / (2*a))

#primeira parte 
print(" O valor de delta é:", delta)

#segunda parte
if delta < 0:
    print("a equação não possui valores reais")
elif delta == 0:
    print("o valor de x1 é:", x1 ,"o valor de x2 é:", x2)
elif delta > 0: 
    print("o valor de x1 é:", x1 ,"o valor de x2 é:", x2)