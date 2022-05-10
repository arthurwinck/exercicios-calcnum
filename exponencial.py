def diferencaErro(atual, antigo, erro):
    return abs(atual - antigo) < erro

def exponencial(x, erro):

    i = 1
    res = 1
    resAntigo = 0
    fib = 1

    while not diferencaErro(res, resAntigo, erro):
        resAntigo = res
        i += 1
        fib = fib*(i-1)
        res += x**(i-1)/fib

    return res