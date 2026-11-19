from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DIR = BASE_DIR / "data" / "processed"

BANCO = PROCESSED_DIR / "noticias_economia.db"
ARQUIVO_JSON = PROCESSED_DIR / "noticias.json"
ARQUIVO_CSV = PROCESSED_DIR / "noticias.csv"

HEADERS = {"User-Agent": "PersonalEconomyNewsAggregator/1.0"}
TIMEOUT = 20
PAUSA_ENTRE_FONTES = 1

FONTES = {
    "InfoMoney": "https://www.infomoney.com.br/feed/",
    "Valor Econômico": "https://valor.globo.com/rss/valor",
    "G1 Economia": "https://g1.globo.com/dynamo/economia/rss2.xml",
    "Exame": "https://exame.com/feed/",
    "Money Times": "https://www.moneytimes.com.br/feed/",
}

PALAVRAS_CHAVE = [
    "economia", "inflação", "ipca", "igpm",
    "selic", "juros", "copom", "pib",
    "dólar", "câmbio", "bolsa", "ibovespa",
    "ações", "investimentos", "mercado financeiro",
    "banco central", "federal reserve", "fed",
    "empresas", "fiscal", "tributária",
    "desemprego", "emprego", "exportações",
    "importações", "commodities", "petróleo",
    "tesouro direto", "renda fixa", "fundos imobiliários",
]

CATEGORIAS = {
    "Inflação e indicadores": ["inflação", "ipca", "igpm", "pib", "ibge"],
    "Política monetária": ["selic", "juros", "copom", "banco central"],
    "Mercado financeiro": [
        "ibovespa", "ações", "bolsa", "dólar", "câmbio", "investimentos",
    ],
    "Empresas e negócios": [
        "empresa", "negócios", "fusão", "aquisição", "lucro", "prejuízo",
    ],
    "Economia internacional": [
        "federal reserve", "fed", "eua", "china", "europa", "petróleo",
    ],
    "Economia geral": ["economia", "desemprego", "emprego", "fiscal", "tributária"],
}
