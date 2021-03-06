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

    bibliotecario()
    
    for rodada in range(1,7):

        print(f"Você está na rodada {rodada}!")
        
        # palavra existente, capitalizada, com acentos e no tamanho correto ex: fOgãO -> fogão  
        chute_do_usuario = recebe_input_usuario(lista_de_palavras)

        # Verifica acertos e erros do usuario
        placar_da_rodada, acertos, status_das_letras  = letras_certas(chute_do_usuario, palavra_secreta, status_das_letras)
        historico_de_placares.append(placar_da_rodada)
        
        # Atualizar e imprimir os palacares
        printar_palcar_do_jogo(historico_de_placares)

        # Imprime a parcial das letras
        parcial_das_letras_utilizadas(status_das_letras)

        if acertos == 5:
            
            ganhou()
            
            tentativas[str(rodada)] += 1
            tentativas["n_tentativas"] +=1

            printar_finalizacao(palavra_secreta)
            resumo_de_rodadas(tentativas)
            break
        
        if rodada == 6:

            perdeu()
            
            tentativas["Não acertou"] += 1
            tentativas["n_tentativas"] +=1

            printar_finalizacao(palavra_secreta)

            resumo_de_rodadas(tentativas)

    jogar_novamente = valida_input_usuario("Deseja jogar novamente? Digite sim(s) ou não(n): ", "s", "n")
    
    if jogar_novamente == "n":
        break
    elif jogar_novamente == "s":

        status_das_letras, historico_de_placares = iniciar(renovar_tentativas = False)

        

        

