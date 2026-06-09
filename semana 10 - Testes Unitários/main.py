from funcao_doctest import gerar_f

def main():
    n = int(input("Inteiro (>=0) -> "))

    while n >= -1:
        try:
            print("Resultado:", gerar_f(n))
        except ValueError as e:
            print(e)

        n = int(input("Inteiro (>=0) -> "))

    print("Fim")


if __name__ == "__main__":
    main()