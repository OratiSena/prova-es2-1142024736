
from emprestimo import pode_emprestar, LIMITE


def test_limite_exato_e_aceito():
    resultado = pode_emprestar(LIMITE)
    assert resultado is True


def test_acima_do_limite_e_rejeitado():
    resultado = pode_emprestar(LIMITE + 1)
    assert resultado is False


def test_quantidade_zero_e_rejeitada():
    resultado = pode_emprestar(0)
    assert resultado is False


def test_quantidade_decimal_e_rejeitada():
    quantidade = LIMITE - 0.5
    resultado = pode_emprestar(quantidade)
    assert resultado is False
