'''
Script: 
    script_parser_json.py

Objetivo: 
    Realizar a pré formatação dos arquivos no formato markdown para um formato
    aceito pela biblioteca que realiza o parser dos arquivospara o formato json.
'''

import os
import glob
import re

'''
Método: geraListaArquivosReadmes
Objetivo: Ler o nome dos arquivos no formato readme e adicioná-los a uma lista
Retorno: Lista contendo todos os nomes dos arquivos readmes
Parâmetros: Não recebe parâmetros
'''
def geraListaArquivosReadmes():
    listaDeNomesArquivosReadmes = []
    for nomeArquivo in glob.glob("readmes/*.md"):
       listaDeNomesArquivosReadmes.append(nomeArquivo)
    return listaDeNomesArquivosReadmes


'''
 Método: geraArquivoJsonFormatado
 Objetivo: Invocar processo externo responsável pelo parser dos arquivos (realizar o parser).
 Retorno: Não há retorno
 Parâmetros: nome dos arquivos temporários pré formatados no formato aceito pela biblioteca m2j.
'''
def geraArquivoJsonFormatado(nomeArquivo):
    os.popen('m2j '+nomeArquivo+' >> '+nomeArquivo.replace('_tmp.md','.json'))



listaDeNomesDeArquivosReadme = geraListaArquivosReadmes()

auxiliaFormatacaoArquivo = ''
encontroUrl = 0

for nomeArquivo in listaDeNomesDeArquivosReadme:
    identificadorJogo = 0
    arquivoReadme = open(nomeArquivo, "r")
    arquivoReadmePreFormatado = nomeArquivo.replace('.md','_tmp.md')
    arquivoParaFormatar = open(arquivoReadmePreFormatado , 'w')
    arquivoParaFormatar.write('---\n')
    for linhaDoArquivo in arquivoReadme:
        auxiliaFormatacaoArquivo = linhaDoArquivo.rstrip()
        auxiliaFormatacaoArquivo = auxiliaFormatacaoArquivo.replace('#', '')
        auxiliaFormatacaoArquivo = auxiliaFormatacaoArquivo.replace('*', '-')
        url = re.findall(r'src=(\S+)><', auxiliaFormatacaoArquivo)
        if url:
            encontroUrl = 1
            for urlNaoFormatada in url:
                #formatacaoUrl = x
                for y in ['(', ')']:
                    formatacaoUrl = urlNaoFormatada.replace(y, "")
            auxiliaFormatacaoArquivo = '   - '+formatacaoUrl[:-1]+'?raw=true"'
        if numeroLinha == 0: #Define o nome e o identificador do jogo
            identificadorJogo = listaDeNomesDeArquivosReadme.index(nomeArquivo)
            arquivoParaFormatar.write(' ID:\n    '+str(identificadorJogo)+'\n' + ' Name:\n    '+auxiliaFormatacaoArquivo+'\n')
        else:
            achoUrlRepositorio = re.findall(r'https://', auxiliaFormatacaoArquivo)
            if not achoUrlRepositorio:
                if (auxiliaFormatacaoArquivo.replace('#','').strip() == "Carousel Gallery:") or (auxiliaFormatacaoArquivo.replace('#','').strip() == "Cover Image:") or (auxiliaFormatacaoArquivo.replace('#','').strip() == "Image Gallery:") or (auxiliaFormatacaoArquivo.replace('#','').strip() == "Debian:") or (auxiliaFormatacaoArquivo.replace('#','').strip() == "RedHat:") or (auxiliaFormatacaoArquivo.replace('#','').strip() == "Windows:") :
                    auxiliaFormatacaoArquivo = auxiliaFormatacaoArquivo.replace(' ','')
                    auxiliaFormatacaoArquivo = '  '+auxiliaFormatacaoArquivo

                if (auxiliaFormatacaoArquivo.replace('#','').strip() != "Description:" and auxiliaFormatacaoArquivo.replace('#','').strip() !="Version:" and auxiliaFormatacaoArquivo.replace('#','').strip() !="Year:" and 
                    auxiliaFormatacaoArquivo.replace('#','').strip() !="Repository:" and auxiliaFormatacaoArquivo.replace('#','').strip() !="Awards:" and auxiliaFormatacaoArquivo.replace('#','').strip() !="Gallery:" and
                    auxiliaFormatacaoArquivo.replace('#','').strip() !="Genre:" and auxiliaFormatacaoArquivo.replace('#','').strip() !="Downloads:" and auxiliaFormatacaoArquivo.replace('#','').strip() !="Development:" and auxiliaFormatacaoArquivo.replace('#','').strip() !="Art:" and 
                    auxiliaFormatacaoArquivo.replace('#','').strip() !="Music:" and auxiliaFormatacaoArquivo.replace('#','').strip() !="CoverImage:") and is_url == 0:
                    auxiliaFormatacaoArquivo = auxiliaFormatacaoArquivo.replace(':',' -')

            arquivoParaFormatar.write(auxiliaFormatacaoArquivo+'\n')
        numeroLinha+=1
    arquivoParaFormatar.write('---')

    arquivo.close()
    arquivoParaFormatar.close()
    encontroUrl = 0
    geraArquivoJsonFormatado(arquivoReadmePreFormatado)
