
def validar1(login1, senha):

    return login1 == "procopio" and senha == 12345


def validar2(login2, senha1):
    return login2 == 'paiva' and senha1== 54321

print('********************')
print('Seja bem vindo ao Painel de Rede')

usuario = (input('Por favor informe o seu usuario: '))
passowoard= int(input('Por favor informe sua senha: '))



if validar1(usuario, passowoard) or validar2(usuario, passowoard):
    print('Seja bem vindo ao painel de rede')

else:
    print('email nao cadastrado')