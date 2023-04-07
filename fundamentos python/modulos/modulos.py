#importação de um módulo inteiro
import areas

print(areas.triangulo(2,8))

# importação de uma função direto
from areas import trapezio

print(trapezio(5,6,2))

# Módulos nativos do python
import math
print('Função consseno', math.cos(100))
print('Função logaritima', math.log(10))

# É quuase a mesma coisa que a função Range, é um módulo para sequências elaboradas
import itertools
# combinação de 3 em 3
print(list(itertools.combinations('ABCD',3)))


# Módulos de horário
from datetime import datetime, timedelta
# horário atual
print('horário atual', datetime.now())
print('Horário atual após 7 dias', datetime.now() + timedelta(days=7))


# Módulo para criação de números e sequências aleatórias
import random
print('Número aleatório entre 0 e 1:', random.random())
# randônificação entre intervalors
print('Número aleatório entre 50 e 100:', random.randint(50,100))

# Módulo para fazer interação com sistema operacional
import os
# cria uma pasta
#os.mkdir('pasta feita com python') 

from colorama import Fore
print(Fore.BLUE + 'texto aoba')