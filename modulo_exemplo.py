# importação absoluta
import random

# importação relativa (deve ser priorizada)
from math import sqrt
from meu_modulo import somar, multiplicar


# sortei um numero inteiro entre 1 e 20
print(random.randint(1, 20))

# calcula raiz quadrada de 10
print(sqrt(10)) 

# executa funções do módulo implementado
print(somar(4, 7))
print(multiplicar(10, 4))
