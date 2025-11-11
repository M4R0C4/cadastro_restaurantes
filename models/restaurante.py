from models.avaliacao import Avaliacao

class Restaurante: #Classe Restaurante com 3 caracteristicas: nome, categoria e ativo
    catalogo_de_restaurantes = [] #local onde será armazenado a lista de restaurantes

    def __init__(self, nome, categoria): #método CONSTRUTOR que exige que, quando a classe seja chamada, ela tenha as caracteristicas.
        self._nome = nome.title() #busca na iteração, o NOME atribuido a classe Restaurante
        self._categoria = categoria.upper() #busca na iteração, a CATEGORIA atribuida a classe Restaurante
        self._ativo = False #atributo privado
        self._avaliacao = []
        Restaurante.catalogo_de_restaurantes.append(self) #assim que o novo restaurante é criado na classe Restaurantes, é adicionado no catálogo

    def __str__(self): #método que exibe na forma de string as características da classe
        return f'{self._nome} | {self._categoria}' #nesse caso, ele exibe Nome | Categoria 

    @classmethod
    def listar_restaurantes(cls): #método que lista os restaurantes do catálogo. Estrutura: Classe.metodo()
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls. catalogo_de_restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo} ')



    @property #modificando o retorno do estado ativo (false ou true) para mostrar os emojis
    def ativo(self):
        return '✅' if self._ativo else '❌'
        #estrutura emoji verde se ativo for True, se não for, emoji vermelho

    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def recebe_avaliacao(self, cliente, nota):
        if  0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 'N/A'
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)

        media= round(soma_das_notas/quantidade_de_notas,1)
        return media
    

