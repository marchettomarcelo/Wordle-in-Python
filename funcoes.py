
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
    
    gabarito_puro = gabarito
    gabarito_limpo = valida_palavra(gabarito)
    
    frequencia_letras_do_gabarito = frequencia_letras(gabarito_limpo)


    placar_da_rodada = [" ", " ", " ", " ", " "]
    
    # Letras certas, nos lugares certo
    for indice, letra in enumerate(chute):
        
        if letra == gabarito_limpo[indice]:
            acertos += 1
            
            # Atualiza o p
            placar_da_rodada[indice] = verde + gabarito_puro[indice].upper() + reset
            frequencia_letras_do_gabarito[letra] -= 1

             # atualizar dict de lógica do feedback do teclado
            if letra in status_das_letras["n_usadas"]:
                status_das_letras["n_usadas"].remove(letra)
                status_das_letras["correto"].append(letra)
            
            elif letra in status_das_letras["presente"]:
                status_das_letras["presente"].remove(letra)
                status_das_letras["correto"].append(letra)

    # Letras certas, nos lugares certo E letras inexistentes na palavra
    for indice, letra in enumerate(chute):

        if letra in gabarito_limpo and frequencia_letras_do_gabarito[letra] > 0 and placar_da_rodada[indice] == " " :
            
            # atualizar dict de lógica do feedback do teclado
            if letra in status_das_letras["n_usadas"]:
                status_das_letras["n_usadas"].remove(letra)
                status_das_letras["presente"].append(letra)
                  
            placar_da_rodada[indice] = amarelo + chute[indice] + reset
            frequencia_letras_do_gabarito[letra] -= 1

        elif placar_da_rodada[indice] == " ":
            placar_da_rodada[indice] = chute[indice]

            # atualizar dict de lógica do feedback do teclado
            if letra in status_das_letras["n_usadas"]:
                status_das_letras["n_usadas"].remove(letra)
                status_das_letras["ausente"].append(letra)


    return "".join(placar_da_rodada).replace(" ", "_"), acertos, status_das_letras



def recebe_input_usuario(lista_de_palavras):

    while True:
        
        chute_do_usuario = input("Insira uma palavra: ").strip().capitalize()
        foi_sucesso, status = valida_chute(chute_do_usuario)
     
        if foi_sucesso:
            if chute_do_usuario in lista_de_palavras:
                return valida_palavra(chute_do_usuario)
            else:
                print("Palávra inválida! ")
        else:
            print(status)




def resumo_de_rodadas(dict_tentativas):
    return f''' parcial:
            Tentativas 1: {dict_tentativas["1"] /dict_tentativas["n_tentativas"]*100:.2f}%
            Tentativas 2: {dict_tentativas["2"] /dict_tentativas["n_tentativas"]*100:.2f}%
            Tentativas 3: {dict_tentativas["3"] /dict_tentativas["n_tentativas"]*100:.2f}%
            Tentativas 4: {dict_tentativas["4"] /dict_tentativas["n_tentativas"]*100:.2f}%
            Tentativas 5: {dict_tentativas["5"] /dict_tentativas["n_tentativas"]*100:.2f}%
            Tentativas 6: {dict_tentativas["6"] /dict_tentativas["n_tentativas"]*100:.2f}%
            Não acertou:  {dict_tentativas["Não acertou"] /dict_tentativas["n_tentativas"]*100:.2f}%
        '''