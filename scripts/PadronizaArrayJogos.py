'''
Classe:
    PadronizaArrayJogos

Objetivo:
    Verifica se o arquivo já está salvo na lista e padroniza todas as chaves no array de jogos
'''

import glob
import json
import os

class PadronizaArrayJogos:

    '''
        Objetivo:Verificar se o arquivo já se encontra na lista salva e padroniza todas as chaves dos arquivos no array de jogos
        Retorno: Lista dos jogos
    '''
    @staticmethod
    def abri_transformar_json_python(lista_jsons):
        lista_jogos = []

        for json_file in lista_jsons:
            with open(json_file, "r") as data:
                # Verifica se o arquivo já está salvo
                while True:
                    tamanho_arquivo = os.path.getsize(json_file)

                    if tamanho_arquivo != 0:
                        break

                objeto_jogo = json.load(data)

                # Padroniza todas as chaves no array de jogos
                key_objeto_jogo = objeto_jogo.keys()
                key_objeto_jogo = list(key_objeto_jogo)[0]
                objeto_jogo["jogo"] = objeto_jogo.pop(key_objeto_jogo)

                lista_jogos.append(objeto_jogo)

        return lista_jogos
