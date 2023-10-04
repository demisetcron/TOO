class Pessoa:
    def __init__(self,nome, endereco, fone, cpf):
        self. endereco = endereco
        self.nome = nome
        self.fone = fone
        self.cpf = cpf
        
    def exibir(self):
        print(f'nome: {self.nome}')
        print(f'endereco: {self.endereco}')
        print(f'fone: {self.fone}')
        print(f'cpf: {self.cpf}')


class Aluno(Pessoa):
    def __init__(self, nome, endereco, fone, cpf, disciplina):
        super().__init__(nome, endereco, fone, cpf)
        self.disciplina = []

    def exibir(self):
        super().exibir()
        print(f'disciplina: {self.disciplina}')

    def incluir(self, disciplinas):
        self.disciplina.append(disciplinas)

class Funcionario:
    def __init__(self, nome, endereco, fone, cpf, salario):
        super().__init__(nome, endereco, fone, cpf)
        self.salario = salario

    def exibir(self):
        super().exibir()
        print(f'salario: {self.salario}')

class Disciplina(Aluno):
    def __init__(self, nome, endereco, fone, cpf, disciplina, nome_d):
        super().__init__(nome, endereco, fone, cpf, disciplina)
        self.nome_d = nome_d

    def exibir(self):
        super().exibir()
        print(f'Nome da Disciplina: {self.nome_d}')

class Professor(Funcionario):
    def __init__(self, nome, endereco, fone, cpf, salario, titulacao, disciplina):
        super().__init__(nome, endereco, fone, cpf, salario)
        self.titulacao = titulacao
        self.disciplina = []

    def incluir(self, disciplinas):
        self.disciplina.append(disciplinas)

    def exibir(self):
        super().exibir()
        print(f'titulacao: {self.titulacao}')
        print(f'disciplina: {self.disciplina}')

class Tecnico(Funcionario):
    def __init__(self, nome, endereco, fone, cpf, salario, cargo):
        super().__init__(nome, endereco, fone, cpf, salario)
        self.cargo = cargo

    def exibir(self):
        super().exibir()
        print(f'cargo: {self.cargo}')

Disciplina = []


disciplina1 = Disciplina('Programação')
disciplina2 = Disciplina('Banco de Dados')
professor1 = Professor('Joao', 'Rua Silva, 456', '(11)99999-9555', '9999999', 2000, 'Mestrado')
aluno1 = Aluno('Maria', 'Avenida São Francisco, 239', '(11)98888-8435', '555555')
tecnico1 = Tecnico('Pedro', 'Rua Rocha, 77', '(11)93333-3333', '8787887', 1500, 'Tecnico')


aluno1.incluir_disciplina(disciplina1)
aluno1.incluir_disciplina(disciplina2)
professor1.incluir_disciplina(disciplina1)


print('Disciplinas associadas ao aluno:')
for d in aluno1.disciplina:
    print(d.nome)


print('Disciplinas associadas ao Professor:')
for d in professor1.disciplina:
    print(d.nome)