
LIMITE = 9


def pode_emprestar(quantidade):
    if quantidade < 1:
        return False
    return quantidade < LIMITE
