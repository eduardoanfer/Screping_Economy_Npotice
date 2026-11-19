"""
Agregador de notícias econômicas (InfoMoney, Valor, G1, Exame, Money Times).

Execute a partir da raiz do projeto:  python -m src.main
"""

from src.scraper.client import coletar_noticias
from src.storage.save import (
    consultar_noticias,
    exportar_csv,
    exportar_json,
    inicializar_banco,
    salvar_banco,
)


def executar():
    inicializar_banco()

    print("Iniciando agregador de notícias econômicas...")

    noticias = coletar_noticias()
    salvar_banco(noticias)
    exportar_json()
    exportar_csv()
    consultar_noticias()

    print("\nColeta finalizada!")


if __name__ == "__main__":
    executar()
