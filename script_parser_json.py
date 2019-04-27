import os
import glob
import re

def lista_arquivo():
    lista = []
    for x in glob.glob("readmes/*.md"):
       lista.append(x)
    return lista

def salva_json(nomeArquivo):
    os.popen('m2j '+nomeArquivo+' >> '+nomeArquivo.replace('_tmp.md','.json'))

lista_md = lista_arquivo()

dados = []
aux = ''
is_url = 0

for i in lista_md:
    count = 0
    arquivo = open(i, "r")
    arquivoTmp = i.replace('.md','_tmp.md')
    readme_json = open(arquivoTmp , 'w')
    readme_json.write('---\n')
    for linha in arquivo:
        aux = linha.rstrip()
        aux = aux.replace('#', '')
        aux = aux.replace('*', '-')
        url = re.findall(r'src=(\S+)><', aux)
        if url:
            is_url = 1
            for x in url:
                item = x
                for y in ['(', ')']:
                    item = item.replace(y, "")
            aux = '   - '+item
        if count == 0: #Define Name and ID of the game
            gameId = lista_md.index(i)
            readme_json.write(' ID:\n    '+str(gameId)+'\n' + ' Name:\n    '+aux+'\n')
        else:
            url_rep = re.findall(r'https://', aux)
            if not url_rep:
                if (aux.replace('#','').strip() == "Carousel Gallery:") or (aux.replace('#','').strip() == "Cover Image:") or (aux.replace('#','').strip() == "Image Gallery:"):
                    aux = aux.replace(' ','')
                    aux = '  '+aux

                if (aux.replace('#','').strip() != "Description:" and aux.replace('#','').strip() !="Version:" and aux.replace('#','').strip() !="Year:" and 
                    aux.replace('#','').strip() !="Repository:" and aux.replace('#','').strip() !="Awards:" and aux.replace('#','').strip() !="Gallery:" and
                    aux.replace('#','').strip() !="Genre:" and aux.replace('#','').strip() !="Development:" and aux.replace('#','').strip() !="Art:" and 
                    aux.replace('#','').strip() !="Music:" and aux.replace('#','').strip() !="CoverImage:") and is_url == 0:
                    aux = aux.replace(':',' -')

            readme_json.write(aux+'\n')
        count+=1
    readme_json.write('---')

    arquivo.close()
    readme_json.close()
    is_url = 0
    salva_json(arquivoTmp)
