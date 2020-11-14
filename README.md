[![author](https://badgen.net/badge/Author/otavio-s-s/blue)](https://www.linkedin.com/in/otavioss28/) [![python](https://badgen.net/badge/Python/3+/yellow)](https://www.python.org) [![license](https://img.shields.io/badge/License-MIT-red)](https://github.com/otavio-s-s/data_science/blob/master/LICENSE) [![contributions](https://badgen.net/badge/Contributions/Welcome/green)](https://github.com/otavio-s-s/lerMicrodados/issues) 


# lerMicrodados
 
Pacote desenvolvido para extração e leitura de microdados do IBGE utilizando Python.

## Funções:
 
 * ler_POF(path, header=True):
    
    Realiza a leitura dos microdados da POF 2017/2018 diretamente do arquivo .zip baixado do site do IBGE
    e exporta os dados como um arquivo .csv.
    * path: caminho para o arquivo .zip
    * header: boolean, Default True - acrescenta o código da variável como nome de cada coluna.
    * format: formato do arquivo gerado. *.csv* a *.xlsx* disponíveis.
    
    Atualizada em 23/10/2020.
    
 * ler_PNAD(path, ano, header=True):
    
    Realiza a leitura dos microdados da PNAD 2013, 2014 ou 2015 diretamente do arquivo .zip baixado do site do IBGE
    e exporta os dados como um arquivo .csv.
    * path: caminho para o arquivo .zip
    * ano: ano da PNAD.
    * header:  boolean, Default True - acrescenta o código da variável como nome de cada coluna.

 * ler_PNS(path, header=True):
    
    Realiza a leitura dos microdados da PNS 2013 diretamente do arquivo .zip baixado do site do IBGE e exporta os dados como um arquivo .csv. *Função  sugerida por [Bruna Schultz](https://www.linkedin.com/in/brunanschultz/).*
    * path: caminho para o arquivo .zip
    * header: boolean, Default True - acrescenta o código da variável como nome de cada coluna.  
 
 * ler_PNADcontinua(anos: list):
 
    Faz a leitura de arquivos da PNAD Contínua trimestral, diretamente do site do IBGE. Retorna um dataframe com os dados agrupados para todos os anos informados.
    
    * anos: Lista com os anos desejados da pesquisa.
  
    Exemplo:
    
    > pnad = ler_PNADcontinua(anos=['2017','2018'])
  

## Funcionamento

![](https://miro.medium.com/max/700/1*31vC5t30avsM-vQEiwhi3g.png)

***

Leia mais sobre o pacote [neste artigo](https://medium.com/data-hackers/microdados-em-python-um-pacote-para-ler-dados-da-pnad-e-pof-e254cf18477d).
