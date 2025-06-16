def menu1():
    while True:
        print('-=' * 13)
        print()
        print('[BEM-VINDO Á RDZ VIAGENS!]    ')
        print()
        print('-=' * 13)
        print()
        print('[1] - CADASTRAR USUÁRIO ')
        print('[2] - FAZER LOGIN ')
        print('[3] - MENU DO MOTORISTA')
        print('[4] - MENU DE ADMIN')
        print('[0] - SAIR DO PROGRAMA ')
        print()
        print('-=' * 13)
        print()
        op = input('DIGITE A OPÇÃO DESEJADA ^-^: ')
        print()
        if op.isdigit():
            return int(op)

        else:
            print('OPÇÃO INVÁLIDA! DIGITE 0, 1, 2, 3 OU 4.')


def menu2():
    while True:
        print('-=' * 10)
        print()
        print('  [MENU DO USUARIO]  ')
        print()
        print('-=' * 10)
        print()
        print('[1] - LISTAR CARONAS DISPONÍVEIS ')
        print('[2] - BUSCAR E RESERVAR CARONA')
        print('[3] - CANCELAR RESERVA')
        print('[4] - SUAS RESERVAS')
        print('[0] - LOGOUT ')
        print()
        print('-=' * 10)
        print()
        op2 = input('ESCOLHA A OPÇÃO DESEJADA ^-^: ')
        print()
        if op2.isdigit():
            return int(op2)

        else:
            print('OPÇÃO INVÁLIDA! DIGITE 0, 1, 2, 3, OU 4.')


def menu3():
    while True:
        print('-=' * 12)
        print()
        print('  [MENU DO MOTORISTA]  ')
        print()
        print('-=' * 12)
        print()
        print('[1] - CADASTRAR CARONA ')
        print('[2] - REMOVER CARONA')
        print('[3] - SUAS CARONAS')
        print('[4] - RELATORIO TOTALIZADOR')
        print('[5] - FINALIZAR CARONA [ SIMULAÇÃO <3 ]')
        print('[0] - LOGOUT ')
        print()
        print('-=' * 12)
        print()
        op3 = input('ESCOLHA A OPÇÃO DESEJADA ^-^: ')
        print()
        if op3.isdigit():
            return int(op3)

        else:
            print('OPÇÃO INVÁLIDA! DIGITE 0, 1, 2, 3, 4, OU 5.')



def menu4():
    while True:
        print('-=' * 14)
        print()
        print('[BEM-VINDO AO MENU DE ADMIN!]    ')
        print()
        print('-=' * 14)
        print()
        print('[1] - REMOVER USUARIO ')
        print('[2] - CADASTRAR MOTORISTA ')
        print('[0] - VOLTAR')
        print()
        print('-=' * 14)
        print()
        op4 = input('DIGITE A OPÇÃO DESEJADA ^-^: ')
        print()
        if op4.isdigit():
            return int(op4)

        else:
            print('OPÇÃO INVÁLIDA! DIGITE O, 1 OU 2.')