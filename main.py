from funcoes import *
from validacao import *
from palavra_secreta import gerar_palavra_secreta

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
    "lugar_errado" : [],
    "certa": [],
    "inexistente" : []
}

while True:

    # palavra_secreta = gerar_palavra_secreta()
    palavra_secreta = "falaf"
    print(palavra_secreta)
    
    for rodada in range(1,7):

        print(f"Você está na rodada {rodada}!")
        
        # palavra em lowrcase, sem acentos e no tamanho correto
        chute_do_usuario = recebe_input_usuario()

        placar_da_rodada, acertos, status_das_letras  = letras_certas(chute_do_usuario, palavra_secreta, status_das_letras)

        # print(status_das_letras)
        print(placar_da_rodada)

        if acertos == 5:
            print(f"Você ganhou em {rodada} tentativas!")
            
            tentativas[str(rodada)] += 1
            tentativas["n_tentativas"] +=1

            resumo_das_rodadas = resumo_de_rodadas(tentativas)
            print(resumo_das_rodadas)

            break
        
        if rodada == 6:

            tentativas["Não acertou"] += 1
            tentativas["n_tentativas"] +=1
            print("voce perdeu")

            resumo_das_rodadas = resumo_de_rodadas(tentativas)
            print(resumo_das_rodadas)


    jogar_novamente = valida_input_usuario("Deseja jogar novamente? Digite sim(s) ou não(n): ", "s", "n")
    if jogar_novamente == "n":
        break

        

