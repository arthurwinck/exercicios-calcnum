import sympy as sy
from xdez import xdez
# Método de Newton
# xk+1 = xk - (f(xk)-f'(xk))
def newtonIter(x0, funcao, func_derivada, precisao):
    iteracoes = 0

    while True:
        resFunc = funcao(x0)
        resDerivada = func_derivada(x0)
        

        xk = x0 - (resFunc/resDerivada)
        funcao_xk = funcao(xk)


        if abs(funcao(xk)) < precisao:
            break
        
        iteracoes += 1
        x0 = xk

    
    print(f"raíz = {xk} / iterações = {iteracoes} / precisão = {funcao(xk)}")

    return xk 


def newton(x0, funcao, func_derivada, precisao, iteracoes):
    xk = x0 - (funcao(x0)/(func_derivada(x0)))
    iteracoes += 1
    print(f"raíz = {xk} / iterações = {iteracoes} / precisão = {funcao(xk)}")


    if abs(funcao(xk)) < precisao:
        print(f"raíz = {xk} / iterações = {iteracoes} / precisão = {funcao(xk)}")
        return xk
    else:
        resFunc = newton(xk, xdez, funcao, precisao, iteracoes)
        
        if resFunc != None:
            return resFunc

    return 

x, y, z = sy.symbols('x y z')
expr = sy.diff(x**10-2, x)
funcao = sy.lambdify(x, expr)
precisao = 10**(-10)
x0 = 1

newtonIter(x0, xdez, funcao, precisao)