import csv
import json
import sqlite3

from config.settings import ARQUIVO_CSV, ARQUIVO_JSON, BANCO


def inicializar_banco():
    BANCO.parent.mkdir(parents=True, exist_ok=True)
    conexao = sqlite3.connect(BANCO)
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS noticias (
            id TEXT PRIMARY KEY,
            portal TEXT,
            titulo TEXT,
            descricao TEXT,
            conteudo TEXT,
            autor TEXT,
            link TEXT,
            data_publicacao TEXT,
            data_coleta TEXT,
            categoria TEXT
        )
    """)
    conexao.commit()
    conexao.close()


def salvar_banco(noticias):
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.cursor()
    novas = 0

    for n in noticias:
        cursor.execute("""
            INSERT OR IGNORE INTO noticias (
                id, portal, titulo, descricao, conteudo, autor, link,
                data_publicacao, data_coleta, categoria
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            n["id"], n["portal"], n["titulo"], n["descricao"], n["conteudo"],
            n["autor"], n["link"], n["data_publicacao"], n["data_coleta"],
            n["categoria"],
        ))
        novas += cursor.rowcount

    conexao.commit()
    conexao.close()
    print(f"\nNovas notícias salvas: {novas}")


def exportar_json():
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row
    cursor = conexao.execute(
        "SELECT * FROM noticias ORDER BY data_publicacao DESC"
    )
    noticias = [dict(row) for row in cursor.fetchall()]

    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=4)

    conexao.close()
    print(f"Arquivo JSON atualizado: {ARQUIVO_JSON}")


def exportar_csv():
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.execute(
        "SELECT * FROM noticias ORDER BY data_publicacao DESC"
    )
    colunas = [d[0] for d in cursor.description]

    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8-sig") as f:
        escritor = csv.writer(f)
        escritor.writerow(colunas)
        escritor.writerows(cursor.fetchall())

    conexao.close()
    print(f"Arquivo CSV atualizado: {ARQUIVO_CSV}")


def consultar_noticias(limite=20):
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.execute("""
        SELECT portal, titulo, categoria, data_publicacao, link
        FROM noticias
        ORDER BY data_publicacao DESC
        LIMIT ?
    """, (limite,))

    print("\n========== ÚLTIMAS NOTÍCIAS ==========\n")
    for portal, titulo, categoria, data, link in cursor:
        print(f"[{portal}]")
        print(f"Título: {titulo}")
        print(f"Categoria: {categoria}")
        print(f"Data: {data}")
        print(f"Link: {link}")
        print("-" * 70)

    conexao.close()
