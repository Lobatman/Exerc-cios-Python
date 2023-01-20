# -*- coding: utf-8 -*-
nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input( "digite sua segunda nota: "))

total = (nota1 + nota2) /2

if total >= 6: 
    print("Aprovado, com a nota ", total)
else: 
    print("Reprovado")