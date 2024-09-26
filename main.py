import requests
from bs4 import BeautifulSoup
from  tabulate import tabulate
import locale
from utilitarios import FundoImobiliario, EstrategiaInventimento

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
headers = {"User-Agent": "Mozilla/5.0"}


def conversao_porcentagem(porc_str):
    return locale.atof(porc_str.split("%")[0])


def conversao_decimal(dec_str):
    return  locale.atof(dec_str)


response = requests.get("https://fundamentus.com.br/fii_resultado.php", headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

lines = soup.find(id="tabelaResultado").find("tbody").find_all("tr")

estrategia = EstrategiaInventimento(cotacao_min=50.0, dv_yield_min=5, p_vp_min=0.50,
                                    valor_mercado_min=20000000, liquidez_min=50000,
                                    qt_imoveis_min=5, maxima_vacancia_media=10)

result = []
for line in lines:
    data = line.find_all("td")
    codigo = data[0].text
    segmento = data[1].text
    cotacao =  conversao_decimal(data[2].text)
    ff_yield = conversao_porcentagem(data[3].text)
    dv_yield = conversao_porcentagem(data[4].text)
    p_vp = conversao_decimal(data[5].text)
    valor_mercado = conversao_decimal(data[6].text)
    liquidez = conversao_decimal(data[7].text)
    qt_imoveis = int(data[8].text)
    preco_m2 = conversao_decimal(data[9].text)
    aluguel_m2 = conversao_decimal(data[10].text)
    cap_rate = conversao_porcentagem(data[11].text)
    vacancia_media = conversao_porcentagem(data[12].text)

    fundo_imob = FundoImobiliario(codigo, segmento, cotacao, ff_yield, dv_yield, p_vp,
                 valor_mercado, liquidez, qt_imoveis, preco_m2, aluguel_m2,
                 cap_rate, vacancia_media)

    if estrategia.aplica_estrategia(fundo_imob):
        result.append(fundo_imob)

header = ["Codigo", "Segmento", "Cotacao", "Dividend Yield", "Valor de Mercado"]

table = []
for item in result:
    table.append([item.codigo, item.segmento, locale.currency(item.cotacao), f"{locale.str(item.dv_yield)} %", locale.currency(item.valor_mercado)])

print(tabulate(table, headers=header, showindex="always", tablefmt="fancy_grid"))
