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
        print('[3] - SAIR DO PROGRAMA ')
        print('[4] - MENU DE ADMIN')
        print()
        print('-=' * 13)
        print()
        op = input('DIGITE A OPÇÃO DESEJADA ^-^: ')
        print()
        if op.isdigit():
            return int(op)
        else:
            print('OPÇÃO INVÁLIDA! DIGITE 1, 2, 3 OU 4.')


def menu2():
    while True:
        print('-=' * 10)
        print()
        print('  [MENU DO USUÁRIO]  ')
        print()
        print('-=' * 10)
        print()
        print('[1] - CADASTRAR CARONA ')
        print('[2] - LISTAR CARONAS DISPONÍVEIS ')
        print('[3] - BUSCAR E RESERVAR CARONA')
        print('[4] - CANCELAR RESERVA [ PASSAGEIRO ]')
        print('[5] - REMOVER CARONA [ MOTORISTA ]')
        print('[6] - SUAS CARONAS [ MOTORISTA ]')
        print('[7] - SUAS RESERVAS [ PASSAGEIRO ]')
        print('[8] - RELATORIO TOTALIZADOR [ MOTORISTA ]')
        print('[9] - FINALIZAR CARONA [ SIMULAÇÃO <3 ]')
        print('[0] - LOGOUT ')
        print()
        print('-=' * 10)
        op2 = input('ESCOLHA A OPÇÃO DESEJADA ^-^: ')
        print()
        if op2.isdigit():
            return int(op2)
        else:
            print('OPÇÃO INVÁLIDA! DIGITE 0, 1, 2, 3, 4, 5, 6, 7, 8 OU 9')


def menu3():
    while True:
        print('-=' * 14)
        print()
        print('[BEM-VINDO AO MENU DE ADMIN!]    ')
        print()
        print('-=' * 14)
        print()
        print('[1] - REMOVER USUARIO ')
        print('[2] - CADASTRAR MOTORISTA ')
        print('[3] - VOLTAR')
        print()
        print('-=' * 14)
        print()
        op3 = input('DIGITE A OPÇÃO DESEJADA ^-^: ')
        print()
        if op3.isdigit():
            return int(op3)
        else:
            print('OPÇÃO INVÁLIDA! DIGITE 1, 2 OU 3')