# NOME: concatenate_json
# FUNÇÃO: Concatenar os arquivos json com os dados dos jogos em um único arquivo json que será o banco de dados da aplicação

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
SalvaDicionarioEmJson.salva_arquivo_json(lista_jogos, 4)

