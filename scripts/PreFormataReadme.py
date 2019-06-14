'''
Classe: 
    PreFormataReadme

Objetivo: 
    Realizar a pré formatação dos arquivos no formato markdown para um formato
    aceito pela biblioteca que realiza o parser dos arquivos para o formato json.
'''

import re

class PreFormataReadme:

    '''
        Método: formataReadme
        Objetivo: Realiza a pre formatação dos arquivos markdown para um formato aceito pela biblioteca de
        conversão para json.
        Retorno: Lista contendo os arquivos readmes pré formatados
        Parâmetros: Lista com os nomes dos arquivos q serem formatados
    '''
    @staticmethod
    def formataReadme(listaDeNomesArquivos):
        listaPreFormatados = []
        listaDeNomesDeArquivosReadme = listaDeNomesArquivos
        auxiliaFormatacaoArquivo = ''
        encontroUrl = 0
        for nomeArquivo in listaDeNomesDeArquivosReadme:
            numeroLinha = 0
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
                        for y in ['(', ')']:
                            formatacaoUrl = urlNaoFormatada.replace(y, "")
                    auxiliaFormatacaoArquivo = '   - '+formatacaoUrl[:-1]+'?raw=true"'
                if numeroLinha == 0:
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
                            auxiliaFormatacaoArquivo.replace('#','').strip() !="Music:" and auxiliaFormatacaoArquivo.replace('#','').strip() !="CoverImage:") and encontroUrl == 0:
                            auxiliaFormatacaoArquivo = auxiliaFormatacaoArquivo.replace(':',' -')

                    arquivoParaFormatar.write(auxiliaFormatacaoArquivo+'\n')
                numeroLinha+=1
            arquivoParaFormatar.write('---')

            arquivoReadme.close()
            arquivoParaFormatar.close()
            encontroUrl = 0
            listaPreFormatados.append(arquivoReadmePreFormatado)
        return listaPreFormatados
