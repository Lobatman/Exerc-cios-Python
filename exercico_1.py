# -*- coding: utf-8 -*-
while True: 
    idade = input("Digite sua idade: ")

    try:
        idade = int (idade) 
    except:
        print("a idade deve ser inserida em número")
    else: 
        if idade >= 18:
            print ("Maior de idade")
        else:
            print("Menor de idade")
        break
    