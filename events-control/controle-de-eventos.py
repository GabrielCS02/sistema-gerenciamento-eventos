from datetime import datetime

# Lista de eventos (cada evento é um dicionário)
eventos = []

# Função para validar se o número de vagas é maior que zero e é um número válido
def validar_vagas(vagas_max):
    while True:
        try:
            vagas_max = int(vagas_max)
            if vagas_max > 0:
                return vagas_max
            else:
                print("O número de vagas deve ser maior que zero. Tente novamente.")
        except ValueError:
            print("O número de vagas deve ser um número inteiro válido. Tente novamente.")
        vagas_max = input("Número máximo de vagas: ")

# Função para cadastrar eventos
def cadastrar_evento(nome, data, descricao, vagas_max):
    vagas_max = validar_vagas(vagas_max)  # Validação de vagas
    evento = {
        'nome': nome,
        'data': data,
        'descricao': descricao,
        'vagas_max': vagas_max,
        'vagas_restantes': vagas_max,
        'inscritos': []
    }
    eventos.append(evento)
    print(f"Evento '{nome}' cadastrado com sucesso!")

# Função para validar a entrada de data
def validar_data(data):
    while True:
        try:
            datetime.strptime(data, '%Y-%m-%d')  # Tentando converter a data para o formato YYYY-MM-DD
            return data
        except ValueError:
            print("Data inválida! O formato correto é YYYY-MM-DD. Tente novamente.")
            data = input("Data do evento (YYYY-MM-DD): ")

# Função para atualizar evento
def atualizar_evento(nome_evento, nova_data=None, novas_vagas=None):
    for evento in eventos:
        if evento['nome'] == nome_evento:
            if nova_data:
                nova_data = validar_data(nova_data)  # Validação de data
                evento['data'] = nova_data
            if novas_vagas:
                novas_vagas = validar_vagas(novas_vagas)  # Validação de vagas
                evento['vagas_max'] = novas_vagas
                evento['vagas_restantes'] = novas_vagas - len(evento['inscritos'])
            print(f"Evento '{nome_evento}' atualizado com sucesso!")
            return
    print("Evento não encontrado.")

# Função para visualizar eventos disponíveis
def visualizar_eventos():
    if not eventos:
        print("Não há eventos cadastrados.")
    else:
        print("Eventos Disponíveis:")
        for evento in eventos:
            # Conversão da data para o formato brasileiro
            data_brasileira = datetime.strptime(evento['data'], '%Y-%m-%d').strftime('%d/%m/%Y')
            print(f"{evento['nome']} - {data_brasileira} - {evento['descricao']} - Vagas Restantes: {evento['vagas_restantes']}")

# Função para validar o nome do aluno
def validar_aluno(aluno):
    while not aluno.strip():
        print("O nome do aluno não pode estar vazio. Tente novamente.")
        aluno = input("Nome do aluno: ")
    return aluno

# Função para se inscrever em um evento
def inscrever_em_evento(nome_evento, aluno):
    aluno = validar_aluno(aluno)  # Validação de nome do aluno
    for evento in eventos:
        if evento['nome'] == nome_evento:
            if evento['vagas_restantes'] > 0:
                evento['inscritos'].append(aluno)
                evento['vagas_restantes'] -= 1
                print(f"Aluno {aluno} inscrito no evento '{nome_evento}' com sucesso!")
                return
            else:
                print("Não há vagas disponíveis para este evento.")
                return
    print("Evento não encontrado.")

# Função para visualizar inscritos em um evento
def visualizar_inscritos(nome_evento):
    for evento in eventos:
        if evento['nome'] == nome_evento:
            if evento['inscritos']:
                print(f"Inscritos no evento '{nome_evento}':")
                for inscrito in evento['inscritos']:
                    print(f"- {inscrito}")
            else:
                print(f"Não há inscritos para o evento '{nome_evento}'.")
            return
    print("Evento não encontrado.")

# Função para excluir evento
def excluir_evento(nome_evento):
    global eventos
    eventos = [evento for evento in eventos if evento['nome'] != nome_evento]
    print(f"Evento '{nome_evento}' excluído com sucesso.")

# Função para mostrar o menu de opções
def menu():
    while True:
        print("\n--- Sistema de Gerenciamento de Eventos ---")
        print("1. Cadastrar evento")
        print("2. Atualizar evento")
        print("3. Visualizar eventos disponíveis")
        print("4. Inscrever-se em evento")
        print("5. Visualizar inscritos de um evento")
        print("6. Excluir evento")
        print("7. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            nome = input("Nome do evento: ")
            data = input("Data do evento (YYYY-MM-DD): ")
            descricao = input("Descrição do evento: ")
            vagas_max = input("Número máximo de vagas: ")
            vagas_max = validar_vagas(vagas_max)  # Validação de vagas
            data = validar_data(data)  # Validação de data
            cadastrar_evento(nome, data, descricao, vagas_max)
        
        elif escolha == "2":
            nome_evento = input("Nome do evento que deseja atualizar: ")
            nova_data = input("Nova data do evento (deixe em branco para não alterar): ")
            novas_vagas = input("Novo número de vagas (deixe em branco para não alterar): ")
            if novas_vagas:
                novas_vagas = validar_vagas(novas_vagas)  # Validação de vagas
            atualizar_evento(nome_evento, nova_data or None, novas_vagas)
        
        elif escolha == "3":
            visualizar_eventos()
        
        elif escolha == "4":
            nome_evento = input("Nome do evento para inscrição: ")
            aluno = input("Nome do aluno: ")
            inscrever_em_evento(nome_evento, aluno)
        
        elif escolha == "5":
            nome_evento = input("Nome do evento para visualizar inscritos: ")
            visualizar_inscritos(nome_evento)
        
        elif escolha == "6":
            nome_evento = input("Nome do evento que deseja excluir: ")
            excluir_evento(nome_evento)
        
        elif escolha == "7":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu interativo
menu()
