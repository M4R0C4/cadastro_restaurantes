import os

def exibir_subtitulo(texto):
    '''Essa função exibe o subtítulo da opção escolhida no Menu Principal'''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()
