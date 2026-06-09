
def transformar_string(texto: str, chaves: list[int], modo: int, campo: int | list[int] |
                        None = None, delimitador: str = ",") -> str:
    """
    Aplica encriptação/desencriptação a uma string usando chaves cíclicas.
    Pode atuar no texto inteiro ou apenas em campos separados por delimitador.

    Args:
        texto: Texto a transformar.
        chaves: Lista de chaves inteiras.
        modo: +1 encripta, -1 desencripta.
        campo: Índice(s) dos campos a alterar ou None para texto completo.
        delimitador: Separador dos campos.

    Returns:
        String transformada.
    """

    if campo is None:
        transformado = ""                                            
        i = 0
        for c in texto:                                                     
            if c == " ":                                                  
                transformado += c
            else:
                chave = chaves[i % len(chaves)]                           
                novo = chr(ord(c) + modo * chave)                           
                transformado += novo                                       
                i += 1

        return transformado

    else:
        campos = texto.split(delimitador)
        if isinstance(campo, int):                                          
            campo = [campo]
        for c in campo:                                                     
            if c < len(campos):
                campos[c] = transformar_string(campos[c], chaves, modo)     

        return delimitador.join(campos)



def transformar_ficheiro(entrada: str, saida: str, chaves: list[int], modo: int, campo: int | list[int] | 
                         None = None, delimitador: str = ",") -> None:
    """
    Lê um ficheiro linha a linha, aplica a transformação e escreve o resultado
    num novo ficheiro.

    Args:
        entrada: Caminho do ficheiro de origem.
        saida: Caminho do ficheiro de destino.
        chaves: Lista de chaves inteiras.
        modo: +1 encripta, -1 desencripta.
        campo: Campo(s) a transformar ou None.
        delimitador: Separador dos campos.
    """

    with open(entrada, "r", encoding="utf-8") as f_in, open(saida, "w", encoding="utf-8") as f_out:

        for linha in f_in:                                                              
            linha = linha.rstrip("\n")                                                  
            nova_linha = transformar_string(linha, chaves, modo, campo, delimitador)    
            f_out.write(nova_linha + "\n")                                              


def main():
    texto = "Teste encriptação. Fingers crossed, esperemos que dê certo."
    texto_campo = "Teste,encriptação,Fingers,crossed"
    chaves = [3, 5, 7]
    campo = [0, 1, 2, 3]

    print("Texto original:", texto)
    print("Texto por campos original:", texto_campo)

    encriptado = transformar_string(texto, chaves, 1)
    print("Texto encriptado:", encriptado)

    desencriptado = transformar_string(encriptado, chaves, -1)
    print("Texto desencriptado:", desencriptado)

    #encriptado_campo = transformar_string(texto_campo, chaves, 1, campo)
    #print("Texto com campos encriptados:", encriptado_campo)

    #desencriptado_campo = transformar_string(encriptado_campo, chaves, -1, campo)
    #print("Texto com campos desencriptados:", desencriptado_campo)

    transformar_ficheiro("texto.txt", "texto_encriptado.txt", chaves, 1)
    transformar_ficheiro("texto_encriptado.txt", "texto_desencriptado.txt", chaves, -1)

    #transformar_ficheiro("texto_campos.txt", "texto_campos_encriptado.txt", chaves, 1, campo)
    #transformar_ficheiro("texto_campos_encriptado.txt", "texto_campos_desencriptado.txt", chaves, -1, campo)



main()