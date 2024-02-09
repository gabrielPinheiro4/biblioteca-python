from biblioteca_python.utils.funcoes import ler_arquivo

#Cabeçalho para escrita do arquivo livros.csv
CABECALHO = [
    'Título', 
    'Autor', 
    'Data de Lançamento',
    'Gênero', 
    'Quantidade'
]

# Variável para abrir o arquivo livros.csv
ABRIR_ARQUIVO_LIVRO = ler_arquivo('livros.csv')