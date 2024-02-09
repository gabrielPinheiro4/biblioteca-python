from utils.funcoes import ler_arquivo


class Biblioteca:

    def __init__(self, nome, endereco, numero, quantidade_catalogo):
        self.__nome = nome
        self.__endereco = endereco
        self.__numero = numero
        self.__quantidade_catalogo = quantidade_catalogo

    @property
    def nome(self):
        return self.__nome
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def quantidade_catalogo(self):
        return self.__quantidade_catalogo

    # Cria uma lista com os objetos instanciados da classe Biblioteca
    def selecionar_biblioteca():
        return [
            Biblioteca(*lista) for lista in ler_arquivo('bibliotecas.csv', aninhada=True)
        ]
                         
    def __repr__(self):
        return (
            f'Nome: {self.nome}\n'
            f'Número: {self.numero}\n'
            f'Endereço: {self.endereco}\n'
            f'Quantidade de Catálogos: {self.quantidade_catalogo}'
        )


biblioteca1, biblioteca2, biblioteca3, biblioteca4 = Biblioteca.selecionar_biblioteca()
