#Interpolação de variáveis
nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

#Old style %
print("Nome: %s Idade: %d" % (nome, idade)) #Nome: Guilherme Idade: 28

#Método format
print("Nome: {} Idade: {}".format(nome, idade)) #Nome: Guilherme Idade: 28
print("Nome: {1} Idade: {0}".format(idade, nome)) #Nome: Guilherme Idade: 28
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome)) #Nome: Guilherme Idade: 28 Nome: Guilherme Guilherme

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade)) #Nome: Guilherme Idade: 28
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome)) #Nome: Guilherme Idade: 28 Guilherme Guilherme 28
print("Nome: {nome} Idade: {idade}".format(**dados)) #Nome: Guilherme Idade: 28

#F-string
print(f"Nome: {nome} Idade: {idade}") #Nome: Guilherme Idade: 28
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}") #Nome: Guilherme Idade: 28 Saldo: 45.44
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}") #Nome: Guilherme Idade: 28 Saldo:       45.4

#Formatar string com f-string
PI = 3.14159

print(f"Valor de PI: {PI:.2f}") #"Valor de PI:       3.14"

print(f"Valor de PI: {PI:10.2f}") #"Valor de PI:        3.14"
