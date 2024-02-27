from biblioteca import (
    Biblioteca, 
    biblioteca1,
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

    def mostrar_livro(self):
        # Retorna os dados do livro selecionado
        return self.listar('titulo', self.livro)

    def gera_nova_lista_livro(self, devolucao=False):
        novo_arq = []

        for livros in ABRIR_ARQUIVO_LIVRO:
            if self.mostrar_livro()[0] == {
                meu_normalize(chave.lower()):
                meu_normalize(valor.lower()) for chave, valor in livros.items()
            }:

                quantidade_nova = int(livros.get('Quantidade'))
                quantidade_nova += 1 if devolucao else  -1
                livros.update({'Quantidade': quantidade_nova})

            # Adiciona os dados alterados na lista criada anteriormente
            novo_arq.append(livros)

        return novo_arq

    def gera_nova_lista_biblioteca(self, devolucao=False):
        novo_arq_biblioteca = []

        for bibliotecas in ABRIR_ARQUIVO_BIBLIOTECA:

            if self.biblioteca.nome in bibliotecas.get('Nome da Biblioteca'):

                quantidade_nova = int(bibliotecas.get('Quantidade de Catálogos'))
                quantidade_nova += 1 if devolucao else -1
                bibliotecas.update({'Quantidade de Catálogos': quantidade_nova})

            novo_arq_biblioteca.append(bibliotecas)

        return novo_arq_biblioteca
    
    def emprestimo_devolucao(self, eh_devolucao=False):

        if eh_devolucao:
            escrita_livro(self.gera_nova_lista_livro(True), CABECALHO)
            escrita_biblioteca(self.gera_nova_lista_biblioteca(True), CABECALHO_BIBLIOTECA)

            return 'Devolução feita com sucesso'

        escrita_livro(self.gera_nova_lista_livro(), CABECALHO)
        escrita_biblioteca(self.gera_nova_lista_biblioteca(), CABECALHO_BIBLIOTECA)

        return 'Emprestimo feito com sucesso'

gabriel = Emprestimo(biblioteca1, 'gPinheiro', 'a guerra dos tronos')
gabriel.cadastrar_usuario('gabriel', '23.2333-09', 'rua 123', '08/09/2004', 'masculino')
