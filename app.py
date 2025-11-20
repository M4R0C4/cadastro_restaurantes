from models.restaurante import Restaurante
import os
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato
from models.cardapio.sobremesa import Sobremesa


def finalizando_app():
    '''Função que finaliza o app'''
    exibir_subtitulo('Finalizando o APP 👋')
    print(' ')

def exibir_subtitulo(texto):
    '''Essa função exibe o subtítulo da opção escolhida no Menu Principal'''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    '''Essa função exibe a mensagem de opção invalida e chama outra função que retorna ao Menu Principal'''
    print('A opção escolhida é invalida. Tente novamente\n')
    voltar_menu_principal()

def voltar_menu_principal():
    '''função que retorna ao menu principal'''
    input('Digite qualquer tela para retornar ao Menu Principal: ')
    main()

def exibindo_menu_principal():
    print('1. Cadastrar restaurante 🛠')
    print('2. Listar restaurante 🏘')
    print('3. Área de Ativação/Desativação de Restaurantes')
    print('4. Sair\n')

def escolhendo_opcao_menu_principal():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            Restaurante.listar_restaurantes()
            voltar_menu_principal()
        elif opcao_escolhida == 3:
            alternar_status_restaurante()
            pass
        elif opcao_escolhida == 4:
            finalizando_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def cadastrar_restaurante():
    nome_restaurante = input('Nome do restaurante: ')
    categoria_restaurante = input('Categoria restaurante: ')
    novo_restaurante = Restaurante(nome_restaurante,categoria_restaurante)
    print(f'\n O restaurante {nome_restaurante} de categoria: {categoria_restaurante}, foi criado com sucesso!')
    voltar_menu_principal()
    #return nome_restaurante

def alternar_status_restaurante():
    print('Alterando Status do Restaurante!')
    restaurante = input('Digite o nome do restaurante: ')
    for restaurante in Restaurante.catalogo_de_restaurantes:
        restaurante.alternar_estado()       
    voltar_menu_principal()

restaurante1 = Restaurante('Spoletto','Massas')
restaurante2 = Restaurante('Habbibs','Arabe')

bebida_simples = Bebida('Suco de Laranja',7.5,'600ml')
bebida_alcolica = Bebida('Caipirinha', 5,'500ml')

prato1 = Sobremesa('Docin', 15.5, 'Feijão com carne suculentas do porco.')
prato2 = Prato('Salada Ceasar',22,'Salada de folhas e molho agridoce.')

bebida_simples.aplicar_desconto()
prato1.aplicar_desconto()

restaurante1.adicionar_no_cardapio(bebida_simples)
restaurante1.adicionar_no_cardapio(prato1)

def main():
    restaurante1.exibir_cardapio
#    os.system('cls')
#    exibindo_menu_principal()
#    escolhendo_opcao_menu_principal()

#    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()