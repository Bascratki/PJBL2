admin_login = "admin"
admin_password = "admin123"

tempo_credito = 1

usuarios = [
    {
        "cpf": "",
        "senha": "",
        "créditos": 0,
    }
]

locacoes = [
    {
        "cpf_locacao": "",
        "data_retirada": "",
        "hora_retirada": "",
        "data_devolução": "",
        "hora_devolução": "",
    }
]


# Ínicio do código
while True:
    print("-" * 42)
    print("Bem-vindo ao Sistema de Aluguel de Bicicletas")
    print("-" * 42)
    print("[1] Login")
    print("[2] Cadastro")
    print("[3] Sair")
    print("-" * 42)
    
    option = input("Opção: ")
    
    if option == "1":
        cpf = input("Digite o CPF: ")
        senha = input("Digite a senha: ")
        
        if cpf == admin_login and senha == admin_password:
            while True:
                print("-" * 42)
                print("Bem-vindo ao Menu do Administrador")
                print("-" * 42)
                print("[1] Imprimir Relatório")
                print("[2] Verificar Créditos")
                print("[3] Atualizar Créditos")
                print("[4] Sair")
                print("-" * 42)
                
                admin_option = input("Opção: ")

                if admin_option == "1":
                    if len(locacoes) == 0:
                        print("Nenhuma locação encontrada.")
                        continue
                    else:
                        print("Relatório de Locações")
                        for locacao in locacoes:
                            print("Usuário:", locacao["cpf_locacao"])
                            print("Data de Retirada:", locacao["data_retirada"])
                            print("Hora de Retirada:", locacao["hora_retirada"])
                            print("Data de Devolução:", locacao["data_devolução"])
                            print("Hora de Devolução:", locacao["hora_devolução"])
                            break
                                            
                elif admin_option == "2":
                    print("Verificação de Créditos")
                    if len(usuarios) == 0:
                        print("Nenhum usuário encontrado.")
                        continue
                    else:
                        cpf = input("Digite o CPF: ")
                        for usuario in usuarios:
                            if usuario["cpf"] == cpf:
                                print("CPF:", usuario["cpf"])
                                print("Senha:", usuario["senha"])
                                print("Créditos:", usuario["créditos"])
                                break
                        else:
                            print("Usuário não encontrado.")
                            continue
                        break
                                                            
                elif admin_option == "3":
                    print("Atualização de Créditos")
                    cpf = input("Digite o CPF: ")
                    if usuario["cpf"] == cpf:
                        credito = float(input("Digite o valor da recarga: "))
                        usuario["créditos"] += credito
                        print("Créditos atualizados com sucesso.")
                        print("Novo saldo de créditos:", usuario["créditos"])
                        print("Válidos para uso por", tempo_credito * usuario["créditos"], "horas.")
                        break
                    else:
                        print("Usuário não encontrado.")
                        continue
                                    
                elif admin_option == "4":
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
                    continue
        else:
            for usuario in usuarios:
                if usuario["cpf"] == cpf and usuario["senha"] == senha:
                    print("Login realizado com sucesso!")
                    while True:
                        print("-" * 42)
                        print("Bem-vindo ao Menu do Usuário")
                        print("-" * 42)
                        print("[1] Alugar Bicicleta")
                        print("[2] Devolver Bicicleta")
                        print("[3] Consulta de Aluguéis")
                        print("[4] Recarga de Créditos")
                        print("[5] Sair")
                        print("-" * 42)
                        
                        user_option = input("Opção: ")
                        
                        if user_option == "1":
                            if usuario["créditos"] >= 5:
                                print("Aluguel de Bicicleta")
                                data_retirada = input("Data de retirada, no formato dd/mm/aaaa: ")
                                hora_retirada = input("Hora de retirada, no formato hh:mm: ")
                                data_devolucao = input("Data de devolução, no formato dd/mm/aaaa: ")
                                hora_devolucao = input("Hora de devolução, no formato hh:mm: ")
                                tempo_aluguel = (int(data_devolucao[0:2]) - int(data_retirada[0:2])) * 24 + (int(hora_devolucao[0:2]) - int(hora_retirada[0:2]))
                                if tempo_aluguel <= usuario["créditos"]:
                                    locacoes.append([usuario["cpf"], data_retirada, hora_retirada, data_devolucao, hora_devolucao])
                                    usuario["créditos"] -= tempo_aluguel
                                    print("Bicicleta alugada com sucesso!")
                                    print("Créditos restantes:", usuario["créditos"])
                                    print("Válidos para uso por", tempo_credito * usuario["créditos"], "horas.")
                                else:
                                    print("Créditos insuficientes para realizar a locação.")
                                    print("Você precisa de pelo menos 5 créditos para alugar uma bicicleta.")
                                    continue
                            else:
                                print("Créditos insuficientes para realizar a locação.")
                                print("Você precisa de pelo menos 5 créditos para alugar uma bicicleta.")
                                continue
                            
                        elif user_option == "2":
                            if len(locacoes) == 0:
                                print("Nenhuma bicicleta alugada.")
                                continue
                            else:
                                for locacao in locacoes:
                                    print("Devolução de Bicicleta")
                                    if locacao["cpf_locacao"] == usuario["cpf"]:
                                        locacao["data_devolução"] = input("Data de Devolução: ")
                                        locacao["hora_devolucao"] = input("Hora de Devolução: ")
                                        # Erro aqui
                                        print("Bicicleta devolvida com sucesso!")
                                        break
                                else:
                                    print("Nenhuma bicicleta alugada.")
                                    continue
                            
                        elif user_option == "3":
                            for locacao in locacoes:
                                # Erro aqui
                                if locacao["cpf_locacao"] == usuario["cpf"]:
                                    print("Consulta de Aluguéis")
                                    print("Data de Retirada:", locacao["data_retirada"])
                                    print("Hora de Retirada:", locacao["hora_retirada"])
                                    print("Data de Devolução:", locacao["data_devolução"])
                                    print("Hora de Devolução:", locacao["hora_devolucao"])
                            else:
                                print("Nenhum aluguel encontrado.")
                                continue
                            
                        elif user_option == "4":
                            print("Recarga de Créditos")
                            credito = float(input("Digite o valor da recarga: "))
                            usuario["créditos"] += credito
                            print("Créditos atualizados com sucesso.")
                            print("Novo saldo de créditos:", usuario["créditos"])
                            print("Válidos para uso por", tempo_credito * usuario["créditos"], "horas.")
                        
                        elif user_option == "5":
                            print("Saindo...")
                            break
                        else:
                            print("Opção inválida. Tente novamente.")
                            continue
                    break
                elif usuario["cpf"] == cpf and usuario["senha"] != senha:
                    print("Senha incorreta.")
                    break
            else:
                print("Usuário não encontrado.")
                print("Faça o cadastro.")
                continue
                
    elif option == "2":
        print("Cadastro de Usuário")
        cpf = input("Digite o CPF: ")
        senha = input("Digite a senha: ")
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                print("Usuário já cadastrado.")
                break
        else:
            usuarios.append({"cpf": cpf, "senha": senha, "créditos": 0})
            print("Usuário cadastrado com sucesso!")
                
    elif option == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        continue