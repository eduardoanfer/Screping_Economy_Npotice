from datetime import datetime, timezone

from config.settings import CATEGORIAS, PALAVRAS_CHAVE
from src.utils.helpers import gerar_id, limpar_html, normalizar_data


def identificar_categoria(texto):
    texto = texto.lower()
    for categoria, palavras in CATEGORIAS.items():
        if any(p in texto for p in palavras):
            return categoria
    return "Outros"


def noticia_relevante(texto):
    texto = texto.lower()
    return any(p in texto for p in PALAVRAS_CHAVE)


def parse_item(item, portal):
    """Converte uma entrada do feed em dict de notícia. Retorna None se descartada."""
    titulo = limpar_html(item.get("title", ""))
    descricao = limpar_html(item.get("summary", ""))
    link = item.get("link", "")

    if not titulo or not link:
        return None

    conteudo = ""
    if item.get("content"):
        conteudo = limpar_html(item["content"][0].get("value", ""))

    texto_completo = f"{titulo} {descricao} {conteudo}"
    if not noticia_relevante(texto_completo):
        return None

    return {
        "id": gerar_id(link),
        "portal": portal,
        "titulo": titulo,
        "descricao": descricao,
        "conteudo": conteudo,
        "autor": item.get("author", ""),
        "link": link,
        "data_publicacao": normalizar_data(
            item.get("published") or item.get("updated")
        ),
        "data_coleta": datetime.now(timezone.utc).isoformat(),
        "categoria": identificar_categoria(texto_completo),
    }
