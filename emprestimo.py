from biblioteca import Biblioteca
from usuario import Usuario
from livro import Livro
import unicodedata
from csv import *


class Emprestimo(Usuario, Livro, Biblioteca):
    def __init__(self, biblioteca, usuario, livro):
        self.__biblioteca = biblioteca
        self.__usuario = usuario
        self.__livro = livro

    @property
    def biblioteca(self):
        return self.__biblioteca
    
    @property
    def usuario(self):
        return self.__usuario
    
    @property
    def livro(self):
        return self.__livro

    @property
    def quantidade_livro(self):
        for livro in self.mostrar_livro():
            return int(livro['quantidade'])
        
    @property
    def quantidade_livro_biblioteca(self):
        for livro_biblioteca in self.mostrar_biblioteca():
            return int(livro_biblioteca['quantidade de catalogos'])

    
    def cadastrar_usuario(self,  
                cpf, 
                endereco, 
                data_nascimento,
                genero_preferido):
        super().__init__(
            self.usuario,
            cpf, 
            endereco, 
            data_nascimento,
            genero_preferido
            )
        

    def mostrar_biblioteca(self):
        nova_lista_biblioteca = []
        for biblioteca in self.csv_biblioteca():
            nova_lista_biblioteca.append(
                {unicodedata.normalize(
                    'NFD', chave.lower()).encode(
                        'ascii', 'ignore').decode(
                            'utf-8'): unicodedata.normalize(
                                'NFD', valor.lower()).encode(
                                    'ascii', 'ignore').decode(
                                        'utf-8') for chave, valor in biblioteca.items()})
            
        biblioteca_selecionada = list(
            filter(
                lambda x: unicodedata.normalize(
                    'NFD', self.biblioteca.lower()).encode(
                        'ascii', 'ignore').decode(
                            'utf-8') in x['nome da biblioteca'], nova_lista_biblioteca
            )
        )

        return biblioteca_selecionada


    def mostrar_livro(self):
        return self.listar('titulo', self.livro)
    

    def emprestimo(self):
        for livro in self.mostrar_livro():
            for biblioteca in self.mostrar_biblioteca():
                # with open('livros.csv') as arq:
                #     csv = DictReader(arq)
                #     for linha in csv:
                #         print({chave.lower(): valor.lower() for chave, valor in linha.items()})
                        
                for x in self.listar('titulo', self.livro):
                    int(x['quantidade']) - 1



eu = Emprestimo('Biblioteca Técnica de Iguatu', 'gabriel', '1984')
eu.cadastrar_usuario('23.2333-09', 'rua da pica', '08/092004', 'lbgt')
# print(eu.mostrar_biblioteca())
# print(eu.mostrar_livro())
# print(eu.mostra_usuario())
# print(eu.mostrar_livro())
# print(eu.emprestimo())
# print(eu.mostrar_livro())