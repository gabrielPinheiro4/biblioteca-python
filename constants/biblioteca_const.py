from biblioteca_python.utils.funcoes import ler_arquivo

#Cabeçalho para escrita do arquivo bibliotecas.csv
CABECALHO_BIBLIOTECA = [
    'Nome da Biblioteca', 
    'Endereço', 
    'Número', 
    'Quantidade de Catálogos'
]

# Variável para abrir o arquivo bibliotecas.csv
ABRIR_ARQUIVO_BIBLIOTECA = ler_arquivo('bibliotecas.csv')