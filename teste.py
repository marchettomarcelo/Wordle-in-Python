# from validacao import *
# from funcoes import *

# def criar_lista_de_palavras():
#     with open("palavras.txt") as file:
#         lista_de_palavras = [line.rstrip().capitalize() for line in file]
#     return lista_de_palavras

# def recebe_input_usuario(lista_de_palavras):

#     while True:
        
#         chute_do_usuario = input("Insira uma palavra: ").strip().capitalize()
#         foi_sucesso, status = valida_chute(chute_do_usuario)
     
#         if foi_sucesso:
#             if chute_do_usuario in lista_de_palavras:
#                 return valida_palavra(chute_do_usuario)
#             else:
#                 print("Palávra inválida! ")
#         else:
#             print(status)


# l = criar_lista_de_palavras()
# print(l)

# x = recebe_input_usuario(l)
# print(x)