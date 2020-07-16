'''
Script:
    script_get_readme

Objetivo:
    Acessar cada repositório na organização para capturar o arquivo 'unbgames.md' 
    com as informações referentes a cada jogo,
'''
from github import Github
import urllib
import os

'''
    Variável de ambiente configurada no travis para autenticação da API Github
'''
token = os.environ['AUTH_TOKEN']

objetoGithub = Github(token)
organizacao = objetoGithub.get_organization('plataformagames')

for repositorio in organizacao.get_repos():
    try:
        conteudoArquivo = repositorio.get_file_contents('unbgames.md')

        if(repositorio.name != 'unbgames' or repositorio.name != 'game-template' or repositorio.name != 'unbgames-platform'):
            urllib.request.urlretrieve(conteudoArquivo.download_url, ('readmes/'+repositorio.name + '.md'))

    except Exception as excecaoEncontrada :
        print("O repositório: " + repositorio.name + " não possui o arquivo 'unbgames.md'.")
        print(str(excecaoEncontrada))
