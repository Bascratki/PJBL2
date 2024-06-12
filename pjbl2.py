usuarios = [["lucas", "1234", 0], ["joao", "1234", 0]] # matriz de usuario = [login, senha, creditos]
locacoes_efetuadas = [[],[]] #matriz de locacoes efetuadas = [login, data_retirada, hora_retirada , data de devolucao, hora da devolucao]
locacoes = [["", "", ""],["", "", ""]]  #matriz de registro de locacoes = [login, data_retirada, hora_retirada ]

def cadastrar_usuario():
    #funcao que recebe um nome de login e uma senha
    #adiciona um novo usuario a matriz de usuarios[login, senha, creditos]
    login = input("digite o login do usuário: ")
    senha = input("digite a senha do usuário: ")
    for usuario in range(len(usuarios)):
        if usuarios[usuario][0] == login:
            existe = False
            return existe
    usuarios.append([login, senha, 0])
    locacoes.append(["", "", "", "","",""])
    locacoes_efetuadas.append([])
    return login, senha

def atualizar_creditos(usuario):
    #funcao que recebe o indice do usuario na lista usuarios[] e atualiza o saldo de creditos do usuario
    #funcao que atualiza o saldo de creditos de um usuario
    valor_adicionar = int(input("digite quanto quer adicionar: "))
    if valor_adicionar < 0:
        print("valor inválido. Digite um valor maior que 0.")
        atualizar_creditos(usuario)
    usuarios[usuario][2] += valor_adicionar

def converter_para_minutos_totais(data, hora):
    #funcao que recebe uma data e uma hora e converte para minutos totais para facilitar o calculo de horas utilizadas
    #funcao que converte uma data e hora para minutos totais


    dia = 0
    mes = 0
    ano = 0
    hora_num = 0
    minuto = 0

    # Extraindo dia, mês e ano da data (formato: "dd/mm/aaaa")
    i = 0
    while data[i] != '/':
        dia = dia * 10 + int(data[i])
        i += 1
    i += 1
    while data[i] != '/':
        mes = mes * 10 + int(data[i])
        i += 1
    i += 1
    while i < len(data):
        ano = ano * 10 + int(data[i])
        i += 1

    # Extraindo hora e minuto da hora (formato: "hh:mm")
    i = 0
    while hora[i] != ':':
        hora_num = hora_num * 10 + int(hora[i])
        i += 1
    i += 1
    while i < len(hora):
        minuto = minuto * 10 + int(hora[i])
        i += 1

    # Calcular dias no mês 
    dias_por_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Calcular total de minutos até a data e hora fornecida
    minutos_totais = minuto + hora_num * 60
    minutos_totais += (dia - 1) * 24 * 60

# Somar os minutos de cada mês anterior
    minutos_meses_anteriores = 0
    for i in range(mes - 1):
        minutos_meses_anteriores += dias_por_mes[i] * 24 * 60
    minutos_totais += minutos_meses_anteriores

    # Adicionar os minutos de cada ano anterior
    minutos_anos_anteriores = 0
    for i in range(ano - 1):
        if is_bissexto(i + 1):
            minutos_anos_anteriores += 366 * 24 * 60
        else:
            minutos_anos_anteriores += 365 * 24 * 60
    minutos_totais += minutos_anos_anteriores

    # Considerar anos bissextos adicionais
    minutos_totais += ((ano - 1) // 4) * 24 * 60

    # Excluir minutos correspondentes aos anos bissextos que foram contados duas vezes
    minutos_totais -= ((ano - 1) // 100) * 24 * 60
    minutos_totais += ((ano - 1) // 400) * 24 * 60
    return minutos_totais
         
        

def is_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False
    

def validar_data(dia, mes, ano):
    #funcao que recebe um dia, mes e ano e verifica se a data é válida
    #retorna True se a data for válida e False caso contrário

    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    
    if mes < 1 or mes > 12:
        return False
    if dia < 1:
        return False
    
    # Dias máximos em cada mês
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return dia <= 31
    elif mes in [4, 6, 9, 11]:
        return dia <= 30
    elif mes == 2:
        if is_bissexto(ano):
            return dia <= 29
        else:
            return dia <= 28
    return False





def fazer_locacao(usuario):
    #funcao que recebe como parametro o indice do usuario na lista usuarios[] que esta realizando a locacao
    #realiza a locacao de uma bicicleta para um usuario e atualiza a matriz de locacoes   
            dia_retirada = input("Digite o dia de retirada, no formato dd 01 - 31: ")
            mes_retirada = input("Digite o mês de retirada, no formato mm 01 - 12: ")
            ano_retirada = input("Digite o ano de retirada, no formato aaaa: ")
            hora_retirada = input("Digite a hora de retirada, no formato 00 - 23: ")
            minuto_retirada = input("Digite o minuto de retirada, no formato mm 00 - 59: ")
            #avalia se a data e hora digitadas são válidas

            if len(dia_retirada) == 2 and len(mes_retirada) == 2 and len(ano_retirada) == 4 and len(hora_retirada) == 2 and len(minuto_retirada) == 2:
                if validar_data(dia_retirada, mes_retirada, ano_retirada):
                    if int(hora_retirada) >= 0 and int(hora_retirada) < 24 and int(minuto_retirada) >= 0 and int(minuto_retirada) < 60:
                        data_retirada = dia_retirada + "/" + mes_retirada + "/" + ano_retirada
                        hora_retirada = hora_retirada + ":" + minuto_retirada
                    
                        locacoes[usuario] = [usuarios[usuario][0], data_retirada, hora_retirada]
                        return True
                    else:
                        print("Hora inválida. Tente novamente.")
                        return False

                else:
                    print("Data inválida. Tente novamente.")
                    return False
            else:
                print("quantidade Data ou hora inválida. Tente novamente.")
                return False

def fazer_devolucao(usuario):
    #recebe como parametro o indice do usuario na lista usuarios[] que esta realizando a devolucao
    #funcao que realiza a devolucao de uma bicicleta para um usuario e atualiza a matriz de locacoes
        if locacoes[usuario] == ["", "", ""]:
            return "Vazio"
        else:
            dia_devolucao = input("Digite o dia de devolução, no formato dd 01 - 31: ")
            mes_devolucao = input("Digite o mês de devolução, no formato mm 01 - 12: ")
            ano_devolucao = input("Digite o ano de devolução, no formato aaaa:  ")
            hora_devolucao = input("Digite a hora de devolução, no formato hh 00 - 23: ")
            minuto_devolucao = input("Digite o minuto de devolução, no formato mm 00 - 59: ")
            
            data_devolucao = dia_devolucao + "/" + mes_devolucao + "/" + ano_devolucao
            horario_devolucao = hora_devolucao + ":" + minuto_devolucao
            if len(dia_devolucao) == 2 and len(mes_devolucao) == 2 and len(ano_devolucao) == 4 and len(hora_devolucao) == 2 and len(minuto_devolucao) == 2:
                if validar_data(dia_devolucao, mes_devolucao, ano_devolucao):
                    if (int(hora_devolucao) >= 0 and int(hora_devolucao) < 24) and (int(minuto_devolucao) >= 0 and int(minuto_devolucao) < 60):
                        
                        


                        data_retirada = locacoes[usuario][1]
                        hora_retirada = locacoes[usuario][2]
                        print("data de retirada:", data_retirada)
                        print("hora de retirada:", hora_retirada)
                        print("data de devolução:", data_devolucao)
                        print("hora de devolução:", horario_devolucao)
                        minutos_retirada = converter_para_minutos_totais(data_retirada, hora_retirada)
                        minutos_devolucao = converter_para_minutos_totais(data_devolucao, horario_devolucao)


                        diferenca_minutos = minutos_devolucao - minutos_retirada
                        print("diferença de minutos:", diferenca_minutos)
                        horas = diferenca_minutos // 60  
                        resto_minutos = diferenca_minutos % 60
                        horas_utilizadas = horas + (resto_minutos / 60)


                        locacoes_efetuadas[usuario] += [usuarios[usuario][0],data_retirada, hora_retirada, data_devolucao, hora_devolucao]
                        print("horas utilizadas:", horas_utilizadas)
                        print("devolução realizada com sucesso!")
                        print("hora de devolução:", locacoes_efetuadas[usuario][2])

                        locacoes[usuario] = ["", "", ""]
                        usuarios[usuario][2] -= horas_utilizadas
                        if usuarios[usuario][2] < 0:
                            print("Você precisa pagar a diferença de horas utilizadas no valor de: ", -usuarios[usuario][2])
                            usuarios[usuario][2] = 0

                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

def imprimir_relatorio(usuario):
    #funcao que recebe o indice do usuario na lista usuarios[] e
    #imprime um relatorio de todas as locacoes realizadas ate o momento
    if locacoes_efetuadas == []:
        print("Não há locações realizadas anteriormente.")

    if locacoes[usuario] == ["", "", ""]:
        print("Não há locações em andamento.")
    else:
        print("relatório da locação atual:")
        print("usuário:", locacoes[usuario][0])
        print("data de retirada:", locacoes[usuario][1])
        print("hora de retirada:", locacoes[usuario][2])
        

  


    print("Relatório de locações anteriores: ")
    if locacoes_efetuadas[usuario] == []:
        print("Não há locações anteriores.")
    else:
        for locacao_efetuada in range(len(locacoes_efetuadas[usuario])) :
            print("Usuário:", locacoes_efetuadas[usuario][locacao_efetuada][0])
            print("Data de retirada:", locacoes_efetuadas[usuario][locacao_efetuada][1])
            print("Hora de retirada:", locacoes_efetuadas[usuario][locacao_efetuada][2])
            print("Data de devolução:", locacoes_efetuadas[usuario][locacao_efetuada][3])
            print("Hora de devolução:", locacoes_efetuadas[usuario][locacao_efetuada][4])

  
def login_usuario():
    #funcao que pede para o usuario digitar um nome de login e uma senha
    #realiza o login de um usuario e retorna o indice do usuario na lista usuarios[], o login e a senha do usuario
    login = input("Login: ")
    senha = input("Senha: ")
    for usuario in range(len(usuarios)):
        if usuarios[usuario][0] == login and usuarios[usuario][1] == senha:
            return usuario, login, senha
        
    return False, False, False

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
        indice_usuario, login, senha = login_usuario()

        if (login and senha):
            while True:
                print("-" * 42)
                print("Bem-vindo ao Menu do Usuário")
                print("-" * 42)
                print("Usuário:", login)
                print("Créditos:", usuarios[indice_usuario][2])
                print("-" * 42)
                print("[1] Alugar Bicicleta")
                print("[2] Devolver Bicicleta")
                print("[3] Consulta de Aluguéis")
                print("[4] Recarga de Créditos")
                print("[5] Sair")
                print("-" * 42)
                
                opcao_usuario = input("Opção: ")
                
                if opcao_usuario == "1":
                    if usuarios[indice_usuario][2] >= 5:
                        locacao = fazer_locacao(indice_usuario)
                        if locacao:
                            print("Locação realizada com sucesso.")
                        else:
                            print("Data ou hora inválida. Tente novamente.")

                            continue

                    else:
                        print("Você precisa de pelo menos 5 créditos.")
                elif opcao_usuario == "2":
                    devolucao = fazer_devolucao(indice_usuario)
                    if devolucao == "Vazio":
                        print("Você não possui uma locação em andamento.")
                    if devolucao == False:
                        print("Voce digitou uma data ou hora inválida. Tente novamente.")
                        continue

                    
                elif opcao_usuario == "3":
                    imprimir_relatorio(indice_usuario)
                elif opcao_usuario == "4":
                    
                    atualizar_creditos(indice_usuario)
                    print("Créditos atualizados com sucesso para o usuário", login)
                    print("Novo saldo de créditos:", usuarios[indice_usuario][2])
                    
                elif opcao_usuario == "0":
                    print("Voltando...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
                    continue
        else:
            print("Falha no login. Tente novamente.")
            continue

    elif opcao == "2":
        cadastrou_usuario = cadastrar_usuario()
        if not cadastrou_usuario:
            print("Usuário já cadastrado.")
        else:
            print("Usuário cadastrado com sucesso.")

    elif opcao == "3":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        
