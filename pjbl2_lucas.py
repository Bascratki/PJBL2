admin_login = "admin"
admin_password = "admin123"

tempo_credito = 1

# Lista de usuários. Cada usuário é uma lista com login, senha e créditos.
usuarios = [
    ["095", "123", 30]
]

# Lista de locações. Cada locação é uma lista com os dados da locação.
locacoes = []

# Função que converte uma data e uma hora para minutos totais.
def minutos_totais(data, hora):
    minutos = int(data[0:2]) * 24 * 60 + int(data[3:5]) * 60 + int(hora[0:2]) * 60 + int(hora[3:5])
    return minutos

# Início do código
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
        login = input("Digite o login: ")
        senha = input("Digite a senha: ")
        
        # Menu do Administrador
        if login == admin_login and senha == admin_password:
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
                    else:
                        print("Relatório de Locações")
                        for locacao in locacoes:
                            print(f"Usuário: {locacao[0]}")
                            print(f"Data de Retirada: {locacao[1]}")
                            print(f"Hora de Retirada: {locacao[2]}")
                            print(f"Data de Devolução: {locacao[3] if len(locacao) > 3 else 'Não devolvido'}")
                            print(f"Hora de Devolução: {locacao[4] if len(locacao) > 4 else 'Não devolvido'}")
                            print("-" * 42)
                                            
                elif admin_option == "2":
                    print("Verificação de Créditos")
                    if len(usuarios) == 0:
                        print("Nenhum usuário encontrado.")
                    else:
                        login = input("Digite o login: ")
                        for usuario in usuarios:
                            if usuario[0] == login:
                                print(f"Login: {usuario[0]}")
                                print(f"Créditos: {usuario[2]}")
                                print(f"Válidos para uso por {tempo_credito * usuario[2]} horas.")
                                break
                        else:
                            print("Usuário não encontrado.")
                                                            
                elif admin_option == "3":
                    print("Atualização de Créditos")
                    login = input("Digite o login: ")
                    for usuario in usuarios:
                        if usuario[0] == login:
                            credito = float(input("Digite o valor da recarga: "))
                            usuario[2] += credito
                            print("Créditos atualizados com sucesso.")
                            print(f"Novo saldo de créditos: {usuario[2]}")
                            print(f"Válidos para uso por {tempo_credito * usuario[2]} horas.")
                            break
                    else:
                        print("Usuário não encontrado.")
                                    
                elif admin_option == "4":
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        # Menu do Usuário
        else:
            for usuario in usuarios:
                if usuario[0] == login and usuario[1] == senha:
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
                            if usuario[2] >= 5:
                                print("Aluguel de Bicicleta")
                                data_retirada = input("Digite a data de retirada, no formato dd/mm: ")
                                hora_retirada = input("Digite a hora de retirada, no formato hh:mm: ")
                                if len(data_retirada) == 5 and len(hora_retirada) == 5:
                                    if (int(data_retirada[0:2]) <= 31 and int(data_retirada[0:2]) > 0) and (int(data_retirada[3:5]) > 0 and int(data_retirada[3:5]) <= 12):
                                        if (int(hora_retirada[0:2]) >= 0 and int(hora_retirada[0:2]) < 24) and (int(hora_retirada[3:5]) >= 0 and int(hora_retirada[3:5]) < 60):
                                            locacoes.append([usuario[0], data_retirada, hora_retirada])
                                            print("Aluguel realizado com sucesso!")
                                            print("Hora de retirada:", locacoes[-1][2])
                                        else:
                                            print("Hora inválida.")
                                    else:
                                        print("Data inválida.")
                                else:
                                    print("Data inválida.")
                            else:
                                print("Créditos insuficientes. Recarregue com pelo menos 5 créditos.")
                                                                                                                            
                        elif user_option == "2":
                            print("Devolução de Bicicleta")
                            for locacao in locacoes:
                                if locacao[0] == usuario[0]:
                                    locacao.append(input("Digite a data de devolução, no formato dd/mm: "))
                                    locacao.append(input("Digite a hora de devolução, no formato hh:mm: "))
                                    data_retirada = locacao[1]
                                    hora_retirada = locacao[2]
                                    data_devolucao = locacao[3]
                                    hora_devolucao = locacao[4]
                                    minutos_retirada = minutos_totais(data_retirada, hora_retirada)
                                    minutos_devolucao = minutos_totais(data_devolucao, hora_devolucao)
                                    diferenca_minutos = minutos_devolucao - minutos_retirada
                                    horas_utilizadas = (diferenca_minutos % (24 * 60)) // 60
                                    print(horas_utilizadas)
                                    print("Devolução realizada com sucesso!")
                                    print("Tempo de utilização: ", horas_utilizadas)
                                    print("O preço do aluguel foi de R$", horas_utilizadas)
                                    usuario[2] -= horas_utilizadas
                                    break
                            else:
                                print("Nenhuma bicicleta alugada.")
                                
                        elif user_option == "3":
                            print("Consulta de Aluguéis")
                            alugueis_encontrados = False
                            for locacao in locacoes:
                                if locacao[0] == usuario[0]:
                                    print(f"Data de Retirada: {locacao[1]}")
                                    print(f"Hora de Retirada: {locacao[2]}")
                                    if len(locacao) > 3:
                                        print(f"Data de Devolução: {locacao[3]}")
                                        print(f"Hora de Devolução: {locacao[4]}")
                                    else:
                                        print("Bicicleta ainda não devolvida.")
                                    print("-" * 42)
                                    alugueis_encontrados = True
                            if not alugueis_encontrados:
                                print("Nenhum aluguel encontrado.")
                            
                        elif user_option == "4":
                            print("Recarga de Créditos")
                            credito = int(input("Digite o valor da recarga: "))
                            usuario[2] += credito
                            print("Créditos atualizados com sucesso.")
                            print(f"Novo saldo de créditos: {usuario[2]}")
                            print(f"Válidos para uso por {tempo_credito * usuario[2]} horas.")
                        
                        elif user_option == "5":
                            print("Saindo...")
                            break
                        else:
                            print("Opção inválida. Tente novamente.")
                    break
                elif usuario[0] == login and usuario[1] != senha:
                    print("Senha incorreta.")
                    break
            else:
                print("Usuário não encontrado.")
                print("Faça o cadastro.")
                
    elif option == "2":
        print("Cadastro de Usuário")
        login = input("Digite o login: ")
        senha = input("Digite a senha: ")
        for usuario in usuarios:
            if usuario[0] == login:
                print("Usuário já cadastrado.")
                break
        else:
            novo_usuario = [login, senha, 0]
            usuarios.append(novo_usuario)
            print("Usuário cadastrado com sucesso!")
                
    elif option == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
