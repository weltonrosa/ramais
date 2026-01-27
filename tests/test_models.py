import sys
sys.path.append(".")
from src.models import pessoa

def test_concatenacao_nome_completo():
    p = pessoa.Pessoa("Ana", "Silva", 28, "12345678900")
    assert p.nome_completo() == "Ana Silva"