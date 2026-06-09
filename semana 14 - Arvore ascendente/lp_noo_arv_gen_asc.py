# nó de árvore (binária) genealógica ascendente

class NooArvGenAsc:
    """
    Representa um nó de uma árvore genealógica ascendente.

    Cada nó contém:
    - _nome: nome da pessoa
    - _mae: referência para o nó da mãe (subárvore esquerda)
    - _pai: referência para o nó do pai (subárvore direita)

    """

    def __init__(self, val: str):
        self._nome: str = val
        self._mae = None
        self._pai = None


    def get_nome(self) -> str:
        return self._nome

    def get_mae(self):
        return self._mae

    def get_pai(self):
        return self._pai


    def set_nome(self, novo_nome: str):
        self._nome = novo_nome

    def set_mae(self, mae):
        self._mae = mae

    def set_pai(self, pai):
        self._pai = pai

