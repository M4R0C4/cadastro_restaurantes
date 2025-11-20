from models.cardapio.item_cardapio import ItemCardapio #importando a classe Pai

class Prato(ItemCardapio): #declara de onde vamos herdar algumas características
    def __init__(self, nome, preco, descricao):
        super().__init__(nome,preco) # buscando os atributos da classe Pai
        self.descricao = descricao        
    
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)