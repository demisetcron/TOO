class Animal:
    def __init__(self,nome,cor,numero):
        self.nome=nome
        self.cor=cor
        self.numero=numero
        
    def exibir(self):
        print(f'Nome: {self.nome}')
        print(f'Cor: {self.cor}')
        print(f'Numero: {self.numero}')
        

class Cachorro(Animal):
    def __init__(self,nome,cor,numero,raca):
        super().__init__(nome,cor,numero)
        self.raca=raca
    
    def exibir(self):
        super().exibir()
        print(f'Raça: {self.raca}')
    
    
animal = Animal('Passarinho', 'Azul', 2)
animal.exibir()       # exibe os atributos do animal

dog = Cachorro('Rex', 'Marrom', 4, 'Vira lata')
dog.exibir()          # exibe os atributos do cachorro


        