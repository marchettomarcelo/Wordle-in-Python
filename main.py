from funcoes import *
from validacao import *
from palavra_secreta import *
from iniciar_jogo import *
from resultados_parciais import *
from prints import *

tentativas, status_das_letras, historico_de_placares = iniciar()
lista_de_palavras = criar_lista_de_palavras()

while True:

    palavra_secreta = gerar_palavra_secreta(lista_de_palavras)
    print("Palavra secreta: ", palavra_secreta)
    
    for rodada in range(1,7):

        print(f"Você está na rodada {rodada}!")
        
        # palavra em lowrcase, sem acentos e no tamanho correto
        chute_do_usuario = recebe_input_usuario(lista_de_palavras)
        
        # Verifica acertos e erros do usuario
        placar_da_rodada, acertos, status_das_letras  = letras_certas(chute_do_usuario, palavra_secreta, status_das_letras)
        historico_de_placares.append(placar_da_rodada)
        
        # Atualizar e imprimir os palacares
        printar_palcar_do_jogo(historico_de_placares)

        # Imprime a parcial das letras
        parcial_das_letras_utilizadas(status_das_letras)

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

            printar_finalizacao(palavra_secreta)

            resumo_das_rodadas = resumo_de_rodadas(tentativas)
            print(resumo_das_rodadas)


    jogar_novamente = valida_input_usuario("Deseja jogar novamente? Digite sim(s) ou não(n): ", "s", "n")
    if jogar_novamente == "n":
        break
    elif jogar_novamente == "s":

        status_das_letras, historico_de_placares = iniciar(renovar_tentativas = False)

        

        

