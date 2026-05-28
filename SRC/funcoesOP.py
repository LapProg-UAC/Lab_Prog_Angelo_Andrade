def procurar_utente(prescricoes, condicao):
    """
    Função de ordem superior: recebe um predicado (condição)
    e devolve o primeiro utente que o satisfaz.
    """
    return next((p for p in prescricoes if condicao(p)), None)

def filtrar_receitas(prescricoes, condicao):
    """
    Função de ordem superior: recebe um predicado e devolve
    todas as receitas que satisfazem essa condição.
    """
    return [p for p in prescricoes if condicao(p)]


def filtrar_utentes(prescricoes, condicao):
    """
    Função de ordem superior: recebe um predicado e devolve
    todos os utentes que satisfazem essa condição.
    """
    return [p for p in prescricoes if condicao(p)]



def por_numero(numero):
    return lambda p: p["numero"] == numero


def id_entre(x, y):
    return lambda p: x <= p["numero"] <= y


def receitas_por_numero(numero):
    return lambda p: p["numero"] == numero






