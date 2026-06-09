def gerar_f(n: int) -> list:
    
    """
    f(0)=0, f(1)=1
    f(i)=3*f(i-2)+f(i-1)

    >>> gerar_f(5)
    [0, 1, 1, 4, 7]

    >>> gerar_f(0)
    [0]

    >>> gerar_f(-1)
    Traceback (most recent call last):
    ...
    ValueError: n deve ser inteiro nao negativo
    """

    if not isinstance(n, int) or n < 0:
        raise ValueError("n deve ser inteiro nao negativo")

    if n == 0:
        return [0]

    f = [0, 1]

    for i in range(2, n):
        f.append(3 * f[i-2] + f[i-1])

    return f[:n]