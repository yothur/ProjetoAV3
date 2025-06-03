def salvar_usuarios(usuarios):
    file = open('Usuarios.txt', 'w')
    for email in usuarios:
        u = usuarios[email]
        linha = f'{u['Email']};{u['Senha']};{u['Nome']}\n'
        file.write(linha)
    file.close()

def carregar_usuarios(usuarios):
    file = open('Usuarios.txt', 'r')
    linhas = file.readlines()
    file.close()
    for linha in linhas:
        partes = linha.strip().split(';')
        email = partes[0]
        senha = partes[1]
        nome = partes[2]
        usuarios[email] = {'Email': email, 'Senha': senha, 'Nome': nome, 'Reservas':[]}

def salvar_relatorio(motoristas, email_user, caronas):
    totalizador = 0
    file2 = open('Relatorio.txt', 'w')
    for carona_id in motoristas[email_user]['Caronas']:
        carona = caronas[carona_id]
        texto2 = f'ID: {carona_id} | Origem: {carona['Local']} | Destino: {carona['Destino']} | Data: {carona['Data']} | Horário: {carona['Horario']}h | Vagas: {carona['Vagas']} | Valor: R${carona['Valor']} | Passageiros: {carona['Passageiros']} | Total: R${float(carona['Valor']) * len(carona['Passageiros'])}\n'
        if len(carona['Passageiros']) != 0:
            totalizador += float(carona['Valor'])
            total = f'VALOR DE TODAS AS CARONAS R${totalizador}\n'
            file2.write(texto2)
            file2.write(total)
    file2.close
