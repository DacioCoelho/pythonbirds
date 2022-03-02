# CLASSE - É A FORMA COMO O OBJETOS SE COMPORTAM
"""
A Classe é uma forma de vocÊ criar seues tipos personalizados
Funciona como forma de gelo, e você precis colocar agua para seer moldada

Metódo é uma função que pertence a uma classe"""

class Pessoa:  #Letras em maisculo no inicio das frases
    def __init__(self, *filhos, nome= None, idade= 30):   #Atributo de inicialização
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    bernardo = Pessoa(nome='Bernardo')
    ana = Pessoa(bernardo, 'Ana Cláudia', 23)
    print(Pessoa.cumprimentar(ana))
    print(id(ana))
    print(ana.cumprimentar())
    print(ana.idade)
    print(ana.filhos)
    for filho in ana.filhos:
        print(filho.nome)

