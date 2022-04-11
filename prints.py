
def printar_palcar_do_jogo(historico_de_placares):
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for placar in historico_de_placares:
        print(placar)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")

def printar_finalizacao(palavra_secreta):
    print("")            
    print("!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!")
    print("")            
    print("A palavra secreta é: ")
    print(palavra_secreta)
    print("")            
    print("!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!")
    print("")            
    print("voce perdeu")


def resumo_de_rodadas(dict_tentativas):
    print(f''' parcial:
            Tentativas 1: {dict_tentativas["1"] /dict_tentativas["n_tentativas"]*100:.2f}%
            Tentativas 2: {dict_tentativas["2"] /dict_tentativas["n_tentativas"]*100:.2f}%
            Tentativas 3: {dict_tentativas["3"] /dict_tentativas["n_tentativas"]*100:.2f}%
            Tentativas 4: {dict_tentativas["4"] /dict_tentativas["n_tentativas"]*100:.2f}%
            Tentativas 5: {dict_tentativas["5"] /dict_tentativas["n_tentativas"]*100:.2f}%
            Tentativas 6: {dict_tentativas["6"] /dict_tentativas["n_tentativas"]*100:.2f}%
            Não acertou:  {dict_tentativas["Não acertou"] /dict_tentativas["n_tentativas"]*100:.2f}%
        ''')
    return