class FundoImobiliario:

    def __init__(self, codigo, segmento, cotacao, ff_yield, dv_yield, p_vp,
                 valor_mercado, liquidez, qt_imoveis, preco_m2, aluguel_m2,
                 cap_rate, vacancia_media):
        self.codigo = codigo
        self.segmento = segmento
        self.cotacao = cotacao
        self.ff_yield = ff_yield
        self.dv_yield = dv_yield
        self.p_vp = p_vp
        self.valor_mercado = valor_mercado
        self.liquidez = liquidez
        self.qt_imoveis = qt_imoveis
        self.preco_m2 = preco_m2
        self.aluguel_m2 = aluguel_m2
        self.cap_rate = cap_rate
        self.vacancia_media = vacancia_media


class EstrategiaInventimento:

    def __init__(self,segmento="", cotacao_min=0, ff_yield_min=0, dv_yield_min=0, p_vp_min=0,
                 valor_mercado_min=0, liquidez_min=0, qt_imoveis_min=0, preco_m2_min=0, aluguel_m2_min=0,
                 cap_rate_min=0, maxima_vacancia_media=0):
        self.segmento = segmento
        self.cotacao_min = cotacao_min
        self.ff_yield_min = ff_yield_min
        self.dv_yield_min = dv_yield_min
        self.p_vp_min = p_vp_min
        self.valor_mercado_min = valor_mercado_min
        self.liquidez_min = liquidez_min
        self.qt_imoveis_min = qt_imoveis_min
        self.preco_m2_min = preco_m2_min
        self.aluguel_m2_min = aluguel_m2_min
        self.cap_rate_min = cap_rate_min
        self.maxima_vacancia_media = maxima_vacancia_media

    def aplica_estrategia(self, fundo: FundoImobiliario):

        if self.segmento != "":
            if fundo.segmento != self.segmento:
                return False

        if fundo.cotacao < self.cotacao_min \
                or fundo.ff_yield < self.ff_yield_min or fundo.dv_yield < self.dv_yield_min \
                or fundo.p_vp < self.p_vp_min or fundo.valor_mercado < self.valor_mercado_min \
                or fundo.liquidez < self.liquidez_min or fundo.qt_imoveis < self.qt_imoveis_min \
                or fundo.preco_m2 < self.preco_m2_min or fundo.aluguel_m2 < self.aluguel_m2_min \
                or fundo.cap_rate < self.cap_rate_min or fundo.vacancia_media > self.maxima_vacancia_media:
            return False
        return True



