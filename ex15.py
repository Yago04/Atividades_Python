
def tabela_and(bit1, bit2):
    print('****Tabela Verdade And****')
    print (f'{bit1} and {bit2}=', bit1 and bit2) 

def tabela_or(bit1, bit2):
 print('****Tabela Verdade Or****')
 print(f'{bit1} or {bit2}=', bit1 or bit2)

def tabela_not(bit1):
    print('****Tabela Verdade Not***')
    print(f'{bit1} not =', not bit1)



print('\n*****************')
print(' TABELA VERDADE ')
print(' 1. Operador AND ')
print(' 2.Operador OR ' )
print('3. Operador NOT')
print('\n*************')

opcao = int(input('Por favor digite um numero 1 a 3: '))

if opcao == 1:

    bit1 = bool(int(input('Digite o primeiro bit 1 ou 0: ')))
    bit2 = bool(int(input('Digite o segundo bit 1 ou 0: ')))
    tabela_and(bit1, bit2)

elif opcao == 2:
   bit1 = bool(int(input('Digite o primeiro bit 1 ou 0: ')))
   bit2 = bool(int(input('Digite o segundo bit 1 ou 0: ')))
   tabela_or(bit1, bit2)

elif opcao == 3:
   bit1 = bool(int(input('Digite o primeiro bit 1 ou 0: ')))
   tabela_not(bit1)

else :
    print('Opcao Invalida ')


