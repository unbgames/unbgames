# NOME: script_get_readme
# FUNÇÃO: Acessar cada repositório na organização para capturar o arquivo 'unbgames.md' 
#         com as informações referentes a cada jogo,

from github import Github
import urllib
import os

# --- Variável de ambiente configurada no travis para autenticação da API Github
token = os.environ['AUTH_TOKEN']

objeto_github = Github(token)
organizacao = objeto_github.get_organization('plataformagames')

for repositorio in organizacao.get_repos():
    try:
        conteudo_arquivo = repositorio.get_file_contents('unbgames.md')

        if(repositorio.name != 'unbgames' or repositorio.name != 'game-template' or repositorio.name != 'unbgames-platform'):
            urllib.request.urlretrieve(conteudo_arquivo.download_url, ('readmes/'+repositorio.name + '.md'))

    except Exception as excecao_encontrada :
        print("O repositório: " + repositorio.name + " não possui o arquivo 'unbgames.md'.")
        print(str(excecao_encontrada))
