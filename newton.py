# Método de Newton
# xk+1 = xk - (f(xk)-f'(xk))

def derivada(funcao):
    #Implementar derivada SymPy
    return funcao

def newton(a, b, x0, funcao, precisao):
    xk = x0 - (funcao(x0)/derivada(funcao(x0)))

    if abs(xk - x0) < precisao:
        return xk
    else:
        resFunc = newton(a, b, xk, funcao, precisao)
        return resFunc
