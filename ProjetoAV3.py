from validar import *
from menus import *
from arquivos import *


usuarios = {'rene@gmail.com':{'Email': 'rene@gmail.com','Senha': 'rene12345', 'Nome': 'rene de sousa', 'Reservas': []}, 'mrarthur@gmail.com':{'Email': 'mrarthur@gmail.com','Senha': 'arthur12345', 'Nome': 'arthur', 'Reservas': []}}
arquivo = open('Usuarios.txt', 'a')
arquivo.close()
carregar_usuarios(usuarios)
adm = {'mrarthur@gmail.com':{'Email': 'mrarthur@gmail.com','Senha': 'arthur12345', 'Nome': 'arthur'}}
caronas = {}
motoristas = {'igris@gmail.com': {'Nome': 'igrito', 'Senha': 'igritochad', 'Caronas': []}, 'mrarthur@gmail.com': {'Nome': 'arthur', 'Senha': 'arthur12345', 'Caronas':[]}}
carona_id = 1


while True:
    op = menu1()
    if op == 1:
        nome = input('DIGITE O SEU NOME: ').strip()
        while not validar_nome(nome):
            nome = input('DIGITE O SEU NOME NOVAMENTE: ').strip()
        email = input('DIGITE SEU EMAIL: ').strip()
        while not validar_email(usuarios, email, adm, motoristas):
            email = input('DIGITE SEU EMAIL: ').strip()
        senha = input('DIGITE UMA SENHA: ').strip()
        while not validar_senha(senha):
            senha = input('DIGITE UMA SENHA: ').strip()
        usuarios[email] = {'Email': email, 'Senha': senha, 'Nome': nome, 'Reservas': []}
        salvar_usuarios(usuarios)
        print('CADASTRO REALIZADO COM SUCESSO!')
    elif op == 2:
            email_user = input('DIGITE SEU LOGIN: ').strip()
            senha_user = input('DIGITE SUA SENHA: ').strip()
            if not validar_login(usuarios, email_user, senha_user):
                print('SEU LOGIN ESTÁ INCORRETO! TENTE NOVAMENTE OU FAÇA O CADASTRO!')
            elif not validar_nao_motorista(email_user, motoristas):
                continue
            else:
                print(f'LOGIN REALIZADO COM SUCESSO! BEM-VINDO, {usuarios[email_user]['Nome'].upper()}')
                while True:
                    op2 = menu2()
                    if op2 == 1:
                       validar_carona_disponivel(caronas, motoristas)
                    elif op2 == 2:
                        encontrar_carona(caronas, usuarios, email_user, motoristas)
                    elif op2 == 3:
                        cancelar_reserva(email_user, usuarios, caronas)
                    elif op2 == 4:
                        ver_reservas(usuarios, email_user, caronas, motoristas)
                    elif op2 == 0:
                        print('VOLTE SEMPRE! S2')
                        break
    elif op == 0:
        print('ATÉ OUTRA HORA <3')
        break
    elif op == 3:
        email_user = input('DIGITE SEU LOGIN DE MOTORISTA: ').strip()
        senha_user = input('DIGITE SUA SENHA DE MOTORISTA: ').strip()
        if not validar_motorista(email_user, senha_user, motoristas):
            continue
        else:
            print(f'LOGIN REALIZADO COM SUCESSO! BEM-VINDO, {motoristas[email_user]['Nome'].upper()}')
            while True:
                op3 = menu3()
                if op3 == 1:
                    if not validar_motorista(email_user, senha_user, motoristas):
                        continue
                    local = input('DIGITE O LOCAL DE ORIGEM DA CARONA: ').strip()
                    while not validar_local(local):
                        local = input('DIGITE O LOCAL DE ORIGEM DA CARONA NOVAMENTE!: ').strip()
                    destino = input('DIGITE O DESTINO DA CARONA: ').strip()
                    while not validar_destino(destino, local):
                        destino = input('DIGITE O DESTINO DA CARONA NOVAMENTE!: ').strip()
                    data = input('DIGITE A DATA DA CARONA [DD/MM/AAAA]: ')
                    while not validar_data(data):
                        data = input('DIGITE A DATA DA CARONA NOVAMENTE! [DD/MM/AAAA]: ')
                    if not validar_carona_mesma_data(email_user, motoristas, caronas, data):
                        continue
                    horario = input('DIGITE O HORARIO DA CARONA [HH:MM]: ')
                    while not validar_horario(horario):
                        horario = input('DIGITE O HORARIO DA CARONA NOVAMENTE! [HH:MM]: ')
                    vagas = input('DIGITE A QUANTIDADE DE VAGAS: ').strip()
                    while not validar_vaga(vagas):
                        vagas = input('DIGITE A QUANTIDADE DE VAGAS NOVAMENTE!: ').strip()
                    valor = input('DIGITE O VALOR POR VAGAS: ').strip()
                    while not validar_valor(valor):
                        valor = input('DIGITE O VALOR POR VAGAS NOVAMENTE!: ').strip()
                    caronas[carona_id] = {'Local': local, 'Destino': destino, 'Data': data, 'Horario': horario,
                                          'Vagas': vagas, 'Valor': valor, 'Motorista': email_user, 'Passageiros': []}
                    motoristas[email_user]['Caronas'].append(carona_id)
                    print(f'{carona_id} CARONA CADASTRADA COM SUCESSO!')
                    carona_id += 1
                elif op3 == 2:
                    remover_carona(caronas, motoristas, email_user)
                elif op3 == 3:
                    ver_caronas(email_user, motoristas, caronas)
                elif op3 == 4:
                    relatorio_totalizador(email_user, motoristas, caronas)
                elif op3 == 5:
                    finalizar_carona(caronas, motoristas, email_user)
                elif op3 == 0:
                    print('VOLTE SEMPRE! S2')
                    break
    elif op == 4:
        if not login_adm(adm):
            print('LOGIN INCORRETO!')
            continue
        while True:
            op4 = menu4()
            if op4 == 1:
                remover_usuario(usuarios, caronas)
            elif op4 == 2:
                cadastrar_motorista(usuarios, motoristas)
            elif op4 == 0:
                print('VOLTE SEMPRE SR!')
                break