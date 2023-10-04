class Endereco:
    def _init_(self,rua, numero,complemento,bairro,cidade,uf,cep):
        self.rua=rua
        self.numero=numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade=cidade
        self.uf=uf
        self.cep=cep
    

class Cliente:
    def _init_(self,nome,telefone,endereco):
        self.nome=nome
        self.telefone=telefone
        self.endereco=endereco


class Historico:
    def _init_(self):
        self.__pedidos=[]
    
    def inserir_pedido(self,pedido):
        self.__pedidos.append(pedido)
    
    def calcular_faturamento(self):
        faturamento = 0
        for pedido in self.__pedidos:
            faturamento += pedido.get_valor_total()
        return faturamento
      

class Pedido:
    def _init_(self,cliente,altura,largura,frase,cor_placa,cor_letra):
        self.cliente=cliente
        self.altura=altura
        self.largura=largura
        self.frase=frase
        self.cor_placa=cor_placa
        self.cor_letra=cor_letra
        self.__valor_fixo_material = 147.00
        self.__valor_fixo_letra = 0.35
        self.__valor_total = None


    def get_valor_total(self):
        area = self.altura * self.largura 
        custo_material = area * self.__valor_fixo_material
        custo_desenho = len(remove(self.frase)) * self.__valor_fixo_letra
        valor_placa = custo_material + custo_desenho
        self.__valor_total = valor_placa
        return self.__valor_total


def remove(frase):
  frase = frase.replace(' ', '')
  return frase


pedidos = []
historico1 = Historico()

while True:
  try:

      print('1 - Pedido')
      print('2 - Histórico (Faturamento)')
      print('3 - Todos os pedidos')
      print('4 - Encerrar')
      opcao = int(input('Escolha uma opção: '))
      for p in range(1):
          if opcao == 1:
              print('Inserira seus dados pessoais \n')
              nome = input('Digite seu nome: ')
              
              while True:
                  telefone=input('Digite o DD + Telefone: ')
                  if telefone.isdigit() and len(telefone) ==11 :
                      break
                  else:
                      print('\nTelefone incorreto...\n')
          
              print('\nEndereço:')
              rua=input('Digite o nome da rua: ')
              numero=input('Digite o numero: ')
              complemento = input('Digite o complemento: ')
              bairro = input('Digite o bairro: ')
              cidade=input('Digite a cidade: ')

              while True:
                  uf=input('Digite o UF: ')
                  if uf.isalpha() and len(uf) ==2 :
                      break
                  else:
                      print('\nUF incorreto...\n')


              while True:
                  cep=input('Digite o CEP: ')
                  if cep.isdigit() and len(cep):
                      break
                  else:
                      print('\nCEP incorreto, apenas números...\n')

              endereco = Endereco(rua, numero, complemento,bairro,cidade,uf,cep)
              cliente1 =  Cliente (nome,telefone,endereco)


              print('\nEspecifições da placa:\n')
              while True: 
                  try:
                      altura= float(input('Digite a altura da placa: '))
                      largura= float(input('Digite a largura da placa: '))
                      break

                  except ValueError:
                      print('Erro. Valor inválido, apenas número\n')
              
              
              frase= input('Digite a frase que deseja colocar na placa: ')

              while True: 
                  cor_placa= input('Digite a cor da placa Branco ou Cinza: ')
                  if cor_placa in ['branco', 'branca', 'cinza']:
                      break
                  else:
                      print('\nCores indisponíveis, escolha entre Branco ou Cinza\n')
      
              while True:
                  cor_letra= input('Escolha uma das cores a seguir (Azul, vermelha, amarelo, preta, verde): ')
                  if cor_letra in ['azul', 'vermelha','vermelho', 'amarela', 'amarelo', 'preta', 'preto', 'verde']:
                      break
                  
                  else:
                      print('\nCores indisponiveis, escolha entre: azul, vermelho, amarelo, preto, verde')
                  

              print('------------------')
              pedido = Pedido(cliente1, altura, largura,frase,cor_placa,cor_letra)
              pedidos.append(pedido)
              historico1.inserir_pedido(pedido)

              print(f'TOTAL: {pedido.get_valor_total()} \n')
          
          elif opcao ==2: 
              historico1.calcular_faturamento()
              print(f'\nFaturamento total: {historico1.calcular_faturamento():.2f} \n')
          
          elif opcao ==3:
             print('Todos pedidos: \n')
             cont=0
             for pedido in pedidos:
              cont +=1
              print(f'Pedido {cont}\nNome: {pedido.cliente.nome}  | Telefone: ({pedido.cliente.telefone[:2]}){pedido.cliente.telefone[2:7]}-{pedido.cliente.telefone[7:]} \nEndereço: {pedido.cliente.endereco.rua} n° {pedido.cliente.endereco.numero} {pedido.cliente.endereco.complemento}, {pedido.cliente.endereco.bairro}, {pedido.cliente.endereco.cidade} - {pedido.cliente.endereco.uf}, {pedido.cliente.endereco.cep[:5]}-{pedido.cliente.endereco.cep[5:]}\nFrase: {pedido.frase} | Cor da placa: {pedido.cor_placa} | Cor das letras: {pedido.cor_letra} \nAltura: {pedido.altura} | Largura : {pedido.largura} \nvalor da placa: {pedido.get_valor_total()}\n')
              print('----------------')


          elif opcao == 4:
              print('Programa finalzado')
              exit()
          
          else:
              print('Opção inválida \n')
  except ValueError:
    print('Erro. Caracter inválido, escolha novamente\n')