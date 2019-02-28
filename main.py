import os


from banqueiro import Banqueiro, Pessoa


class Main(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.inicializa()
		self.executar()

	def inicializa(self):
		valor = input('valor do banqueiro? \n')

		quantidade = input('quantas pessoas? \n')
		lista = []
		quantidade = int(quantidade)
		for i in range(quantidade):
			nome = input("digite o nome da pessoa {} \n".format(i+1))
			pessoa = Pessoa(nome, i+1)
			lista.append(pessoa)
		self.banqueiro = Banqueiro(int(valor), lista)

	def menu(self):
		print("\n Escolha a pessoa Abaixo")
		for i in self.banqueiro.lista:
			print("\n [{}] para {} ".format(i.codigo, i.nome), end="")
		print("\n [0] para Sair ", end="")
		print("\n [-1] para ver a lista de Espera ", end="")
		mensagem = input("\n")
		os.system('cls' if os.name == 'nt' else 'clear')
		return int(mensagem)

	def verifica_ciclo(self):
		for i in self.banqueiro.lista:
			if i.ciclo == 3:
				print('\t {} Devolveu o valor Pego {}'.format(i.nome, i.saldo))
				self.banqueiro.saldo += i.saldo
				i.saldo = 0
				i.ciclo = 0
			# else:
			# 	print(i.ciclo)
		
	def aumenta_ciclo(self):
		for i in self.banqueiro.lista:
			if i.saldo > 0:
				i.ciclo += 1

	def escolha(self, pessoa):
		if pessoa.saldo > 0:
			devolver = input('Como ja tem dinheiro emprestao, Deseja Devolver o Valor Pego? [s] ou [n] \n')
			if devolver == 's':
				print('Valor de {} Devolvido com Sucesso!'.format(pessoa.saldo))
				self.banqueiro.saldo = self.banqueiro.saldo + pessoa.saldo
				pessoa.saldo = 0
				pessoa.ciclo = 0

		else:
			self.verifica_ciclo()
			valor = input('Quanto Deseja Pegar? \n')
			if not valor.isdigit():
				print('Valor informado inválido')
				return
			valor = int(valor)
			if self.banqueiro.saldo >= valor:
				pessoa.saldo = valor
				self.banqueiro.saldo = self.banqueiro.saldo - valor
				print('Valor emprestado com sucesso, Saldo de {} é {}'.format(pessoa.nome, pessoa.saldo))
				self.aumenta_ciclo()
			elif self.banqueiro.saldo_total <= valor:
				print('Solicitação Negada!\n')
			else:
				self.aumenta_ciclo()
				print('Aquarde na lista de Espera !\n')


	def executar(self):
		
		entrada = self.menu()
		while not entrada == 0:
			for i in self.banqueiro.lista:
				if entrada == i.codigo:
					print('Pessoa {} Saldo = {} '.format(i.nome, i.saldo))
					self.escolha(i)
					valida = True

	
			if entrada == '0':
				print('Sair')
				break
			

			entrada = self.menu()


Main()