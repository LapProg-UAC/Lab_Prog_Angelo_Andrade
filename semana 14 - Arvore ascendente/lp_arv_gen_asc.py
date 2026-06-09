from lp_noo_arv_gen_asc import NooArvGenAsc

class ArvGenAsc:
    """
    Representa uma árvore genealógica ascendente (binária).
    A raiz é a pessoa cuja ascendência queremos representar.
    """

    def __init__(self, noo: NooArvGenAsc = None):
        self._raiz = noo
        self._nos = {}

    def get_raiz(self) -> NooArvGenAsc:
        return self._raiz

    def set_raiz(self, nova_raiz: NooArvGenAsc):
        self._raiz = nova_raiz


    def in_ord_trav(self) -> list:
        """
        Travessia em-ordem da árvore genealógica:
        1. pai
        2. pessoa
        3. mãe

        :return: lista dos nomes pela ordem visitada
        """

        def em_ordem(no: NooArvGenAsc):
            if no is None:
                return []

            esquerda = em_ordem(no.get_pai())
            centro = [no.get_nome()]
            direita = em_ordem(no.get_mae())

            return esquerda + centro + direita

        return em_ordem(self._raiz)
    
    
    def carregar_de_ficheiro(self, caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            for linha in f:
                pessoa, mae, pai = [x.strip() for x in linha.split(",")]

                if pessoa not in self._nos:
                    self._nos[pessoa] = NooArvGenAsc(pessoa)

                if (mae and not pai) or (pai and not mae):
                    raise ValueError(f"Nó inválido: {pessoa} tem apenas um progenitor.")


                if mae:
                    if mae not in self._nos:
                        self._nos[mae] = NooArvGenAsc(mae)
                    self._nos[pessoa].set_mae(self._nos[mae])


                if pai:
                    if pai not in self._nos:
                        self._nos[pai] = NooArvGenAsc(pai)
                    self._nos[pessoa].set_pai(self._nos[pai])


        candidatos = set(self._nos.keys())

        for no in self._nos.values():
            if no.get_mae():
                candidatos.discard(no.get_mae().get_nome())
            if no.get_pai():
                candidatos.discard(no.get_pai().get_nome())

        if len(candidatos) != 1:
            raise ValueError("Árvore inválida: não existe uma única raiz.")

        self._raiz = self._nos[candidatos.pop()]


    def obter_pais(self, nome: str, no=None):
        """
        Procura recursivamente a pessoa na árvore e devolve (mae, pai).
        """

        if no is None:
            no = self._raiz

        if no is None:
            return None

        if no.get_nome() == nome:
            mae = no.get_mae().get_nome() if no.get_mae() else None
            pai = no.get_pai().get_nome() if no.get_pai() else None
            return (mae, pai)


        res = self.obter_pais(nome, no.get_pai())
        if res is not None:
            return res

        return self.obter_pais(nome, no.get_mae())
    

    def ascendente(self, nome: str, grau: int, lado: str, no=None, nivel_atual=0):
        """
        Devolve o ascendente da pessoa até ao grau indicado (1 a 4),
        seguindo o lado m (materno) ou p (paterno).
        """

        if no is None:
            if nivel_atual > 0:
                return None
            no = self._raiz


        if no is None:
            return None

        if no.get_nome() == nome:

            if grau == 1:
                if lado == "m":
                    return no.get_mae().get_nome() if no.get_mae() else None
                else:
                    return no.get_pai().get_nome() if no.get_pai() else None

            if lado == "m":
                if not no.get_mae():     
                    return None
                return self.ascendente( no.get_mae().get_nome(), grau - 1, lado, self._raiz, 0)
            else:
                if not no.get_pai():    
                    return None
                return self.ascendente( no.get_pai().get_nome(), grau - 1, lado, self._raiz, 0)


        res = self.ascendente(nome, grau, lado, no.get_pai(), nivel_atual + 1)
        if res is not None:
            return res

        return self.ascendente(nome, grau, lado, no.get_mae(), nivel_atual + 1)


