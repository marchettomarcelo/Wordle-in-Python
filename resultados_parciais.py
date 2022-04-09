


def parcial_das_letras_utilizadas(status_das_letras):

    reset = "\u001b[0m"
    verde = "\u001b[32m"
    amarelo = "\u001b[33m"

    print("")
    print("#############################################")
    print("")

    for status, lista in status_das_letras.items():
        
        if status == "n_usadas":
            print("Letras ainda não utilizadas: ", " ".join(lista))
        
        if status == "presente" and len(lista) > 0:
            print(amarelo + "Letras presentes na palavra: ", " ".join(lista) + reset)
        
        if status == "correto" and len(lista) > 0:
            print(verde+ "Letras nas posições corretas: ", " ".join(lista) + reset)
        
        if status == "ausente" and len(lista) > 0:
            print("Letras ausentes na palavra: ", " ".join(lista))
    
    print("")
    print("#############################################")
    print("")