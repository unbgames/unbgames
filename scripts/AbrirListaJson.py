'''
Classe:
    AbriListaJson

Objetivo:
    Abre os aquivos json e coloca seus conteudos em uma lista de objetos
'''

import glob
import json
import os

class AbrirListaJson:

    '''
        Objetivo: Abre os readmes de todos os repositorios da organização e os coloca em uma lista.
        Retorno: Lista dos jogos
    '''
    @staticmethod
    # Lista JSONs dos jogos
    def lista_json_jogos():
    	lista_jsons = []
    	for arquivo_json in glob.glob("readmes/*.json"):
    		lista_jsons.append(arquivo_json)

    	# Abre os aquivos json e coloca seus conteudos em uma lista de objetos
    	lista_jogos = []
    	return lista_jsons
