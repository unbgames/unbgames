'''
Classe: 
    ArquivoJson

Objetivo: 
    Gerenciar o processo de conversão de arquivos do formato markdown para
    json.
'''

import os

class ArquivoJson:

    '''
        Método: geraArquivoJsonFormatado
        Objetivo: Invocar processo externo responsável pelo parser dos arquivos (realizar o parser).
        Retorno: Não há retorno
        Parâmetros: nome dos arquivos temporários pré formatados no formato aceito pela biblioteca m2j.
    '''
    @staticmethod
    def geraArquivoJsonFormatado(nomeArquivo):
        os.popen('m2j '+nomeArquivo+' >> '+nomeArquivo.replace('_tmp.md','.json'))