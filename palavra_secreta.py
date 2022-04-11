import random

def gerar_palavra_secreta(lista_de_palavras):
    indice_aleatorio = random.randint(0, 6025)
    return lista_de_palavras[indice_aleatorio]


def criar_lista_de_palavras():
    with open("palavras.txt") as file:
        lista_de_palavras = [line.rstrip().capitalize() for line in file]
    return lista_de_palavras