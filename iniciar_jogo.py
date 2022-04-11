
def iniciar(renovar_tentativas = True):
    tentativas =  {
        "n_tentativas": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "Não acertou":  0
    }

    status_das_letras = {
        "n_usadas" : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        "presente" : [],
        "correto": [],
        "ausente" : []
     
    }

    historico_de_placares = []

    if renovar_tentativas :
        return tentativas, status_das_letras, historico_de_placares
    else:
        return status_das_letras, historico_de_placares