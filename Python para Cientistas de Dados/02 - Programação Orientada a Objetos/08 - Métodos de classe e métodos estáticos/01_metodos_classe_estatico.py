# Métodos de Classe: estão ligados à classe e não ao objeto. 
# Eles têm acesso ao estado de classe, pois recebem um parâmentro que aponta para a classe e não para a instância do objeto (self)  
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade  

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

# Métodos Estáticos: não recebe um primeiro argumento explícito, é vinculado a classe e não ao objeto da classe.
# Ele não pode acessar ou modificar  o estado da classe  (cls)
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
