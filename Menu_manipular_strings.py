print("""
	[1] - Preencher_nome
	[2] - Preencher_lista_com_seu_nome
	[3] - Buscar_posicao_do_nome_e_sobrenome
	[4] - Buscar_palavras_dentro_da_lista
	[5] - Inverter_strings
	[6] - Substituir_letras
	[7] - Deixar_maiuscula_minuscula
	[8] - Sair
	""")

contar=0
# Função preencher nome e sobrenome
def Preencher_nome():
	nome=input("Digite seu nome: ")
	sobrenome=input("Digite seu sobrenome: ")
	print("Seu nome é", nome, "\nE seu sobrenome é", sobrenome)

# Função de inserir nome e sobrenome em uma lista
def Preencher_lista_com_seu_nome():
	nome=input("Digite seu nome: ")
	sobrenome=input("Digite seu sobrenome: ")
	print("Lista contendo nome e sobrenome", nome.split(),sobrenome.split())

# Função busca de posições do nome e sobrenome da lista
def Buscar_posicao_do_nome_e_sobrenome():
	nome=input("Digite seu nome: ")
	sobrenome=input("Digite seu sobrenome: ")
	print("Buscando posições do nome e sobrenome adicionado a lista")
	print("1º - Posições do nome")
	print("As posições escolhida do nome são", nome[int(input(":")):int(input(":"))])
	print("2º - Posições do sobrenome")
	print("As posições escolhida do sobrenome são", sobrenome[int(input(":")):int(input(":"))])

# Função buscar palavras dentro da lista
def Buscar_palavras_dentro_da_lista():
	nome=input("Digite seu nome: ")
	sobrenome=input("Digite seu sobrenome: ")
	print("Lista contendo nome e sobrenome", nome.split(),sobrenome.split())
	print("Buscando palavras dentro da lista por sua posição")
	print("1º - Posição do Nome") 
	print(nome.split()[int(input(":"))])
	print("2º - Posição do Sobrenome ")
	print(sobrenome.split()[int(input(":"))])

# Função de inverter string
def Inverter_strings():
	nome=input("Digite seu nome: ")
	sobrenome=input("Digite seu sobrenome: ")
	print("Inverta as posições do nome e sobrenome")
	print("1º - Nome")
	print(nome[::int(input(":"))])
	print(nome[int(input(":")):int(input(":"))])
	print("2º - Sobrenome")
	print(sobrenome[::int(input(":"))])
	print(sobrenome[int(input(":")):int(input(":"))])

# Função de substituir letras ou uma string inteira
def Substituir_letras():
	nome=input("Digite seu nome: ")
	sobrenome=input("Digite seu sobrenome: ")
	print("Substitua letras")
	print("1º - Nome")
	print(nome.replace(input(":"),input(":")))
	print("2º - Sobrenome")
	print(sobrenome.replace(input(":"),input(":")))

# Função de substituir por letras maiuscula ou minuscula
def Deixar_maiuscula_minuscula():
	nome=input("Digite seu nome: ")
	sobrenome=input("Digite seu sobrenome: ")
	print("Substituindo por letras maíuscula ou minuscula")
	print("1º - Nome")
	print(nome.upper(),nome.lower())
	print("2º - Sobrenome")
	print(sobrenome.upper(),sobrenome.lower())

# Escolhendo as opções
escolha=int(input("Escolha uma opção: "))
while escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5 and escolha != 6 and escolha != 7 and escolha != 8:
	escolha=(int(input("Esta opção não existe. Escolha outra: ")))
	contar=contar+1
if escolha == 1:
	Preencher_nome()
elif escolha == 2:
	Preencher_lista_com_seu_nome()
elif escolha == 3:
	Buscar_posicao_do_nome_e_sobrenome()
elif escolha == 4:
	Buscar_palavras_dentro_da_lista()
elif escolha == 5:
	Inverter_strings()
elif escolha == 6:
	Substituir_letras()
elif escolha == 7:
	Deixar_maiuscula_minuscula()
elif escolha == 8:
	print("Sair")



