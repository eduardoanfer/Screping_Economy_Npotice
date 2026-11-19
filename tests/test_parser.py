from src.parsers.parser import identificar_categoria, noticia_relevante


def test_categoria():
    assert identificar_categoria("Copom mantém Selic") == "Política monetária"
    assert identificar_categoria("receita de bolo") == "Outros"


def test_relevante():
    assert noticia_relevante("IPCA sobe em outubro")
    assert not noticia_relevante("Final do campeonato")
