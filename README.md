[![author](https://badgen.net/badge/Author/otavio-s-s/blue)](https://www.linkedin.com/in/otavioss28/) [![python](https://badgen.net/badge/Python/3+/yellow)](https://www.python.org) [![license](https://img.shields.io/badge/License-MIT-red)](https://github.com/otavio-s-s/data_science/blob/master/LICENSE) [![contributions](https://badgen.net/badge/Contributions/Welcome/green)](https://github.com/otavio-s-s/lerMicrodados/issues) 


# lerMicrodados
 
Pacote desenvolvido para extração e leitura de microdados do IBGE utilizando Python.

## Funções:
 
 * ler_POF(path, header=True):
    
    Realiza a leitura dos microdados da POF 2017/2018 diretamente do arquivo .zip baixado do site do IBGE
    e exporta os dados como um arquivo .csv.
    * path: caminho para o arquivo .zip
    * param header: boolean, Default True - acrescenta o código da variável como nome de cada coluna.
    
 * ler_PNAD(path, ano, header=True):
    
    Realiza a leitura dos microdados da PNAD 2013, 2014 ou 2015 diretamente do arquivo .zip baixado do site do IBGE
    e exporta os dados como um arquivo .csv.
    * param path: aminho para o arquivo .zip
    * param ano: ano da PNAD.
    * param header:  boolean, Default True - acrescenta o código da variável como nome de cada coluna.

 * ler_PNS(path, header=True):
    
    Realiza a leitura dos microdados da PNS 2013 diretamente do arquivo .zip baixado do site do IBGE
    e exporta os dados como um arquivo .csv.
    * path: caminho para o arquivo .zip
    * param header: boolean, Default True - acrescenta o código da variável como nome de cada coluna.
