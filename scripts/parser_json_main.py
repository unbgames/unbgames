from ArquivoReadme import ArquivoReadme
from PreFormataReadme import PreFormataReadme
from ArquivoJson import ArquivoJson


listaArquivosReadme = ArquivoReadme.geraListaArquivosReadme()

listaArquivosPreFormatado = PreFormataReadme.formataReadme(listaArquivosReadme)

for arquivoPreFormatado in listaArquivosPreFormatado:
    ArquivoJson.geraArquivoJsonFormatado(arquivoPreFormatado)
