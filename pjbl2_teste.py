import funcoes as f

while True:
    print("\nSistema de Pagamentos - Serviço de Locação de Bicicletas")
    print("1 - cadastrar usuário")
    print("2 - fazer login")
    print("0 - sair")
    
    opcao = input("escolha uma opção: ")
    
    if opcao == "0":
        break
    elif opcao == "1":
        cadastrou_usuario = f.cadastrar_usuario()
        if not cadastrou_usuario:
            print("usuário já cadastrado.")
        else:
            print("usuário cadastrado com sucesso.")
    elif opcao == "2":
    
        indice_usuario, login, senha = f.login_usuario()

        if (login and senha):
            while True:
                print("\nusuário logado:", login)
                print("créditos:", f.usuarios[indice_usuario][2])
                print("1. fazer locação")
                print("2. fazer devolução")
                print("3. imprimir relatório de locações")
                print("4. adicionar créditos")
                print("0. sair")
                
                
                opcao = input("escolha uma opção: ")
                if opcao == "1":
                    if f.usuarios[indice_usuario][2] >= 5:
                        locacao = f.fazer_locacao(indice_usuario)
                        if not locacao:
                            print("data ou hora inválida. tente novamente.")
                            locacao = f.fazer_locacao(indice_usuario)

                    else:
                        print("você precisa de pelo menos 5 créditos para alugar uma bicicleta.")
                elif opcao == "2":
                    devolucao = f.fazer_devolucao(indice_usuario)
                    if not devolucao:
                        print("Você não possui uma locação em andamento.")
                elif opcao == "3":
                    f.imprimir_relatorio(indice_usuario)
                elif opcao == "4":
                    
                    f.atualizar_creditos(indice_usuario)
                    print("créditos atualizados com sucesso para o usuário", login)
                    print("novo saldo de créditos:", f.usuarios[indice_usuario][2])
                    
                elif opcao == "0":
                    print("saindo do sistema...")
                    break
                else:
                    print("opção inválida. tente novamente.")
        else:
            print("falha no login. tente novamente.")
    else:
            print("opção inválida. tente novamente.")