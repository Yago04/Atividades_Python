import math

altura =  float(input("por favor insira a sua altura:"))

peso = float(input('por favor insira o seu peso: '))

conta = peso / ( altura * altura) 
print(f'o seu imc e de : {conta: .2f}')