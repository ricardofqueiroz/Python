
#Criando o menu de opções
print("""
[1] - NomeCompleto
[2] - multiplicacao
[3] - cestaFrutas
[4] - HoraAtual
[5] - sair
""")
#=========================================================#
#Criando um contador para a estrutura de repetição while caso o usuário escolha opção não existente
contar=0
#=========================================================#
#Criando as funções
#1º Função
def NomeCompleto():
	SeuNome = input("Digite seu nome: ")
	print(SeuNome)

#2º Função
def multiplicacao():
	n1=int(input(": "))
	n2=int(input(": "))
	multiplicar=n1*n2
	print(multiplicar)

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
	opcao=int(input("Não existe. Escolha outra: "))
	contar=contar+1
if opcao == 1:
	NomeCompleto()
elif opcao == 2:
	multiplicacao()
elif opcao == 3:
    for i in range(0,4):
    	cesta.append(input(":"))
    	print(cesta)
elif opcao == 4:
	HoraAtual()
elif opcao == 5:
	print("Sair do programa")
else:
	print("Essa Opção não existe. Escolha outra")
	opcao=int(input("Escolha: "))
	contar=contar+1
	
