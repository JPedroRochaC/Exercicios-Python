def verificar_login(usuario, senha, usuario_correto, senha_correta):

    if usuario == usuario_correto and senha == senha_correta:
        return True
    else:
        return False


usuario_cadastro = ""
senha_cadastro = ""

print("1 - Cadastro")
print("2 - Login")

opcao = int(input("Escolha: "))

match opcao:

    case 1:
        print("=== CADASTRO ===")

        usuario_cadastro = input('Digite o nome do seu usuário: ')
        senha_cadastro = int(input('Digite sua senha: '))

        print("Cadastro realizado!")

    case 2:

        if usuario_cadastro == "":
            print("Nenhum usuário cadastrado!")

        else:
            chance = 3

            while chance > 0:

                u = input('Usuário: ')
                s = int(input('Senha: '))

                if verificar_login(u, s, usuario_cadastro, senha_cadastro):
                    print('Acessando...')
                    break

                else:
                    chance -= 1
                    print('Erro')

                    if chance == 0:
                        print('BLOQUEADO')

    case _:
        print("Opção inválida")