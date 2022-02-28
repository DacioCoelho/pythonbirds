# CLASSE - É A FORMA COMO O OBJETOS SE COMPORTAM
"""
A Classe é uma forma de vocÊ criar seues tipos personalizados
Funciona como forma de gelo, e você precis colocar agua para seer moldada

Metódo é uma função que pertence a uma classe"""

class Pessoa:  #Letras em maisculo no inicio das frases
    def __init__(self, nome= None, idade= 30):   #Atributo de inicialização
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Ana Cláudia', 23)
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Dácio'
    print(p.nome)
    print(p.idade)

