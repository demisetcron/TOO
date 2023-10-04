class Pessoa:
    def __init__(self, nome, idade, rg, cpf):
        self.nome = nome
        self.rg = rg
        self.idade = idade
        self.cpf = cpf

    def exibir(self):
        print(f'nome: {self.nome}')
        print(f'rg: {self.rg}')
        print(f'idade: {self.idade}')
        print(f'cpf: {self.cpf}')

class Aluno(Pessoa):
    def __init__(self, nome, idade, rg, cpf, ra):
        super().__init__(nome, idade, rg, cpf)
        self.ra = ra



    def exibir(self):
        super().exibir()
        print(f'RA: {self.ra}')

class Professor(Pessoa):
    def __init__(self, nome, idade, rg, cpf, salario):
        super().__init__(nome, idade, rg, cpf, salario)
        self.salario = salario

    def exibir(self):
        super().exibir()
        print(f'Salario {self.salario}')


aluno1 = Aluno('joao', 20, '12345667', '6666666666', '12452134')
aluno1.exibir()

prof1 = Professor('joaquim', 50, '33214235', '324234253', 30000)
prof1.exibir()