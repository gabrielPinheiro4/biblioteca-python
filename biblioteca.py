from csv import *

class Biblioteca:

    @staticmethod
    def csv_biblioteca():
        with open('bibliotecas.csv') as arq:
            csv = DictReader(arq)
            return [linha for linha in csv]

    @staticmethod
    def csv_arquivo_biblioteca(header):
        with open('bibliotecas.csv') as arq:
            csv = DictReader(arq)
            return [x[header] for x in csv]

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

    
a = Biblioteca(
    Biblioteca.csv_arquivo_biblioteca('Nome da Biblioteca'),
    Biblioteca.csv_arquivo_biblioteca('Endereço'),
    Biblioteca.csv_arquivo_biblioteca('Número'),
    Biblioteca.csv_arquivo_biblioteca('Quantidade de Catálogos')
)

# print(a.numero)
