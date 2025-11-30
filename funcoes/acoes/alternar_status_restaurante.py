from models.restaurante import Restaurante
#from funcoes.acoes.voltar_menu_principal import voltar_menu_principal

def alternar_status_restaurante():
    print('Alterando Status do Restaurante!')
    restaurante = input('Digite o nome do restaurante: ')
    for restaurante in Restaurante.catalogo_de_restaurantes:
        restaurante.alternar_estado()       
    #voltar_menu_principal()