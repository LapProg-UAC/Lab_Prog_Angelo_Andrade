from lp_arv_gen_asc import ArvGenAsc

def main():

    arv = ArvGenAsc()
    arv.carregar_de_ficheiro("nomes_ArvGen.txt")
    print("Raiz:", arv.get_raiz().get_nome())

    print(arv.in_ord_trav())

    nome = "Ana" 
    print(f"Pais de {nome}:", arv.obter_pais(nome))

    print(f"Ascendente materno de grau 1 de {nome}:", arv.ascendente(nome, 1, "m"))
    print(f"Ascendente materno de grau 2 de {nome}:", arv.ascendente(nome, 2, "m"))
    print(f"Ascendente paterno de grau 2 de {nome}:", arv.ascendente(nome, 2, "p"))
    print(f"Ascendente materno de grau 3 de {nome}:", arv.ascendente(nome, 3, "m"))


main()
