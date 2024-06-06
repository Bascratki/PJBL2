usuarios = [["lucas", "1234", 0], ["joao", "1234", 0]] # matriz de usuario = [login, senha, creditos]
locacoes_efetuadas = [[],[]] #matriz de locacoes efetuadas = [login, data_retirada, hora_retirada , data de devolucao, hora da devolucao]
locacoes = [["", "", "", "","",""],["", "", "", "","",""]]  #matriz de registro de locacoes = [login, data_retirada, hora_retirada , data de devolucao, hora da devolucao]

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
    dia, mes, ano = map(int, data.split('/'))
    hora, minuto = map(int, hora.split(':'))
    
    # Calcular dias no mês (considerando um ano bissexto simplificado)
    dias_por_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Calcular total de minutos até a data e hora fornecida
    minutos_totais = minuto + hora * 60
    minutos_totais += (dia - 1) * 24 * 60
    minutos_totais += sum(dias_por_mes[:mes-1]) * 24 * 60
    minutos_totais += (ano - 1) * 365 * 24 * 60
    minutos_totais += ((ano - 1) // 4) * 24 * 60  # Considerar anos bissextos
    
    return minutos_totais


            
def fazer_locacao(usuario):
    #funcao que recebe como parametro o indice do usuario na lista usuarios[] que esta realizando a locacao
    #realiza a locacao de uma bicicleta para um usuario e atualiza a matriz de locacoes
    if locacoes[usuario] == ["", "", "", "","",""]:
            dia_retirada = input("digite o dia de retirada, no formato dd: ")
            mes_retirada = input("diite o mês de retirada, no formato mm: ")
            ano_retirada = input("digite o ano de retirada, no formato aaaa: ")
            hora_retirada = input("digite a hora de retirada, no formato hh: ")
            minuto_retirada = input("digite o minuto de retirada, no formato mm: ")
            #avalia se a data e hora digitadas são válidas
            if len(dia_retirada) == 2 and len(mes_retirada) == 2 and len(ano_retirada) == 4 and len(hora_retirada) == 2 and len(minuto_retirada) == 2:
                if (int(dia_retirada) < 31 and int(dia_retirada) > 0) and (int(mes_retirada) > 0 and int(mes_retirada) <= 12):
                    if (int(hora_retirada) >= 0 and int(hora_retirada) < 24) and (int(minuto_retirada) >= 0 and int(minuto_retirada) < 60):
                        data_retirada = dia_retirada + "/" + mes_retirada + "/" + ano_retirada
                        hora_retirada = hora_retirada + ":" + minuto_retirada
                    
                        locacoes[usuario] = [usuarios[usuario][0], data_retirada, hora_retirada, "", ""]
                    else:
                        return False
                else:
                    return False
            else:
                return False

def fazer_devolucao(usuario):
    #recebe como parametro o indice do usuario na lista usuarios[] que esta realizando a devolucao
    #funcao que realiza a devolucao de uma bicicleta para um usuario e atualiza a matriz de locacoes
        if locacoes[usuario] == ["", "", "", "","",""]:
            return False
        else:
            dia_devolucao = input("digite o dia de devolução, no formato dd: ")
            mes_devolucao = input("digite o mês de devolução, no formato mm: ")
            ano_devolucao = input("digite o ano de devolução, no formato aaaa: ")
            hora_devolucao = input("digite a hora de devolução, no formato hh: ")
            minuto_devolucao = input("digite o minuto de devolução2, no formato mm: ")

            data_devolucao = dia_devolucao + "/" + mes_devolucao + "/" + ano_devolucao
            hora_retirada = hora_devolucao + ":" + minuto_devolucao
            if len(dia_devolucao) == 2 and len(mes_devolucao) == 2 and len(ano_devolucao) == 4 and len(hora_devolucao) == 2 and len(minuto_devolucao) == 2:
                if (int(dia_devolucao) < 31 and int(dia_devolucao) > 0) and (int(mes_devolucao) > 0 and int(mes_devolucao) <= 12):
                    if (int(hora_devolucao) >= 0 and int(hora_devolucao) < 24) and (int(minuto_devolucao) >= 0 and int(minuto_devolucao) < 60):
                        data_devolucao = f"{dia_devolucao} + '/' + {mes_devolucao} + '/' + {ano_devolucao}"
                        hora_devolucao = f"{hora_devolucao} + ':' + {minuto_devolucao}"
                        locacoes[usuario][0] = usuarios[usuario][0]
                        locacoes[usuario][3] = data_devolucao
                        locacoes[usuario][4] = hora_devolucao
                        data_retirada = locacoes[usuario][1]
                        hora_retirada = locacoes[usuario][2]
                        minutos_retirada = converter_para_minutos_totais(data_retirada, hora_retirada)
                        minutos_devolucao = converter_para_minutos_totais(data_devolucao, hora_devolucao)
                        diferenca_minutos = minutos_devolucao - minutos_retirada
                        horas_utilizadas = (diferenca_minutos % (24 * 60)) // 60

                        locacoes_efetuadas[usuario] += [usuarios[usuario][0],data_retirada, hora_retirada, data_devolucao, hora_devolucao]
                        print("horas utilizadas:", horas_utilizadas)
                        print("devolução realizada com sucesso!")
                        print("hora de devolução:", locacoes[usuario][2])

                        locacoes[usuario] = []
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
        print("não há locações realizadas.")
        return False
    elif locacoes[usuario] == ["", "", "", "","",""]:
        print("não há locações em andamento.")
        return False

    if locacoes[usuario][3] != "":
        print("data de devolução estimada:", locacoes[usuario][3])
        print("hora de devolução estimada:", locacoes[usuario][4])
    else:
        print("locação ainda em andamento")

    print("relatório de locações ja realizadas:")
    for locacao_efetuada in range(len(locacoes_efetuadas[usuario])) :
        print("usuário:", locacoes_efetuadas[usuario][locacao_efetuada][0])
        print("data de retirada:", locacoes_efetuadas[usuario][locacao_efetuada][1])
        print("hora de retirada:", locacoes_efetuadas[usuario][locacao_efetuada][2])
        print("data de devolução:", locacoes_efetuadas[usuario][locacao_efetuada][3])
        print("hora de devolução:", locacoes_efetuadas[usuario][locacao_efetuada][4])
    print("relatório da locação atual:")
    print("usuário:", locacoes[usuario][0])
    print("data de retirada:", locacoes[usuario][1])
    print("hora de retirada:", locacoes[usuario][1][0:2])
  
def login_usuario():
    #funcao que pede para o usuario digitar um nome de login e uma senha
    #realiza o login de um usuario e retorna o indice do usuario na lista usuarios[], o login e a senha do usuario
    login = input("digite o login do usuário: ")
    senha = input("digite a senha do usuário: ")
    for usuario in range(len(usuarios)):
        if usuarios[usuario][0] == login and usuarios[usuario][1] == senha:
            return usuario, login, senha
        
    return False, False, False