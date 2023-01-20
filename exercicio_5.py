# -*- coding: utf-8 -*-
n1  = int(input("Escreva o primeiro numero: "))
n2 = int(input("Escreva o segundo numero: "))
sinal = input("Escreva o sinal: ")

if sinal == "+":
    op = n1 + n2
elif sinal == "*":
    op = n1 * n2
elif sinal == "/":
    op =  n1 / n2
elif sinal == "-": 
    op = n1 - n2 
else: 
     print("sinal inválido")

print("o resultado é", op)
