import funcoes as f

while True:
    print("-" * 42)
    print("Bem-vindo ao Sistema de Aluguel de Bicicletas")
    print("-" * 42)
    print("[1] Login")
    print("[2] Cadastro")
    print("[3] Sair")
    print("-" * 42)
    
    opcao = input("opção: ")
    
    if opcao == "1":
        cadastrou_usuario = f.cadastrar_usuario()
        if not cadastrou_usuario:
            print("usuário já cadastrado.")
        else:
            print("usuário cadastrado com sucesso.")
    elif opcao == "2":
    
        indice_usuario, login, senha = f.login_usuario()

        if (login and senha):
            while True:
                print("-" * 42)
                print("Bem-vindo ao Menu do Usuário")
                print("-" * 42)
                print("Usuário:", login)
                print("Créditos:", f.usuarios[indice_usuario][2])
                print("-" * 42)
                print("[1] Alugar Bicicleta")
                print("[2] Devolver Bicicleta")
                print("[3] Consulta de Aluguéis")
                print("[4] Recarga de Créditos")
                print("[5] Sair")
                print("-" * 42)
                
                opcao_usuario = input("Opção: ")
                
                if opcao_usuario == "1":
                    if f.usuarios[indice_usuario][2] >= 5:
                        locacao = f.fazer_locacao(indice_usuario)
                        if not locacao:
                            print("data ou hora inválida. tente novamente.")
                            locacao = f.fazer_locacao(indice_usuario)

                    else:
                        print("você precisa de pelo menos 5 créditos para alugar uma bicicleta.")
                elif opcao_usuario == "2":
                    devolucao = f.fazer_devolucao(indice_usuario)
                    if not devolucao:
                        print("Você não possui uma locação em andamento.")
                elif opcao_usuario == "3":
                    f.imprimir_relatorio(indice_usuario)
                elif opcao_usuario == "4":
                    
                    f.atualizar_creditos(indice_usuario)
                    print("créditos atualizados com sucesso para o usuário", login)
                    print("novo saldo de créditos:", f.usuarios[indice_usuario][2])
                    
                elif opcao_usuario == "0":
                    print("saindo do sistema...")
                    break
                else:
                    print("opção inválida. tente novamente.")
        else:
            print("falha no login. tente novamente.")

    elif opcao == "3":
        print("Saindo do sistema...")
        break
    else:
        print("opção inválida. tente novamente.")
