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
    def salva_arquivo_json(lista_jogos):
        dicionario_jogos = {"jogos" : lista_jogos}
    	
        with open('../utils/db.json', 'w') as database:
            json.dump(dicionario_jogos, database, indent=4)
        database.close()