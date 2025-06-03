import time
from arquivos import salvar_relatorio

def validar_nome(nome):
    nao_pode = ['(', ')', '[', ']', '{', '}', '<', '>', ',', ';', ':', '\\', '"', "'", '`', '\t', '\n', '!', '#',
                '$', '%', '^', '&', '*', '=', '+', '/', '?', '|', '~','@','.com','0','1','2','3','4','5','6','7','8','9']
    for caractere in nome:
        if caractere in nao_pode:
            print('VOCÊ NÃO PODE TER ESSES CARACTERES NO SEU NOME!')
            return False
    if nome == '':
        print('NÚMERO DE CARACTERES INSUFICIENTE!')
        return False
    if len(nome) < 3:
        print('NÚMERO DE CARACTERES INSUFICIENTE!')
        return False
    return True


def validar_email(usuarios, email):
    if email in usuarios:
        print('O EMAIL JA EXISTE!')
        return False
    nao_pode = ['(', ')', '[', ']', '{', '}', '<', '>', ',', ';', ':', '\\', '"', "'", '`', ' ', '\t', '\n', '!', '#',
                '$', '%', '^', '&', '*', '=', '+', '/', '?', '|', '~']
    for caractere in email:
        if caractere in nao_pode:
            print('EMAIL INVALIDO, DIGITE NOVAMENTE!')
            return False
    if '@' not in email or '.com' not in email:
        print('EMAIL INVALIDO, DIGITE NOVAMENTE!')
        return False
    else:
        partes_email = email.split('@')
        if len(partes_email) != 2 or not partes_email[0]:
            print('EMAIL INVALIDO, DIGITE NOVAMENTE!')
            return False
        else:
            dominio = partes_email[1].split('.')
            if len(dominio) < 2 or not dominio[0] or dominio[1] != 'com':
                print('EMAIL INVALIDO, DIGITE NOVAMENTE!')
                return False
            elif len(dominio) > 2:
                print('EMAIL INVALIDO, DIGITE NOVAMENTE!')
                return False
    return True


def validar_senha(senha):
    if ' ' in senha:
        print('SENHA INVALIDA. O NÚMERO DE CARACTERES NÃO É SUFICIENTE')
        return False
    if len(senha) < 8:
        print('SENHA INVALIDA. O NÚMERO DE CARACTERES NÃO É SUFICIENTE')
        return False
    return True


def validar_login(usuarios, email_user, senha_user):
    if email_user in usuarios and usuarios[email_user]['Senha'] == senha_user:
        return True
    return False


def validar_motorista(usuarios, email_user, motoristas:dict):
    while True:
        if email_user in motoristas:
            return True
        elif email_user not in motoristas:
            se_tornar_motorista = input('PARA CADASTRAR UMA CARONA, VOCÊ DEVE SE TORNAR UM MOTORISTA, GOSTARIA DE CONTINUAR?[S/N]: ').upper()[0].strip()
            while se_tornar_motorista not in 'SN':
                print('DIGITE UMA OPÇÃO VALIDA!')
                se_tornar_motorista = input('PARA CADASTRAR UMA CARONA, VOCÊ DEVE SE TORNAR UM MOTORISTA, GOSTARIA DE CONTINUAR?[S/N]: ').upper()[0].strip()
            if se_tornar_motorista == 'S':
                motoristas[email_user] = {'Nome': usuarios[email_user]['Nome'], 'Caronas': []}
                print('AGORA VOCÊ É UM MOTORISTA, CADASTRE SUA CARONA!')
                return True
            elif se_tornar_motorista == 'N':
                return False


def validar_local(local):
    if local == '':
        print('LOCAL INVALIDO!')
        return False
    return True


def validar_destino(destino, local):
    if destino == local:
        print('SEU DESTINO NÃO PODE SER IGUAL AO SEU LOCAL DE ORIGEM!')
        return False
    if destino == '':
        print('DESTINO INVALIDO!')
        return False
    return True

def validar_data(data):
    if len(data) == 10:
        dia = (data.split('/')[0])
        mes = (data.split('/')[1])
        ano = (data.split('/')[2])
        for parte in dia, mes, ano:
            for caractere in parte:
                if caractere not in '0123456789':
                    print('DATA INVÁLIDA. USE APENAS NÚMEROS!')
                    return False
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        if ano > 2025 or ano < 1930:
            print('ANO INVALIDO!')
            return False
        elif mes > 12:
            print('MÊS INVALIDO')
            return False
        elif dia < 1:
            print('DIA INVALIDO')
            return False
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia >= 1 and dia <= 31:
                return True
            else:
                print('ESSE MÊS POSSUI 31 DIAS! ')
                return False
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia >= 1 and dia <= 30:
                return True
            else:
                print('ESSE MÊS POSSUI 30!')
                return False
        elif mes == 2:
            if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                if dia <= 29:
                    return True
                else:
                    print('ESSE ANO É BISSEXTO! FEVEREIRO POSSUI 29 DIAS!')
                    return False
            elif dia <= 28:
                return True
            else:
                print('FEVEREIRO SÓ POSSUI 28 DIAS (29 SE O ANO FOR BISSEXTO!)')
                return False
    else:
        print('DATA INVALIDA. DIGITE NOVAMENTE!')
        return False


def validar_carona_mesma_data(email_user, motoristas, caronas, data):
    for id in motoristas[email_user]['Caronas']:
        if caronas[id]['Data'] == data:
            print('VOCÊ JÁ POSSUI UMA CARONA CADASTRADA NESSA DATA! TERMINE ELA ANTES DE CADASTRAR OUTRA NO MESMO DIA!')
            return False
    return True


def validar_horario(horario):
    if len(horario) == 5:
        hora, min = horario.split(':')
        for parte in hora, min:
            for caractere in parte:
                if caractere not in '0123456789':
                    print('HORA INVALIDA!. USE APENAS NÚMEROS!')
                    return False
        hora, min = int(hora), int(min)
        if hora >= 0 and hora <= 23 and min >= 0 and min <= 59:
            return True
        else:
            print('HORARIO INVALIDO. TENTE NOVAMENTE: ')
            return False
    else:
        print('HORARIO INVALIDO. TENTE NOVAMENTE: ')
        return False

def validar_vaga(vagas):
    if vagas == '':
        print('VOCÊ NÃO DIGITOU AS VAGAS!')
        return False
    if not vagas.isdigit():
        print('VAGA INVALIDA!. USE APENAS NÚMEROS (NÃO USE VALORES QUEBRADOS)!')
        return False
    vaga_convertida = int(vagas)
    if vaga_convertida <= 0:
        print('NÃO PODE TER 0 VAGAS!')
        return False
    return True

def validar_valor(valor):
    if valor == '':
        print('VOCÊ NÃO DIGITOU O VALOR!')
        return False
    if ',' in valor:
        print('USE PONTO NO LUGAR DA VIRGULA')
        return False
    ponto = 0
    for caractere in valor:
        if caractere == '.':
            ponto += 1
            if ponto > 1:
                print('VALOR INVÁLIDO! USE APENAS UM PONTO DECIMAL.')
                return False
        elif caractere not in '0123456789':
            print('VALOR INVÁLIDO! USE APENAS NÚMEROS.')
            return False
    if valor[0] == '.' or valor[-1] == '.':
        print('VALOR INVÁLIDO! NÃO PODE COMEÇAR OU TERMINAR COM PONTO.')
        return False
    valor_convertido = float(valor)
    if valor_convertido <= 0:
        print('NÃO PODE TER UMA CARONA GRÁTIS!')
        return False
    return True


def validar_carona_disponivel(caronas, motoristas):
    print('CARONAS DISPONIVEIS:')
    if len(caronas) == 0:
        print('AINDA NÃO TEM CARONAS DISPONIVEIS!')
    for carona_disponivel in caronas:
        disponivel = caronas[carona_disponivel]
        print(f'ID: {carona_disponivel} | Origem: {disponivel['Local']} | Destino: {disponivel['Destino']} | Data: {disponivel['Data']} | Horário: {disponivel['Horario']}h | Vagas: {disponivel['Vagas']} | Valor: R${disponivel['Valor']} | Motorista: {motoristas[disponivel['Motorista']]['Nome']}')


def encontrar_carona(caronas,usuarios,email_user,motoristas):
    if email_user in motoristas:
        print('VOCÊ NÃO PODE BUSCAR CARONAS COMO MOTORISTA!')
        return False
    buscar_local = input('DIGITE O LOCAL: ').strip()
    if buscar_local == '':
        print('VOCÊ PRECISA DIGITAR UM LOCAL!')
        return False
    buscar_destino = input('DIGITE O DESTINO QUE QUER BUSCAR: ').strip()
    if buscar_destino == '':
        print('VOCÊ PRECISA DIGITAR UM DESTINO!')
        return False
    for carona_ld in caronas:
        dados = caronas[carona_ld]
        if dados['Local'] == buscar_local and dados['Destino'] == buscar_destino:
            print('TEM CARONAS DISPONÍVEIS!')
            detalhes=input('GOSTARIA DE VER OS DETALHES?[S/N]: ').upper()[0].strip()
            while detalhes not in 'SN':
                print('DIGITE UMA OPÇÃO VÁLIDA!')
                detalhes = input('GOSTARIA DE VER OS DETALHES?[S/N]: ').upper()[0].strip()
            if detalhes == 'S':
                for carona_id2 in caronas:
                    d=caronas[carona_id2]
                    if d['Local'] == buscar_local and d['Destino'] == buscar_destino:
                        print(f'ID: {carona_id2} |Email Do Motorista: {d['Motorista']} | Origem: {d['Local']} | Destino: {d['Destino']} | Data: {d['Data']} | Horário: {d['Horario']}h | Vagas: {d['Vagas']} | Valor: R${d['Valor']} | Motorista: {motoristas[d['Motorista']]['Nome']}')
                reservar = input('GOSTARIA DE RESERVAR UMA DESTAS CARONAS?[S/N]: ').upper()[0].strip()
                while reservar not in 'SN':
                    print('DIGITE UMA OPÇÃO VÁLIDA!')
                    reservar = input('GOSTARIA DE RESERVAR UMA DESTAS CARONAS?[S/N]: ').upper()[0].strip()
                if reservar=='S':
                    id_reserva = input('DIGITE O ID DA CARONA QUE DESEJA RESERVAR: ').strip()
                    if not id_reserva.isdigit():
                        print('ID INVÁLIDO! DEVE SER UM NÚMERO INTEIRO.')
                        return False
                    id_reserva_int = int(id_reserva)
                    if id_reserva_int not in caronas:
                        print('ID INVÁLIDO! CARONA NÃO ENCONTRADA.')
                        return False
                    dados_reserva = caronas[id_reserva_int]
                    if dados_reserva['Vagas'] == 0:
                        print('NÃO É POSSÍVEL RESERVAR. TODAS AS VAGAS JÁ FORAM PREENCHIDAS!')
                        return False
                    if dados_reserva['Motorista'] == email_user:
                        print('VOCÊ NÃO PODE FAZER UMA RESERVA SENDO MOTORISTA!')
                        return False
                    reserva_email = input('DIGITE O EMAIL DO MOTORISTA: ').strip()
                    data_carona = input('DIGITE A DATA DA CARONA [DD/MM/AAAA]: ').strip()
                    if reserva_email != dados_reserva['Motorista'] or data_carona != dados_reserva['Data']:
                        print('EMAIL OU DATA INCORRETOS! RESERVA NÃO EFETUADA.')
                        return False
                    valor_original = float(dados_reserva['Valor'])
                    num_reservas = len(usuarios[email_user]['Reservas'])
                    if num_reservas >= 2:
                        desconto=valor_original * 0.10
                        valor_com_desconto = valor_original-desconto
                        print(f'VOCÊ POSSUI MAIS DE 2 CARONAS RESERVADAS E GANHOU UM DESCONTO DE 10%! O VALOR A PAGAR É R${valor_com_desconto:.2f}')
                    else:
                        valor_com_desconto=valor_original
                    pago = input('DIGITE O VALOR A SER PAGO NA PASSAGEM: ').strip()
                    while not validar_valor(pago):
                        pago=input('VALOR INVÁLIDO. DIGITE NOVAMENTE: ').strip()
                    pagar = float(pago)
                    if pagar == valor_com_desconto:
                        caronas[id_reserva_int]['Vagas'] = int(caronas[id_reserva_int]['Vagas']) - 1
                        usuarios[email_user]['Reservas'].append(id_reserva_int)
                        caronas[id_reserva_int]['Passageiros'].append(email_user)
                        print(f'CARONA RESERVADA COM SUCESSO PARA {usuarios[email_user]['Nome'].upper()}')
                    elif pagar<valor_com_desconto:
                        print(f'VALOR INSUFICIENTE. A CARONA CUSTA R${valor_com_desconto:.2f}')
                        return False
                    elif pagar > valor_com_desconto:
                        troco = pagar-valor_com_desconto
                        caronas[id_reserva_int]['Vagas'] = int(caronas[id_reserva_int]['Vagas']) - 1
                        usuarios[email_user]['Reservas'].append(id_reserva_int)
                        caronas[id_reserva_int]['Passageiros'].append(email_user)
                        print(f'CARONA RESERVADA COM SUCESSO PARA {usuarios[email_user]['Nome'].upper()}')
                        print(f'TROCO: R${troco:.2f}')
                elif reservar == 'N':
                    return False
            elif detalhes == 'N':
                return False
            return True
    print('NÃO TEM CARONAS PARA ESSES LOCAIS!')
    return False


def cancelar_reserva(email_user, usuarios, caronas, motoristas):
    if email_user in motoristas:
        print('VOCÊ NÃO PODE CANCELAR UMA RESERVA SENDO MOTORISTA!')
        return False
    email_passageiro = input('DIGITE O SEU EMAIL PARA CANCELAR A RESERVA: ').strip()
    if email_user == email_passageiro:
        for id_carona in caronas:
            dados = caronas[id_carona]
            if email_user in dados['Passageiros']:
                dados['Passageiros'].remove(email_user)
                dados['Vagas'] += 1
                if id_carona in usuarios[email_user]['Reservas']:
                    usuarios[email_user]['Reservas'].remove(id_carona)
                print(f'RESERVA CANCELADA! ID Carona: {id_carona} | VAGAS AGORA: {dados['Vagas']}')
                return True
            else:
                print('VOCÊ NÃO POSSUI NENHUMA RESERVA PARA CANCELAR.')
                return False
    else:
        print('O EMAIL INFORMADO NÃO CORRESPONDE AO USUÁRIO LOGADO!')
        return False


def remover_carona(caronas, motoristas, email_user):
    if email_user not in motoristas:
        print('VOCÊ PRECISA SER UM MOTORISTA PARA REMOVER A CARONA!')
        return False
    data_remover = input('DIGITE A DATA DA CARONA QUE VOCÊ QUER REMOVER [DD/MM/AAAA]: ').strip()
    for carona_id in motoristas[email_user]['Caronas']:
        if caronas[carona_id]['Data'] == data_remover:
            del caronas[carona_id]
            motoristas[email_user]['Caronas'].remove(carona_id)
            print('CARONA REMOVIDA COM SUCESSO!')
            return True
    print('NENHUMA CARONA SUA ENCONTRADA NESSA DATA!')
    return False


def ver_caronas(email_user, motoristas, caronas,):
    if email_user not in motoristas or len(motoristas[email_user]['Caronas']) == 0:
        print('VOCÊ AINDA NÃO CADASTROU NENHUMA CARONA!')
    else:
        print('SUAS CARONAS CADASTRADAS:')
        for carona_id in motoristas[email_user]['Caronas']:
            carona = caronas[carona_id]
            print(f'ID: {carona_id} | Origem: {carona['Local']} | Destino: {carona['Destino']} | Data: {carona['Data']} | Horário: {carona['Horario']}h | Vagas: {carona['Vagas']} | Valor: R${carona['Valor']} | Passageiros: {carona['Passageiros']}')


def relatorio_totalizador(email_user, motoristas, caronas,):
    if email_user not in motoristas or len(motoristas[email_user]['Caronas']) == 0:
        print('VOCÊ AINDA NÃO CADASTROU NENHUMA CARONA!')
    else:
        print('SUAS CARONAS CADASTRADAS:')
        totalizador = 0
        for carona_id in motoristas[email_user]['Caronas']:
            carona = caronas[carona_id]
            print(f'ID: {carona_id} | Origem: {carona['Local']} | Destino: {carona['Destino']} | Data: {carona['Data']} | Horário: {carona['Horario']}h | Vagas: {carona['Vagas']} | Valor: R${carona['Valor']} | Passageiros: {carona['Passageiros']} | Total: R${float(carona['Valor']) * len(carona['Passageiros'])}')
            if len(carona['Passageiros']) != 0:
                totalizador += float(carona['Valor'])
                print(f'VALOR DE TODAS AS CARONAS R${totalizador}')
            relatorio = input('DESEJA SALVAR ESSE RELATORIO EM UM ARQUIVO?[S/N]: ').upper()[0].strip()
            while relatorio not in 'SN':
                print('DIGITE UMA OPÇÃO VÁLIDA!')
                relatorio = input('DESEJA SALVAR ESSE RELATORIO EM UM ARQUIVO?[S/N]: ').upper()[0].strip()
            if relatorio == 'S':
                salvar_relatorio(motoristas, email_user, caronas)
                print('OBRIGADO POR SALVAR!')
            elif relatorio == 'N':
                return False




def ver_reservas(usuarios, email_user, caronas, motoristas):
    if email_user in motoristas:
        print('VOCÊ NÃO PODE VER AS RESERVAS DOS PASSAGEIROS')
        return False
    if not usuarios[email_user]['Reservas']:
        print('VOCÊ NÃO TEM NENHUMA CARONA RESERVADA.')
    else:
        print('SUAS CARONAS RESERVADAS:')
        for cod in usuarios[email_user]['Reservas']:
            if cod in caronas:
                dados = caronas[cod]
                print(f'ID: {cod} | Origem: {dados['Local']} | Destino: {dados['Destino']} | Data: {dados['Data']} | Horário: {dados['Horario']}h | Valor: R${dados['Valor']} | Motorista: {motoristas[dados['Motorista']]['Nome']}')
            else:
                print(f'ID: {cod} | ESTA CARONA FOI CANCELADA PELO MOTORISTA.')



def finalizar_carona(caronas, motoristas, email_user):
    if email_user not in motoristas:
        print('VOCÊ PRECISA SER UM MOTORISTA PARA FINALIZAR UMA CARONA!')
        return False
    finalizar = input('DIGITE O ID DA CARONA QUE DESEJA FINALIZAR: ').strip()
    if not finalizar.isdigit():
        print('ID INVÁLIDO!')
        return False
    finalizar = int(finalizar)
    if finalizar not in caronas:
        print('CARONA NÃO EXISTE!')
        return False
    if finalizar not in motoristas[email_user]['Caronas']:
        print('ESSA CARONA NÃO É SUA!')
        return False
    print('FINALIZANDO CARONA', end='', flush=True)
    for _ in range(3):
        time.sleep(0.7)
        print('.', end='', flush=True)
    print()
    motoristas[email_user]['Caronas'].remove(finalizar)
    del caronas[finalizar]
    print('CARONA FINALIZADA COM SUCESSO!')