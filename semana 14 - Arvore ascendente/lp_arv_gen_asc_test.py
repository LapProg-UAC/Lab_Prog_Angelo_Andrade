from lp_arv_gen_asc import ArvGenAsc
from lp_noo_arv_gen_asc import NooArvGenAsc

def main() -> None:
    raiz_aga = NooArvGenAsc("A")  
    noo_pai = NooArvGenAsc("B")  
    noo_mae = NooArvGenAsc("C")  

    raiz_aga._mae = noo_mae
    raiz_aga._pai = noo_pai
    aga = ArvGenAsc(raiz_aga)  
    print("Pessoa na raiz da árvore",aga._raiz._nome)

    return None

main()
