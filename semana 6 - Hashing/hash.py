
def ler_ficheiro(nome_ficheiro: str) -> str:
    with open(nome_ficheiro, "r", encoding="utf-8") as f:
        return f.read()

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

def guardar_assinatura(nome_ficheiro: str, ficheiro_origem: str, hash_valor, assinatura):

    with open(nome_ficheiro, "a") as f:

        f.write(f"Ficheiro: {ficheiro_origem}\n")
        f.write(f"Hash (Folding): {hash_valor}\n")
        f.write(f"Assinatura (Folding): {assinatura}\n")
        f.write("\n")


def main():

    ficheiro = "txt_hash.txt"
    texto = ler_ficheiro(ficheiro)

    valores_hash = hashingFolding(texto)

    print("Hash decimal:", valores_hash)

    hash_hex = hash_para_hexa(valores_hash)

    print("Hash hexadecimal:", hash_hex)

    # chave secreta
    chave = [10, 20, 30, 40, 50, 60, 70, 80]

    assinatura = hash_com_chave(valores_hash, chave)

    guardar_assinatura("assinatura.txt", ficheiro, valores_hash, assinatura)

    print("Assinatura (hashing por folding):", assinatura)



main()