import glob
import json
import os

# Lista JSONs dos jogos
def lista_json_jogos():
	lista_jsons = []
	for arquivo_json in glob.glob("readmes/*.json"):
		lista_jsons.append(arquivo_json)

	# Abre os aquivos json e coloca seus conteudos em uma lista de objetos
	lista_jogos = []
	return lista_jsons

def abri_transformar_json_python(lista_jsons):
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
# Salvando lista em um arquivo json que será o banco de dados
lista_jsons = lista_json_jogos()
lista_jogos = abri_transformar_json_python(lista_jsons)
database_jogos = {"jogos" : lista_jogos}

with open('utils/db.json', 'w') as database:
	json.dump(database_jogos, database, indent=4)
database.close()
