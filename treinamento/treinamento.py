"""
O treinamento será realizado em 2 etapas e as pessoas serão divididas em salas com lotação variável. 
Serão realizados também dois intervalos de café em 2 espaços distintos. Você precisa criar o sistema que 
gerenciará este evento.
O sistema precisa permitir que:
- O cadastro de pessoas, com nome e sobrenome;
- O cadastro das salas do evento, com nome e lotação;
- O cadastro dos espaços de café pelo nome;
- Diferença de no máximo 1 pessoa
- Troca sala

Requisitos obrigatórios:
Crie uma interface que permita:
- O cadastro de pessoas, com nome e sobrenome;
- O cadastro das salas do evento, com nome e lotação;
- O cadastro dos espaços de café com lotação;
- A consulta de cada pessoa;
- A consulta de cada sala e espaço;
"""
#Importando classe pessoas
from Pessoas import Pessoas
#Importando a classe sala
from Sala import Sala
#Importando classe espaço
from Espaco import Espaco

#Criando lista de opções para o usuário
lista_opcoes = ["\nOpções: ",
                "\n0 - Encerrar o programa",
                "1 - Cadastrar sala ",
                "2 - Cadastrar pessoas ",
                "3 - Cadastrar café",
                "4 - Consulta pessoa",
                "5 - Consulta sala",
                "6 - Consulta espaço"]

#Criando lista pessoas 
lista_pessoas = []
#Criando lsita de salas
lista_sala = []
#Criando lista café
lista_cafe = []

#Iniciando interação com o usuário
print("Sistema de cadastro treinamento")
nome_usuario = input("\n Ola! Digite seu nome: ")

#Loop para funcionamento do programa
while True:
    #Mostra as opções e solicita que o usuário selecione uma
    print(f"{nome_usuario} escolha uma opção: ")
    for opcao in lista_opcoes:
        print(opcao)
    opcao_selecionada = int(input("Insira a opção desejada: "))
    #controle de navegação do sistema
    if opcao_selecionada == 0: #Encerra o programa
        confirma = int(input("Você escolheu sair do programa, deseja realmente sair? (Pressione 0 - Não ou 1 - Sim) "))
        if confirma == 1:
            print("Programa encerrado!")
            break
        elif confirma == 0:
            opcao_selecionada = int(input("Insira a opção desejada:"))
        elif confirma > 1:
            print("Opção selecionada inválida!")
            confirma = input("Você escolheu sair do programa, deseja realmente sair? (Pressione 0 - Não ou 1 - Sim)")
    elif opcao_selecionada == 1: #Cadastrar uma nova sala
        while True:
            nome_sala = input("Digite o nome da sala: ")
            capacidade_sala = int(input("Insira a capacidade da sala (somente numero): "))
            sala = Sala(nome = nome_sala, capacidade = capacidade_sala)
            lista_sala.append(sala) #Adiciona uma sala na lista 
            print(f"A sala {nome_sala} foi cadastrada!")

            #Gravando dados em arquivo "salas.txt"
            with open('salas.txt', 'a+') as f:
                f.write("\n Sala: " + sala.nome + " " + "Capacidade: " + str(sala.capacidade))
            
            #Verificando se dejasa continuar cadastrando salas
            controle_insert = input("Deseja cadastrar mais salas? (Digite 'n' ou 'N' para sair) \n")           
            if len(controle_insert) == 1:
                if controle_insert == "n" or controle_insert == "N" or controle_insert == "s" or controle_insert == "S":
                    if controle_insert.upper() == "N":
                        print("Saindo do cadastro de salas")
                        break
    elif opcao_selecionada == 2: #Cadastrando pessoas
        while True:
            nome_pessoa = input("Insira o nome: ")
            sobrenome_pessoa = input("Insira o sobrenome: ")
            nome_sobrenome = nome_pessoa + " " + sobrenome_pessoa
            telefone = int(input("Insira o telefone: "))
            pessoa = Pessoas(nome = nome_pessoa, sobrenome = sobrenome_pessoa, telefone = telefone, nome_sobrenome = nome_sobrenome)
            lista_pessoas.append(pessoa)
            print(f"Foi realizado o cadastro de {nome_pessoa} {sobrenome_pessoa}")
            
            
            #Gravando dados em arquivo "pessoas.txt"
            with open('pessoas.txt', 'a+') as f:
                f.write("\n Nome: " + nome_sobrenome + " " + "Contato: " + str(pessoa.telefone))

            #Verificando se dejasa continuar cadastrando pessoas
            controle_insert = input("Deseja cadastrar mais pessoas? (Digite 'n' ou 'N' para sair) \n")
            if len(controle_insert) == 1:
                if controle_insert == "n" or controle_insert == "N" or controle_insert == "s" or controle_insert == "S":
                    if controle_insert.upper() == "N":
                        print("Saindo do cadastro de pessoas")
                        break
    elif opcao_selecionada == 3: #Cadastro espaço café
        while True:
            nome_espaco = input("Insira o nome do espaço: ")
            lotacao = int(input("Insira a lotação maxima: "))
            espaco = Espaco(nome = nome_espaco, lotacao = lotacao)
            lista_cafe.append(espaco)
            print(f"Foi realizado o cadastro do espaço de café {nome_espaco}")
            
            #Gravando dados em arquivo "espaço.txt"
            with open('espaco.txt', 'a+') as f:
                f.write("\n Espaço: " + espaco.nome + " " + "Capacidade: " + str(espaco.lotacao))

            #Verificando se dejasa continuar cadastrando espaços
            controle_insert = input("Deseja cadastrar mais espaços? (Digite 'n' ou 'N' para sair) \n")
            if len(controle_insert) == 1:
                if controle_insert == "n" or controle_insert == "N" or controle_insert == "s" or controle_insert == "S":
                    if controle_insert.upper() == "N":
                        print("Saindo do cadastro de espaços para o café")
                        break
    elif opcao_selecionada == 4: #Consulta pessoa
        while True:
            nome_pessoa_pesquisada = input("Digite o nome da pessoa que deseja pesquisar: ")
            controle = 0
            for pessoa in lista_pessoas:
                if nome_pessoa_pesquisada.upper() in pessoa.nome_sobrenome.upper():
                    print(f"A pessoa {pessoa.nome_sobrenome} está cadastrada")
                    controle = controle + 1
                if controle == 0:
                    print("Pessoa não encontrada!")
            
            #Saindo da pesquisa
            controle_pesquisa = input("Deseja encerrar a pesquisa? (Digite 's' ou 'S' para sair) \n")
            if len(controle_pesquisa) == 1:
                if controle_pesquisa == "n" or controle_pesquisa =="N" or controle_pesquisa == "s" or controle_pesquisa == "S":
                    if controle_pesquisa.upper() == "S":
                        print("Saindo da pesquisa.")
                        break
                
    elif opcao_selecionada == 5: #Consulta sala
        while True:
            nome_sala_pesquisada = input ("Digite o nome da sala que deseja pesquisar: ")
            controle = 0
            for sala in lista_sala:
                if nome_sala_pesquisada.upper() in sala.nome.upper():
                    print(f"A sala {sala.nome} com a lotação de {sala.capacidade} está cadastrada!")
                    controle = controle + 1
                if controle == 0:
                    print("Sala não encontrada!")

            #Saindo da pesquisa
            controle_pesquisa = input("Deseja encerrar a pesquisa? (Digite 's' ou 'S' para sair) \n")
            if len(controle_pesquisa) == 1:
                if controle_pesquisa == "n" or controle_pesquisa =="N" or controle_pesquisa == "s" or controle_pesquisa == "S":
                    if controle_pesquisa.upper() == "S":
                        print("Saindo da pesquisa.")
                        break
    elif opcao_selecionada == 6: #Consulta espaço
        while True:
            nome_espaco_pesquisado = input("Digite o nome do espaço que deseja pesquisar: ")
            controle = 0
            for espaco in lista_cafe:
                if nome_espaco_pesquisado.upper() in espaco.nome.upper():
                    print(f"O espaço {espaco.nome} com a lotação de {espaco.lotacao}") 
                    controle = controle + 1
                if controle == 0:
                    print("Sala não encontrada!")
            
            #Saindo da pesquisa
            controle_pesquisa = input("Deseja encerrar a pesquisa? (Digite 's' ou 'S' para sair) \n")
            if len(controle_pesquisa) == 1:
                if controle_pesquisa == "n" or controle_pesquisa =="N" or controle_pesquisa == "s" or controle_pesquisa == "S":
                    if controle_pesquisa.upper() == "S":
                        print("Saindo da pesquisa.")
                        break               
                