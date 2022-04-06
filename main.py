from funcoes import remove_acentos
from palavra_secreta import gerar_palavra_secreta



def valida_chute(palavra):

    if len(palavra) > 6:
        return False, "Palavra tem mais de 6 caracteres!"
    
    if len(palavra) < 6:
        return False, "Palavra tem menos de 6 caracteres!"

    if palavra != remove_acentos(palavra):
        return False, "Insira uma palavra sem acentos"
    
    for num in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]:
        if num in palavra:
            return False, "Insira uma palavra sem números! "

    return True, "OK"




while True:

    palavra_secreta = gerar_palavra_secreta()
    

    for rodada in range(1,7):


        print(f"Você está na rodada {rodada}!")

        while True:
            chute_do_usuario = input("Insira uma palavra: ").strip()

            foi_sucesso, status = valida_chute(chute_do_usuario)

            if foi_sucesso:
                
                break
            else:
                print(status)
        

