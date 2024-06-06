import funcoes as f

while True:
    print("-" * 42)
    print("Bem-vindo ao Sistema de Aluguel de Bicicletas")
    print("-" * 42)
    print("[1] Login")
    print("[2] Cadastro")
    print("[3] Sair")
    print("-" * 42)
    
    opcao = input("Opção: ")
    
    if opcao == "1":
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
                            print("Data ou hora inválida. Tente novamente.")
                            locacao = f.fazer_locacao(indice_usuario)

                    else:
                        print("Você precisa de pelo menos 5 créditos.")
                elif opcao_usuario == "2":
                    devolucao = f.fazer_devolucao(indice_usuario)
                    if not devolucao:
                        print("Você não possui uma locação em andamento.")
                elif opcao_usuario == "3":
                    f.imprimir_relatorio(indice_usuario)
                elif opcao_usuario == "4":
                    
                    f.atualizar_creditos(indice_usuario)
                    print("Créditos atualizados com sucesso para o usuário", login)
                    print("Novo saldo de créditos:", f.usuarios[indice_usuario][2])
                    
                elif opcao_usuario == "0":
                    print("Voltando...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        else:
            print("Falha no login. Tente novamente.")

    elif opcao == "2":
        cadastrou_usuario = f.cadastrar_usuario()
        if not cadastrou_usuario:
            print("Usuário já cadastrado.")
        else:
            print("Usuário cadastrado com sucesso.")

    elif opcao == "3":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
