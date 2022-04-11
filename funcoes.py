
from validacao import * 

def frequencia_letras(palavra):
       
    frequencia_letras = {}
    for letra in palavra:
        if letra not in frequencia_letras:
            frequencia_letras[letra] = 1
        else:
            frequencia_letras[letra] += 1
    return frequencia_letras


def letras_certas(chute, gabarito, status_das_letras):

    reset = "\u001b[0m"
    verde = "\u001b[32m"
    amarelo = "\u001b[33m"

    acertos = 0
    
    # Dict para keep track da quantidade de letras utilizadas
    letras_utilizadas = {}
    
    # tranforma palavras para comparalas melhor ex: Fogão -> fogao
    chute_puro = chute
    chute_limpo = valida_palavra(chute)
    gabarito_limpo = valida_palavra(gabarito)

    # Dict com a frequencia de casa letra    
    frequencia_letras_do_gabarito = frequencia_letras(gabarito_limpo)

    placar_da_rodada = [" ", " ", " ", " ", " "]
    
    # Loop para colocar as letras certas, nos lugares certos
    # Ele sempre compara o chute limpo com o gabarito limpo
    for indice, letra in enumerate(chute_limpo):
        
        if letra == gabarito_limpo[indice]:
            acertos += 1
            
            # Mas adiciona no placar a letra na forma pura
            placar_da_rodada[indice] = verde + chute_puro[indice].upper() + reset
            frequencia_letras_do_gabarito[letra] -= 1

             # atualizar dict de lógica do feedback do teclado
            if letra in status_das_letras["n_usadas"]:
                status_das_letras["n_usadas"].remove(letra)
                status_das_letras["correto"].append(letra)
            elif letra in status_das_letras["presente"]:
                status_das_letras["presente"].remove(letra)
                status_das_letras["correto"].append(letra)

    # Letras certas, nos lugares certo E letras inexistentes na palavra
    for indice, letra in enumerate(chute_limpo):

        if letra in gabarito_limpo and frequencia_letras_do_gabarito[letra] > 0 and placar_da_rodada[indice] == " " :
                              
            placar_da_rodada[indice] = amarelo + chute_puro[indice] + reset
            frequencia_letras_do_gabarito[letra] -= 1

            # atualizar dict de lógica do feedback do teclado
            if letra in status_das_letras["n_usadas"]:
                status_das_letras["n_usadas"].remove(letra)
                status_das_letras["presente"].append(letra)

        elif placar_da_rodada[indice] == " ":

            placar_da_rodada[indice] = chute_puro[indice]

            # atualizar dict de lógica do feedback do teclado
            if letra in status_das_letras["n_usadas"]:
                status_das_letras["n_usadas"].remove(letra)
                status_das_letras["ausente"].append(letra)


    return "".join(placar_da_rodada).replace(" ", "_"), acertos, status_das_letras



# _------------------------------------------------------------------------------------------------




