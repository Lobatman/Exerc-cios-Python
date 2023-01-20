# -*- coding: utf-8 -*-

peso = float(input("Escreva seu peso: "))
altura = float(input("Escreva sua altura: "))

IMC = peso / (altura ** 2)
print("Seu índice de massa corporal é:", IMC)

if IMC <= 18.5:
    print("Magreza")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Normal")
elif IMC >= 25.0 and IMC <= 29.9:
    print("Sobrepeso")
elif IMC >= 30 and IMC <= 39.9:
    print ("Obesidade")
elif IMC >= 40:
    print("Obesidade Grave")