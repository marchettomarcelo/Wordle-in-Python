import unicodedata

def remove_acentos(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def valida_palavra(palavra):     
    return remove_acentos(palavra.lower().strip())

def valida_chute(palavra):

    if len(palavra) > 5:
        return False, "Palavra tem mais de 5 caracteres!"
    
    if len(palavra) < 5:
        return False, "Palavra tem menos de 5 caracteres!"
    
    for num in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]:
        if num in palavra:
            return False, "Insira uma palavra sem números! "

    return True, "OK"


def valida_input_usuario(pergunta, respota1, respota2):

    input_do_usuario = input(pergunta)
    while True:

        if input_do_usuario == respota1 or input_do_usuario == respota2:
            return input_do_usuario
        else:
            input_do_usuario =  input(f"Escolha uma dessas duas respostas: {respota1} ou {respota2}!")

def recebe_input_usuario(lista_de_palavras):

    while True:
        
        chute_do_usuario = input("Insira uma palavra: ").strip()
        foi_sucesso, status = valida_chute(chute_do_usuario)
     
        if foi_sucesso:
            if chute_do_usuario.capitalize() in lista_de_palavras:
                return chute_do_usuario
            else:
                print("Palávra inválida! ")
        else:
            print(status)