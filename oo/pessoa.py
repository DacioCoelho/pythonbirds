# CLASSE - É A FORMA COMO O OBJETOS SE COMPORTAM
"""
A Classe é uma forma de vocÊ criar seues tipos personalizados
Funciona como forma de gelo, e você precis colocar agua para seer moldada

Metódo é uma função que pertence a uma classe"""

class Pessoa:  #Letras em maisculo no inicio das frases
    olhos = 2  #ATRIBUTO DE CLASSE - usado quando o dado é fixo para todos, exceto exeções
    def __init__(self, *filhos, nome= None, idade= 23):   #Atributo de inicialização
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    bernardo = Pessoa(nome='Bernardo')
    ana = Pessoa(bernardo, nome='Ana Cláudia')
    print(Pessoa.cumprimentar(ana))
    print(id(ana))
    print(ana.cumprimentar())
    print(ana.idade)
    print(ana.filhos)
    ana.sobrenome = 'Dias'
    bernardo.olhos = 3
    print(ana.__dict__)
    print(bernardo.__dict__)

    print(Pessoa.olhos)
    print(ana.olhos)
    print(bernardo.olhos)
    del bernardo.olhos
    print(bernardo.olhos)

