import math

nome = str(input('Insira o nome do corretor: '))

valori = int(input('insira a qauntidade de imoveis vendido: '))
 
valort = float(input('Insira o valor total de suas vendas:'))

comissao = 200 * valori 

por = valort*0.05

salario =1500

soma = salario + comissao + por 

print('o nome do vendedor e : ',nome)

print(F"o valor final do salario ={soma: .2F}")




