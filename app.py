import os
'''Importações para criar e manipular de objetos'''
from models.restaurante import Restaurante
from models.cardapio.prato import Prato
from models.cardapio.bebida import Bebida
from models.cardapio.sobremesa import Sobremesa
'''Importações de funções para exibir informações'''
from funcoes.exibicao.exibir_menu_principal import exibindo_menu_principal

'''Importações de funções para realizar ações'''
from funcoes.acoes.escolhendo_opcao_menu_principal import escolhendo_opcao_menu_principal






def menu_novo_restaurante(novo_restaurante):
    print('O que deseja fazer a seguir\n')
    print('1. Inserir itens no cardápio')
    print('2. Ativar restaurante')
    print('3. Voltar ao Menu Principal')

    escolha = int(input('Digite o Nº da Opção: '))
    if escolha == 1:
        print('adicionar novos itens do cardápio')
        itens_cardapio(novo_restaurante)
    elif escolha == 2:
        print('adiconar/desativar restaurante')
    elif escolha == 3: 
        print('Voltar ao menu anterior')

def itens_cardapio(novo_restaurante):
    acabou = False
    print(f'Itens que podem ser inseridos no cardápio do restaurante {novo_restaurante}')
    print('1. Bebidas')
    print('2. Pratos')
    print('3. Sobremesas')
    escolha = int(input('Escolha o tipo de item a ser inserido: '))
    if escolha == 1:
        print('inserir bebida')
        inserir_bebida(novo_restaurante)
    elif escolha == 2:
        print('inserir pratos')
        inserir_prato(novo_restaurante)
    elif escolha == 3:
        print('inserir sobremesas')
        inserir_sobremesa(novo_restaurante)
    while not acabou:
        itens_cardapio()
        print('Deseja inserir algum outro item? [S/N]')
        proposicao = input('').upper()
        if proposicao in 'SIM':
            continue
        elif proposicao in "NNÃONAO":
            acabou = True

def inserir_sobremesa(novo_restaurante):
    nome_da_sobremesa = str(input('Nome da Sobremesa: '))
    preco_sobremesa = str(input('Preço da Sobremesa: '))
    descricao_sobremesa = str(input('Descrição breve da Sobremesa: '))
    nova_sobremesa = Sobremesa(nome_da_sobremesa,preco_sobremesa,descricao_sobremesa)
    novo_restaurante.adicionar_no_cardapio(nova_sobremesa)
    print(f'A sobremesa {nova_sobremesa} foi inserido no restaurante {novo_restaurante}')

def inserir_prato(novo_restaurante):
    nome_da_prato = str(input('Nome da Prato: '))
    preco_prato = str(input('Preço da Prato: '))
    descricao_prato = str(input('Descrição breve da Prato: '))
    novo_prato = Prato(nome_da_prato,preco_prato,descricao_prato)
    novo_restaurante.adicionar_no_cardapio(novo_prato)
    print(f'A prato {novo_prato} foi inserido no restaurante {novo_restaurante}')

def inserir_bebida(novo_restaurante):
    nome_da_bebida = str(input('Nome da Bebida: '))
    preco_bebida = str(input('Preço da Bebida: '))
    descricao_bebida = str(input('Descrição breve da Bebida: '))
    nova_bebida = Bebida(nome_da_bebida,preco_bebida,descricao_bebida)
    novo_restaurante.adicionar_no_cardapio(nova_bebida)
    print(f'A bebida {nova_bebida} foi inserido no restaurante {novo_restaurante}')

def cancelar_operacao():
    pass



def main():
    os.system('cls')
    exibindo_menu_principal()
    escolhendo_opcao_menu_principal()

#    Restaurante.listar_restaurantes()


if __name__ == '__main__':

    main()
