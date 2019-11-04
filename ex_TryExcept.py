#1º Script - Cesta de frutas
fruta = input('Digite uma fruta: ')

#Construindo duas listas, uma contendo frutas que estão maduras e outra sem frutas maduras. 
frutas_madura=["laranja", "maça", "abacaxi"]
frutas_nao_maduras=["goiaba", "morango", "uva"]
"""
Condição que identifica se a fruta digitada pelo usuário contendo nas duas listas é madura ou não.
Caso digite uma que não esteja em nenhuma das duas listas será informado como não existente.
"""
if fruta in frutas_madura:
	try:
		printt("Boa pra consumo") #Erro ocorrido no printt
	except:
		print("Houve um erro nesta execução. Segue o programa.")
		#print - Pode deixar somente print 
elif fruta in frutas_nao_maduras:
	print("Não é boa pra consumo")
else:
	print("Essa fruta não esta em nenhuma lista pra ser identificada se pode ser consumida ou não.")

"""
O objetivo no 1º Script é mostrar algum erro no código, no entanto o uso das palavras reservada "try e except" ira tratar o erro
para que o script continue a ser executado. O erro no código esta na saída "printt", linha 13 que pertence a lista de "frutas_madura", 
pois print não tem duas letras 't', isso traria um erro dentro do script não deixando ser executado.
"""
#===================================================================================================#
#2º script - Frota de carros
carro = input('Digite um carro: ')
#Criando as listas
frota1=["Camaro", "Uno", "Vivace", "Monza"]
frota2=["Ferrari", "Celta", "Santana", "Gol"]
#Condição
if carro in frota1:
	print("Esse carro pertece a 1º frota")
elif carro in frota2:
	print("Esse carro pertece a 2º frota")
else:
	print("Esse carro não pertece a nenhuma frota")
