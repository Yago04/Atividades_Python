import math

numero1 = float(input('Por favor insira o primeiro: '))

numero2 = float(input('Por favor insira o segundo:  '))


print('\ndigite 1 paramedia ponderada:\n ')
print('\ndigite 2  quadrado da soma dos 2 números:\n')
print('\ndigite 3  Cubo do menor número:\n')

opcao = int(input('digite a opção que deseje: '))


if opcao == 1:

    conta1 = (2*numero1 + 3 * numero2) / 5
    print('o valor da media ponderada e: ', conta1)


elif opcao == 2:

    conta = (numero1 + numero2) ** 2
    print('o valor ao quadrado e de : ', conta)


elif  opcao == 3:
    if   numero1 > numero2:
        conta2 = numero2 **3
        print('o seu resultado ao cubo e: ', conta2)
    else:
     conta3 = numero1 **3
    print('o seu resultado ao cubo e:  ', conta3)

else:
   
   print('Opcao invalida escolha opcao 1,2 ou 3')
