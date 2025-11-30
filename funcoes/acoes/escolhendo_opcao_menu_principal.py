from models.restaurante import Restaurante
from funcoes.acoes.escolhendo_restaurante import escolhendo_restaurante
#from funcoes.acoes.voltar_menu_principal import voltar_menu_principal
from funcoes.exibicao.opcao_invalida import opcao_invalida
from funcoes.acoes.finalizando_app import finalizando_app
from funcoes.acoes.alternar_status_restaurante import alternar_status_restaurante
from funcoes.acoes.cadastrar_restaurante import cadastrar_restaurante

def escolhendo_opcao_menu_principal():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            print('CADASTRAR RESTAURANTE')
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            Restaurante.listar_restaurantes()
            escolhendo_restaurante()
            #voltar_menu_principal()
        elif opcao_escolhida == 3:
            alternar_status_restaurante()
            pass
        elif opcao_escolhida == 4:
            finalizando_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()