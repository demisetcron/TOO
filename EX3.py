class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

    def exibir(self):
        print(f'endereco: {self.endereco}')
        print(f'preco: {self.preco}')

class ImovelNovo(Imovel):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.adicional = adicional

    def exibir(self):
        super().exibir()
        print(f'adicional: {self.adicional}')

    def calcular_preco(self):
        preco_atualizado = self.preco + self.adicional
        return preco_atualizado

class ImovelVelho(Imovel):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto

    def exibir(self):
        super().exibir()
        print(f'desconto: {self.desconto}')

    def calcular_preco(self):
        preco_atualizado = self.preco - self.desconto
        return preco_atualizado
    
imovel = Imovel("Rua Silva, 123", 300000.0)
imovel.exibir()
imovel_novo = ImovelNovo("Rua Joaquim, 999", 250000.0, 20000.0)
imovel_novo.exibir()
print (imovel_novo.calcular_preco())
imovel_velho = ImovelVelho("Av. Brasil, 777", 500000.0, 35000.0)
imovel_velho.exibir()
print (imovel_velho.calcular_preco())