'''
Classe: 
    ArquivoReadme

Objetivo: 
    Manipular leitura de arquivos no formato markdown que servirão de entrada
    para métodos de formatação dos arquivos.
'''

import glob

class ArquivoReadme:
    '''
        Método: geraListaArquivosReadme
        Objetivo: Ler o nome dos arquivos no formato markdown e adicioná-los a uma lista
        Retorno: Lista contendo todos os nomes dos arquivos readmes
        Parâmetros: Não recebe parâmetros
    '''
    def geraListaArquivosReadme():
        listaDeNomesArquivosReadmes = []
        for nomeArquivo in glob.glob("readmes/*.md"):
            listaDeNomesArquivosReadmes.append(nomeArquivo)
        return listaDeNomesArquivosReadmes