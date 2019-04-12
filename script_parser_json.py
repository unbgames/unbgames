import os
import glob

def lista_arquivo():
    lista = []
    for x in glob.glob("readmes/*.md"):
       lista.append(x)
    return lista

def salva_json(nomeArquivo):
    os.popen('m2j '+nomeArquivo+' >> '+ nomeArquivo.replace('_tmp.md','.json'))


lista_md = lista_arquivo()

dados = []
aux = ''

for i in lista_md:
    count = 0
    arquivo = open(i, "r")
    arquivoTmp = i.replace('.md','_tmp.md')
    readme_json = open(arquivoTmp , 'w')
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

    salva_json(arquivoTmp)