from biblioteca import (
    Biblioteca, 
    biblioteca1,
    biblioteca2,
    biblioteca3,
    biblioteca4
    )

from usuario import Usuario
from livro import Livro
from utils.funcoes import (
    meu_normalize,
    escrita_livro,
    escrita_biblioteca,
    )
 
from constants.biblioteca_const import (
    CABECALHO_BIBLIOTECA, 
    ABRIR_ARQUIVO_BIBLIOTECA
    ) 
from constants.livro_const import (
    CABECALHO, 
    ABRIR_ARQUIVO_LIVRO
    )


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
    
    # Realiza o cadastro do usuário    
    def cadastrar_usuario(
            self,
            nome_completo, 
            cpf, 
            endereco, 
            data_nascimento, 
            genero_preferido
            ):
        super().__init__(
            nome_completo, 
            cpf, 
            endereco, 
            data_nascimento, 
            genero_preferido
            )
        
    # Retorna os dados do livro selecionado
    def mostrar_livro(self):
        return self.listar('titulo', self.livro)
    
    def emprestimo(self):

        # Cria duas listas vazias, uma para as mudanças do arquivo livros.csv
        # e outra para as mudanças do arquivo bibliotecas.csv
        novo_arq = []
        novo_arq_biblioteca = []
        
        # Faz um for em livros.csv
        for livros in ABRIR_ARQUIVO_LIVRO:

            # Se o livro selecionado pelo usuario for igual a um 
            # livro dentro de livros.csv
            if self.mostrar_livro()[0] == {
                meu_normalize(chave.lower()):
                meu_normalize(valor.lower()) for chave, valor in livros.items()
            }:

                # Diminui a quantidade do livro no arquivo livros.csv
                    quantidade_nova = int(livros.get('Quantidade'))
                    quantidade_nova -= 1
                    livros.update({'Quantidade': quantidade_nova})

            # Adiciona os dados alterados na lista criada anteriormente
            novo_arq.append(livros)
            
        # Sobreescreve os dados do arquivo livros.csv com os dados da lista
        escrita_livro(novo_arq, CABECALHO)
        
        for bibliotecas in ABRIR_ARQUIVO_BIBLIOTECA:

            if self.biblioteca.nome in bibliotecas.get('Nome da Biblioteca'):

                quantidade_nova = int(bibliotecas.get('Quantidade de Catálogos'))
                quantidade_nova -= 1
                bibliotecas.update({'Quantidade de Catálogos': quantidade_nova})

            novo_arq_biblioteca.append(bibliotecas)
        escrita_biblioteca(novo_arq_biblioteca, CABECALHO_BIBLIOTECA)

        return 'Emprestimo feito com sucesso'
    
    def devolver_emprestimo(self):
        novo_arq = []
        novo_arq_biblioteca = []
        
        for livros in ABRIR_ARQUIVO_LIVRO:

            if self.mostrar_livro()[0] == {
                meu_normalize(chave.lower()):
                meu_normalize(valor.lower()) for chave, valor in livros.items()
            }:
                quantidade_nova = int(livros.get('Quantidade'))
                quantidade_nova += 1
                livros.update({'Quantidade': quantidade_nova})

            novo_arq.append(livros)
        escrita_livro(novo_arq, CABECALHO)

        for bibliotecas in ABRIR_ARQUIVO_BIBLIOTECA:

            if self.biblioteca.nome in bibliotecas.get('Nome da Biblioteca'):

                quantidade_nova = int(bibliotecas.get('Quantidade de Catálogos'))
                quantidade_nova += 1
                bibliotecas.update({'Quantidade de Catálogos': quantidade_nova})

            novo_arq_biblioteca.append(bibliotecas)
        escrita_biblioteca(novo_arq_biblioteca, CABECALHO_BIBLIOTECA)

        return 'Livro devolvido com sucesso'

    
gabriel = Emprestimo(biblioteca1, 'gPinheiro', 'a guerra dos tronos')
gabriel.cadastrar_usuario('gabriel', '23.2333-09', 'rua 123', '08/09/2004', 'masculino')
