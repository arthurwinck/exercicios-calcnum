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

def secante(a, b, x0, x1, funcao, precisao):
    fx0 = funcao(x0)
    fx1 = funcao(x1)

    print(x1)
    print(fx1)

    if abs(fx1) < precisao:
        return x1
    else:
        xk = x1 - fx1*(x1-x0)/(fx1-fx0)
        resFunc = secante(a,b, x1, xk, funcao, precisao)
        
        if resFunc != None:
            return resFunc

    return None

res = secante(0,1,1,2,expsen,10**(-8))