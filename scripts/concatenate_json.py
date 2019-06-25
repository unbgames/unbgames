# NOME: concatenate_json
# FUNÇÃO: juntar os arquivos json em um unico arquivo json

import glob
import json
import os

from SalvaDicionarioEmJson import SalvaDicionarioEmJson
from PadronizaArrayJogos import PadronizaArrayJogos
from AbrirListaJson import AbrirListaJson

# Lista JSONs dos jogos
lista_jsons = AbrirListaJson.lista_json_jogos()
print(lista_jsons)

# Lê os dados de todos os jogos
lista_jogos = PadronizaArrayJogos.abri_transformar_json_python(lista_jsons)

# Salvando lista em um arquivo json que será o banco de dados
SalvaDicionarioEmJson.salva_arquivo_json(lista_jogos)

