"""
COMPOSIÇÃO - É QUANDO VOCÊ UTILIZA ATRIBUTOS DE UMA CLASSE OUTRAS CLASSES DE OUTROS TIPOS.
"""

"""
Você deve criar um classe carro que vai possuir dois atributos compsotos por duas classes:

1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo Velocidade
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