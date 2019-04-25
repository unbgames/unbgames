import glob
import json
import os

# Lista JSONs dos jogos
lista_jsons = []
for arquivo_json in glob.glob("readmes/*.json"):
	lista_jsons.append(arquivo_json)

# Abre os aquivos json e coloca seus conteudos em uma lista de objetos
games_list = []

for json_file in lista_jsons:
	with open(json_file, "r") as data:
		# Verifica se o arquivo já está salvo
		while True:
			file_size = os.path.getsize(json_file)

			if file_size != 0:
				break

		game_obj = json.load(data)
		games_list.append(game_obj)

# Salvando lista em um arquivo json que será o banco de dados
with open('utils/db.json', 'w') as db:
	json.dump(games_list, db, indent=4)
db.close()
