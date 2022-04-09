
import unicodedata

def remove_acentos(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def valida_palavra(palavra):     
    return remove_acentos(palavra.lower())


def frequencia_letras(palavra):
       
    frequencia_letras = {}
    for letra in palavra:
        if letra not in frequencia_letras:
            frequencia_letras[letra] = 1
        else:
            frequencia_letras[letra] += 1
    return frequencia_letras


def letras_certas(chute, gabarito):

    letras_utilizadas = {}
    
    gabarito_puro = gabarito
    gabarito_limpo = valida_palavra(gabarito)
    

    frequencia_letras_do_gabarito = frequencia_letras(gabarito_limpo)
    

    nova_palavra = [" ", " ", " ", " ", " ", " "]
    
    # Letras certas, nos lugares certo
    for indice, letra in enumerate(chute):
        
        if letra == gabarito_limpo[indice]:

            if letra not in letras_utilizadas:
                letras_utilizadas[letra] = 1
            else:
                letras_utilizadas[letra] += 1

            nova_palavra[indice] = gabarito_puro[indice].upper()
            frequencia_letras_do_gabarito[letra] -= 1

            if gabarito_limpo.count(letra) == letras_utilizadas[letra]:
                frequencia_letras_do_gabarito[letra] = 0

    for indice, letra in enumerate(chute):

        if letra in gabarito_limpo and frequencia_letras_do_gabarito[letra] > 0 and nova_palavra[indice] == " " :
            nova_palavra[indice] = chute[indice]
            frequencia_letras_do_gabarito[letra] -= 1

    
    return "".join(nova_palavra).replace(" ", "_")
