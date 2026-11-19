import hashlib
import re
from datetime import timezone
from email.utils import parsedate_to_datetime

from bs4 import BeautifulSoup


def limpar_html(texto):
    if not texto:
        return ""
    soup = BeautifulSoup(texto, "html.parser")
    return re.sub(r"\s+", " ", soup.get_text(" ", strip=True)).strip()


def gerar_id(link):
    return hashlib.sha256(link.encode("utf-8")).hexdigest()


def normalizar_data(data):
    if not data:
        return None
    try:
        dt = parsedate_to_datetime(data)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc).isoformat()
    except Exception:
        return None
