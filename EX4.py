class Motor:
    def __init__(self,cilindrada,potencia):
        self.cilindrada=cilindrada
        self.potencia=potencia
    
    def exibir(self):
        print(self.cilindrada)
        print(self.potencia)
      
class Veiculo:
    def __init__(self,ano,preco,motor):
        self.ano=ano
        self.preco=preco
        self.motor=motor
    
    def exibir(self):
        print(self.ano)
        print(self.preco)
        print(self.motor.potencia)
        print(self.motor.cilindrada)
       

class Carro(Veiculo):
    def __init__(self,ano,preco,motor,cor,modelo):
        super().__init__(ano,preco,motor)
        self.cor=cor
        self.modelo=modelo
    
    def exibir(self):
        super().exibir()
        print(self.cor)
        print(self.modelo)

class Caminhao(Veiculo):
    def __init__(self,ano,preco,motor,comprimento):
        super().__init__(ano,preco,motor)
        self.comprimento=comprimento
    
    def exibir(self):
        super().exibir()
        print(self.comprimento)



motor1 = Motor(1000, 500)
motor2 = Motor(8000, 900)
carro1 = Carro(2010, 20000, motor1, "branca", "gol")
caminhao1 = Caminhao(2015, 80000, motor2, 10)

carro1.exibir() 
print('-----------------')# imprime os valores de todos os atributos do carro
caminhao1.exibir()        # imprime os valores de todos os atributos do caminhão
