import os
import glob
import re
import json

# Lista JSONs dos jogos
lista_jsons = []
for arquivo_json in glob.glob("readmes/json/*.json"):
	lista_jsons.append(arquivo_json)

# Abre os aquivos json e coloca seus conteudos em uma lista de objetos
games_list = []

for json_file in lista_jsons:
	with open(json_file, 'r') as data:
		game_obj = json.load(data)
		games_list.append(game_obj)

# Salvando lista em um arquivo json
with open('readmes/json/games_db/db.json', 'w') as db:
	json.dump(games_list, db)
	