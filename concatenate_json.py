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

		# Padroniza todas as chaves no array de jogos
		key_game_obj = game_obj.keys()
		key_game_obj = list(key_game_obj)[0]
		game_obj["jogo"] = game_obj.pop(key_game_obj)

		games_list.append(game_obj)

# Salvando lista em um arquivo json que será o banco de dados
with open('utils/db.json', 'w') as db:
	json.dump(games_list, db, indent=4)
db.close()
