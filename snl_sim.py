import numpy as np
from gauss_sem_troca import gauss_sem_troca as gst

# sistema: lista de funções / vars: variáveis do sistema (strings) / x = x0
def snl_newton(sistema: list, x: list, h: float, precisao: float):
    #var_dict = criar_vars(vars)
    delta = [0]*len(sistema)
    #while True:
    # Matriz jacobina
    j = [[0]*len(x) for i in range(len(sistema))]
    iteracoes = 0
    
    while True:
        iteracoes += 1

        # Criação da matriz jacobiana
        for m in range(len(sistema)):
            for n in range(len(x)):
                j[m][n] = (sistema[m](x[0] + h*(1 - n), x[1] + h*n) - sistema[m](x[0], x[1]))/h

        # Resolve JD = -F com gauss 
        delta = gst(j, [ - (sistema[0](x[0], x[1])), - (sistema[1](x[0], x[1]))])

        if sum([abs(elem) for elem in delta]) < precisao:
            break

        x = list(map(lambda x, y: x + y, x, delta))

    print(f"Resultado: {x}")
    print(f"Iterações: {iteracoes}")
    #return x

# ----- Funções
def f1(x,y):
    return np.exp(x) + y - 1
def f2(x,y):
    return x**2 + y**2 - 4

snl_newton([f1, f2], [1, -1], 0.1, 10**(-15))
