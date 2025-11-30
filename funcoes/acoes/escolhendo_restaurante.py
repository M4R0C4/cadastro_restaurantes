from models.restaurante import Restaurante

def escolhendo_restaurante(): #! Melhorar este caralho
    print('▲▲▲ Escolha um dos Restaurantes acima ▲▲▲')
    escolha_usuario = input('Digite o nome do restaurante: ')
    encontrado = False
    
    while not encontrado:
        for restaurante in Restaurante.catalogo_de_restaurantes:
            if escolha_usuario == restaurante.nome:
                print(f'\nRestaurante encontrado: {restaurante.nome}')
                encontrado =  True

        if not encontrado:
            print('Não encontrou')
        

