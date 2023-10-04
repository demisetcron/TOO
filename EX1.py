class Pessoa:
    def __init__(self, identificador, nome):
        self. identificador = identificador
        self.nome = nome
        
    def exibir(self):
        print(f'identificador: {self.identificador}')
        print(f'nome: {self.nome}')

class PessoaJuridica(Pessoa):
    def __init__(self, identificador, nome, cnpj):
        super().__init__(identificador, nome)
        self.cnpj = cnpj

    def exibir(self):
        super().exibir()
        print(f'CNPJ: {self.cnpj}')

class PessoaFisica(Pessoa):
    def __init__(self, identificador, nome, rg, cpf):
        super().__init__(identificador, nome)
        self.rg = rg
        self.cpf = cpf

    def exibir(self):
        super().exibir()
        print(f'RG: {self.rg}')
        print(f'CPF: {self.cpf}')
        
pessoa1 = Pessoa(1,'Alana') 
p_juridica = PessoaJuridica(2, "Bruno", "1111111111")
p_juridica.exibir()
p_fisica = PessoaFisica(3, "Julio", "222222222", "333333333")
p_fisica.exibir()
