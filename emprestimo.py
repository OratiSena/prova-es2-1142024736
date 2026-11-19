LIMITE = 9


def pode_emprestar(quantidade):
    if not isinstance(quantidade, int):
        return False
    if quantidade < 1:
        return False
    return quantidade <= LIMITE
