from biblioteca import Biblioteca
from usuario import Usuario
from livro import Livro
import unicodedata


class Emprestimo(Usuario):
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
        

    def mostrar_biblioteca(self, biblioteca_procurada):
        nova_lista_biblioteca = []
        for biblioteca in Biblioteca.csv_biblioteca():
            nova_lista_biblioteca.append(
                {unicodedata.normalize(
                    'NFD', chave.lower()).encode(
                        'ascii', 'ignore').decode(
                            'utf-8'): unicodedata.normalize(
                                'NFD', valor.lower()).encode(
                                    'ascii', 'ignore').decode(
                                        'utf-8') for chave, valor in biblioteca.items()})
            
        print(nova_lista_biblioteca)
        




eu = Emprestimo(1, 'Gabriel Pinheiro', 1)
eu.cadastrar_usuario('23.2333-09', 'rua da pica', '08/092004', 'lbgt')
print(eu.mostrar_biblioteca('a'))