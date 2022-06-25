import sympy as sy
import numpy as np
from gauss_sem_troca import gauss_sem_troca as gst

# Retorna a função derivada em relação ao símbolo (x1, x2) como x e y
def derivar(func, sym):
    return sy.lambdify(sym, sy.diff(func, sym))
    
# Cria as variáveis para serem usadas no sympy (Pra ser possível realizar a derivação)
def criar_vars(vars: list):
    var_dict = {}
    for i in range(len(vars)):
        var_dict[vars[i]] = sy.symbols(vars[i])
    return var_dict

# sistema: lista de funções / vars: variáveis do sistema (strings) / x = x0
def snl_newton(sistema: list, vars: list, x: list, precisao: float):
    #var_dict = criar_vars(vars)
    delta = [0]*len(sistema)
    #while True:
    # Matriz jacobina
    j = [[0]*len(vars) for i in range(len(sistema))]
    iteracoes = 0
    
    while True:
        iteracoes += 1

        # Criação da matriz jacobiana
        for m in range(len(sistema)):
            for n in range(len(vars)):
                func = derivar(sistema[m], vars[n])
                j[m][n] = func(x[n])

        # Resolve JD = -F com gauss 
        delta = gst(j, [ - (sy.lambdify(vars, sistema[0])(x[0], x[1])), - (sy.lambdify(vars, sistema[1])(x[0], x[1]))])

        if sum([abs(elem) for elem in delta]) < precisao:
            break

        x = list(map(lambda x, y: x + y, x, delta))

    print(f"Resultado: {x}")
    print(f"Iterações: {iteracoes}")
    #return x

# ----- Funções
x, y = sy.symbols('x, y')
f1 = sy.exp(x) + y - 1
f2 = x**2 + y**2 - 4

snl_newton([f1, f2], [x, y], [1, -1], 10**(-15))
