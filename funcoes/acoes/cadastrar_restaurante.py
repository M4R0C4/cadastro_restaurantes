from models.restaurante import Restaurante

def cadastrar_restaurante():
    nome_restaurante = input('Nome do restaurante: ')
    categoria_restaurante = input('Categoria restaurante: ')
    novo_restaurante = Restaurante(nome_restaurante,categoria_restaurante)
    print(f'\n O restaurante {nome_restaurante} de categoria: {categoria_restaurante}, foi criado com sucesso!')
    print(novo_restaurante)
    #voltar_menu_principal()
    #return nome_restaurante