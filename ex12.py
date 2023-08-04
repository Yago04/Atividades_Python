import math 

nota1 = float(input('por favor insira a sua nota do primeiro bimestre: '))

nota2 = float(input('por favor insira a sua nota do segundo bimestre: '))

nota3 = float(input('por favor insira a sua nota do terceiro bimestre: '))

nota4 = float(input('por favor insira a sua nota do quarto  bimestre: '))


media = ( nota1 + nota2+ nota3+ nota4) / 4

if media < 4.9:
    print('Parabens voce esta Reprovado')

elif 5 <= media < 6.9:
    print('Parabens voce esta de Recuperacao')

if media >= 7 :
    print('Parabens voce esta Aprovado')
 
