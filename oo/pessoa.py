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
        return f'Olá {(self.nome)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):   #CLS faz alusão a CLASSE que está criando esse metodo, no caso Pessoa.
        return f'{cls}, olhos da {cls.olhos} '

class Homem(Pessoa):    # A classe Homem, é uma herança de Pessoa, sendo assim Homem, herda alguns atributos de Pessoa
                        # Com a herança você herda tudo de quem for sua herança.
    def cumprimentar(self):
        cumpriemntar_da_classe_pai = Pessoa.cumprimentar(self)
        return f'{cumpriemntar_da_classe_pai}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

    def cumprimentar(self):
        cumpriemntar_da_classe_pai = super().cumprimentar()  #Sobreescrita da class Pai, independente de quem for a classe
        return f'{cumpriemntar_da_classe_pai}. Um abraço'

if __name__ == '__main__':
    bernardo = Mutante(nome='Bernardo')
    ana = Homem(bernardo, nome='Ana Cláudia')
    print(Pessoa.cumprimentar(ana))
    print(id(ana))
    print(ana.cumprimentar())
    print(ana.idade)
    print(ana.filhos)
    ana.sobrenome = 'Dias'
    print(ana.__dict__)
    print(bernardo.__dict__)

    print(Pessoa.olhos)
    print(ana.olhos)
    print(bernardo.olhos)


    print(Pessoa.metodo_estatico(), ana.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), ana.nome_e_atributos_de_classe())

    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))

    pessoa2 = Homem('Anônimo')
    print(isinstance(pessoa2, Pessoa))
    print(isinstance(pessoa2, Homem))

    print(ana.cumprimentar())
    print(bernardo.cumprimentar())
