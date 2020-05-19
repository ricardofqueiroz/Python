
#Menu de opções
print("""
[1] - DadosPessoa
[2] - Calculos
[3] - cestaFrutas
[4] - HoraAtual
[5] - sair
""")
#=========================================================#
#Criando um contador para a estrutura de repetição while caso o usuário escolha opção não existente
contar=0
#=========================================================#
#Funções

#1º Função
def DadosPessoa():

#	SeuNome = input("Digite seu nome: ")
#	print('Nome da pessoa é', SeuNome)
#	idade=int(input("Digite sua idade: "))
#	print(SeuNome, 'tem', idade, 'anos.', 'Nasceu no ano de', 2020 - idade)

#Exemplo com formatação	
    SeuNome=input("Digite seu nome: ")
    print(f'Nome da pessoa é {SeuNome}')
    idade=int(input("Digite sua idade: "))
    print(f'{SeuNome} tem {idade} anos. Nasceu no ano de {2020 - idade}.')

#2º Função
def Calculos():
    print("Calculando uma multiplicação")
    n1=int(input(": "))
    n2=int(input(": "))  
    multiplicar=n1*n2
    print("O resultado da multiplicação é:", multiplicar, "e seu tipo de dado é", type(multiplicar))
    """
    No tipo de dado 'type(multiplicar)' que mostra qual o tipo de dado da multiplicação também poderia 
    ser 'print(type(multiplicar))'  
    """
#3º Função
def cestaFrutas(frutas):
	return frutas
cesta=[]

#4º Função
def HoraAtual():
   from datetime import datetime
   horas=datetime.now()
   horas12=horas.strftime("%I:%M") #%I - Significa formato 12 horas
   periodo=horas.strftime("%p") #%p - Siginifica periodo se é AM/PM
   print("Agora são:", horas12, periodo)
#=========================================================#
#Escolhendo as opções para chamar as funções
opcao=int(input("Escolha uma opção: "))
while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
	opcao=int(input("Esta opção não existe. Escolha outra: "))
	contar=contar+1
if opcao == 1:
	DadosPessoa()
elif opcao == 2:
	Calculos()
elif opcao == 3:
#O loop while ira permitir que preencha a cesta com até 5 frutas  
  contar=0
  while len(cesta)<5: #'len' irá retornar o comprimento da lista cesta, ou seja o nº de frutas na cesta
    fruta=input("Digite uma fruta:") 
    contar=contar+1
#Condição que irá identificar se ha fruta repetida na cesta    
    if fruta in cesta:
      print("Essa fruta ja foi colocada na cesta, digite outra")
    else:
#Continuando preencher a cesta com o uso da função 'append' que irá sempre adicionar uma fruta na cesta      
      cesta.append(fruta)
      print(cesta)
#Condição que informa se a lista 'cesta' foi preenhida com a função 'len' que retorna o comprimeto da lista cesta      
      if len(cesta)==5:
        print("A cesta de frutas esta cheia")
elif opcao == 4:
    HoraAtual()
elif opcao == 5:
    print("Sair do programa")

