"""
COMPOSIÇÃO - É QUANDO VOCÊ UTILIZA ATRIBUTOS DE UMA CLASSE OUTRAS CLASSES DE OUTROS TIPOS.
"""

"""
Você deve criar um classe carro que vai possuir dois atributos compsotos por duas classes:

1) Motor  #__init__():
2) Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo Velocidade    #self.velocidade =0
2) Método acelerar, que deverá incrementar a velocidade de um uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades.

A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos.
1)  Valor de direção com valores possiveis: Norte, Sul, Leste, Oeste
2) Método girar_a_direita
3) Método girar_a_esquerda

  N
O   L
  S

    EXEMPLO:
    #Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    #Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita
    >>> direcao.valor
    'Oeste
    >>> direcao.girar_a_direita
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda
    >>> direcao.valor
    'Norte'
    # TESTANDO CARRO
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade
    1
    >>> motor.acelerar()
    >>> carro.calcular_velocidade
    2
    >>> motor.frear()
    >>> carro.calcular_velocidade
    0
    >>> carro.calcular_direção()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direção()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direção()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direção()
    'Oeste'    
    """

class Carro:
    def __init__(self,direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade
    def acelerar(self):
        self.motor.acelerar()
    def frear(self):
        self.motor.frear()
    def calcular_direcao(self):
        self.direcao.valor
    def girar_a_direita(self):
        self.direcao.girar_a_direita()
    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()
        


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -+ 2
        self.velocidade = max(0, self.velocidade)


NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direção:
    rotacao_a_direita_dct = {NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE}
    rotacao_a_esquerda_dct = {NORTE: OESTE,OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.direcao = NORTE

    def girar_a_direita(self):
#       if self.valor == NORTE:
#          self.valor = LESTE
#     elif self.valor == LESTE:
#        self.valor = SUL
#   elif self.valor == SUL:
#      self.valor = OESTE
        self.valor = self.rotacao_a_direita_dct[self.valor]


    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

print(Carro)