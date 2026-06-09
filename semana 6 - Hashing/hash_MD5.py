import hashlib


def ler_ficheiro(nome_ficheiro: str) -> str:

    with open(nome_ficheiro, "r", encoding="utf-8") as f:
        return f.read()


"""
def texto_para_ascii(texto: str) -> list:
    return [ord(c) for c in texto]


def hashingFolding(texto: str, tamanho_hash: int =8) -> list:

    valores_ASCII = texto_para_ascii(texto)

    while len(valores_ASCII) % tamanho_hash != 0:
        valores_ASCII.append(tamanho_hash)

    linhas = []

    for i in range(0, len(valores_ASCII), tamanho_hash):
        linha = valores_ASCII[i:i+tamanho_hash]
        linhas.append(linha)

    soma = [0] * tamanho_hash

    for linha in linhas:
        for i in range(tamanho_hash):
            soma[i] += linha[i]

    valores_hash = [x % 256 for x in soma]

    return valores_hash


def hash_para_hexa(valores_hash: list) -> list:
    resultado = []

    for valor in valores_hash:
        hexa = format(valor, "02X")
        resultado.append(hexa)

    return resultado


def hash_com_chave(valores_hash: list, chave: list) -> list:

    if len(valores_hash) != len(chave):
        raise ValueError("A chave deve ter o mesmo tamanho do hash")

    assinatura = []

    for i in range(len(valores_hash)):
        valor = (valores_hash[i] + chave[i]) % 256
        assinatura.append(valor)

    return assinatura


def verificar_integridade(hash1: list, hash2: list) -> bool:
    return hash1 == hash2


def guardar_assinatura(nome_ficheiro: str, ficheiro_origem: str, assinatura: list):

    with open(nome_ficheiro, "w") as f:
        f.write(ficheiro_origem + " : ")

        for valor in assinatura:
            f.write(str(valor) + " ")
        f.write("\n")
"""


def assinatura_md5(texto: str, chave: str = "") -> str:
    """
    Gera a assinatura MD5 de um texto, opcionalmente combinada com uma chave.

    Args:
        texto: Texto base.
        chave: Chave adicional para reforçar a assinatura.

    Returns:
        Hash MD5 em hexadecimal.
    """

    combinado = texto + chave
    hash_obj = hashlib.md5(combinado.encode())
    return hash_obj.hexdigest()

def guardar_assinatura(nome_ficheiro: str, ficheiro_origem: str, hash_valor: str, assinatura: str):
    """
    Guarda num ficheiro a informação de hash e assinatura MD5.

    Args:
        nome_ficheiro: Ficheiro onde guardar.
        ficheiro_origem: Nome do ficheiro assinado.
        hash_valor: Hash MD5 calculado.
        assinatura: Assinatura MD5 final.
    """

    with open(nome_ficheiro, "a") as f:
        f.write(f"Ficheiro: {ficheiro_origem}\n")
        f.write(f"Hash (MD5): {hash_valor}\n")
        f.write(f"Assinatura (MD5): {assinatura}\n")
        f.write("\n")


def main():

    ficheiro = "txt_hash.txt"

    texto = ler_ficheiro(ficheiro)

    chave = "chave de hash"

    hash_valor = assinatura_md5(texto)
    assinatura = assinatura_md5(texto, chave)

    guardar_assinatura("assinatura.txt", ficheiro, hash_valor, assinatura)

    print("Assinatura (MD5):", assinatura)


main()