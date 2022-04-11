import random

def gerar_palavra_secreta():

    with open("palavras.txt") as file:
        lista_de_palavras = [line.rstrip().capitalize() for line in file]
        
    indice_aleatorio = random.randint(0, 6025)
    return lista_de_palavras[indice_aleatorio]