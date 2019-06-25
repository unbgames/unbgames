'''
Classe:
    SalvaDicionarioEmJson

Objetivo:
    Salva dicionário com objetos dos jogos em um arquivo json para ser usado como banco de dados da plataforma 
'''

import glob
import json
import os

class SalvaDicionarioEmJson:

    '''
        Objetivo: Salva dicionário em JSON no formato do banco de dados
    '''
    @staticmethod
    # Lista JSONs dos jogos
    def salva_arquivo_json(lista_jogos, tamanho_indentacao):
        arquivo_banco_dados = '../utils/db.json'
        dicionario_jogos = {"jogos" : lista_jogos}
    	
        with open(arquivo_banco_dados, 'w') as database:
            json.dump(dicionario_jogos, database, indent=tamanho_indentacao)
        database.close()