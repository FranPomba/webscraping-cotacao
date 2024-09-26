Este projeto automatiza a análise de Fundos Imobiliários (FIIs) com base em uma estratégia personalizada de investimento. 
Ele coleta dados do site Fundamentus e aplica critérios específicos para identificar FIIs que atendem aos requisitos da estratégia definida.

O projeto utiliza web scraping para coletar dados de FIIs, como cotações, dividend yield, preço sobre valor patrimonial (P/VP), liquidez, entre outros indicadores relevantes. 
Em seguida, uma estratégia personalizada é aplicada para filtrar os fundos que atendem aos critérios estabelecidos pelo investidor, como:
Cotação mínima
Dividend yield mínimo
P/VP mínimo
Valor de mercado mínimo
Liquidez mínima
Quantidade de imóveis mínima
Vacância média máxima entre outros
Os FIIs que atendem aos critérios são listados em formato tabular.

## Tecnologias Utilizadas

- Python: Linguagem de programação principal.
- Requests: Para fazer requisições HTTP e obter os dados do site.
- BeautifulSoup: Para fazer o parsing do HTML e extrair informações.
- Tabulate: Para exibir os resultados em formato de tabela.

## Autor
Francisco Pomba
