
import unicodedata

def remove_acentos(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def valida_palavra(palavra):     
    return remove_acentos(palavra.lower().strip())


def frequencia_letras(palavra):
       
    frequencia_letras = {}
    for letra in palavra:
        if letra not in frequencia_letras:
            frequencia_letras[letra] = 1
        else:
            frequencia_letras[letra] += 1
    return frequencia_letras


def letras_certas(chute, gabarito):

    acertos = 0
    
    letras_utilizadas = {}
    
    gabarito_puro = gabarito
    gabarito_limpo = valida_palavra(gabarito)
    

    frequencia_letras_do_gabarito = frequencia_letras(gabarito_limpo)
    
    
    reset = "\u001b[0m"
    verde = "\u001b[32m"
    amarelo = "\u001b[33m"
    
    # reset = ""
    # verde = ""
    # amarelo = ""
    

    nova_palavra = [" ", " ", " ", " ", " "]
    
    # Letras certas, nos lugares certo
    for indice, letra in enumerate(chute):
        
        if letra == gabarito_limpo[indice]:

            acertos += 1

            if letra not in letras_utilizadas:
                letras_utilizadas[letra] = 1
            else:
                letras_utilizadas[letra] += 1

            nova_palavra[indice] = verde + gabarito_puro[indice].upper() + reset
            frequencia_letras_do_gabarito[letra] -= 1

            if gabarito_limpo.count(letra) == letras_utilizadas[letra]:
                frequencia_letras_do_gabarito[letra] = 0

    for indice, letra in enumerate(chute):

        if letra in gabarito_limpo and frequencia_letras_do_gabarito[letra] > 0 and nova_palavra[indice] == " " :
            nova_palavra[indice] = amarelo + chute[indice] + reset
            frequencia_letras_do_gabarito[letra] -= 1

    return "".join(nova_palavra).replace(" ", "_"), acertos


def valida_chute(palavra):

    if len(palavra) > 5:
        return False, "Palavra tem mais de 5 caracteres!"
    
    if len(palavra) < 5:
        return False, "Palavra tem menos de 5 caracteres!"

    if palavra != remove_acentos(palavra):
        return False, "Insira uma palavra sem acentos"
    
    for num in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]:
        if num in palavra:
            return False, "Insira uma palavra sem números! "

    return True, "OK"


def recebe_input_usuario():

    while True:
        chute_do_usuario = input("Insira uma palavra: ").strip()

        chute_do_usuario_validado = valida_palavra(chute_do_usuario)

        foi_sucesso, status = valida_chute(chute_do_usuario_validado)

        if foi_sucesso:
            return chute_do_usuario_validado
        else:
            print(status)


def valida_input_usuario(pergunta, respota1, respota2):

    input_do_usuario = input(pergunta)
    while True:

        if input_do_usuario == respota1 or input_do_usuario == respota2:
            return input_do_usuario
        else:
            input_do_usuario =  input(f"Escolha uma dessas duas respostas: {respota1} ou {respota2}!")


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