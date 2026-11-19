import time

import feedparser
import requests

from config.settings import FONTES, HEADERS, PAUSA_ENTRE_FONTES, TIMEOUT
from src.parsers.parser import parse_item


def coletar_noticias():
    noticias = []

    for portal, url in FONTES.items():
        print(f"\nConsultando: {portal}")

        try:
            resposta = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            resposta.raise_for_status()

            feed = feedparser.parse(resposta.content)

            if feed.bozo and not feed.entries:
                print("Feed inválido ou indisponível.")
                continue

            for item in feed.entries:
                noticia = parse_item(item, portal)
                if noticia:
                    noticias.append(noticia)

            print(f"Notícias encontradas: {len(feed.entries)}")

        except requests.RequestException as erro:
            print(f"Erro HTTP: {erro}")
        except Exception as erro:
            print(f"Erro na coleta: {erro}")

        time.sleep(PAUSA_ENTRE_FONTES)

    return noticias
