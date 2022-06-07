from xdez import xdez
# Método da Secante
# 
# 
# Pode ser muito dificil obter a derivada explícita de f'(x)
# f'(x) = (f(x + h) - f(x))/h
# --> f'(xk) = (f(xk) - f(xk-1))/(xk-xk-1)
#
# Precisamos agora de dois "chutes" x0 e x1 -> xk-1 = x0 e xk = x1
# xk+1 = xk - f(xk)(xk-xk-1)/(f(xk)-f(xk-1)) -- Reta secante 
#
# f(x1) vai ser o nosso método de parada
from expsen import expsen

def secante(x0, x1, funcao, precisao, iter):
    iter += 1
    
    fx0 = funcao(x0)
    fx1 = funcao(x1)

    #print(x1)
    #print(fx1)

    if abs(fx1) < precisao:
        print(f"raíz = {x1} / iterações = {iter} / precisão = {funcao(x1)}")
        return x1
    else:
        xk = x1 - fx1*(x1-x0)/(fx1-fx0)
        resFunc = secante(x1, xk, funcao, precisao, iter)
        
        if resFunc != None:
            return resFunc

    return None

res = secante(1,2,xdez,10**(-10), 0)