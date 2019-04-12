import os

arquivo = open("README.md", "r")
n_linhas = sum(1 for linha in arquivo)
arquivo.close()

arquivo = open("README.md", "r")

readme_json = open('README_aux.md', 'a')

dados = []
aux = ''
count = 0
readme_json.write('---\n')
for linha in arquivo:
    aux = linha.replace('\n', '')
    aux = aux.replace('#', '')
    if count == 0:
        readme_json.write(aux+':\n')
    else:
        readme_json.write(aux+'\n')
    count+=1

readme_json.write('---')

arquivo.close()
readme_json.close()

os.popen('m2j README_aux.md >> README.json')


