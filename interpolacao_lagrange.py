import sympy as sy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def interpolacao(lista_x: list[int], lista_y: list[int], sim):
    g = len(lista_x) - 1
    n = len(lista_x)
    l = 0

    for i in range(n):
        x = sim
        mult = 1
        div = 1

        for j in range(n):
            if i != j:
                mult *= (x - lista_x[j])
                div *= (lista_x[i] - lista_x[j])

        l += (mult/div)*lista_y[i]


    if not isinstance(sim, float) and not isinstance(sim, int):
        print(sy.factor(l))
        func = sy.lambdify(x, l)
        pontos = list(map(lambda x: func(x), lista_x))
        #plt.plot(lista_x, pontos)
        #plt.show()

        # Gerar números interpoladores e plotar o gráfico
        gerar_x = [x/10.0 for x in range(int(lista_x[0]*10), int(lista_x[-1]*10), 2)]
        gerar_y = list(map(lambda x: func(x), gerar_x))
        plt.plot(gerar_x, gerar_y)
        plt.show()

    else:
        print(f"f({sim}) = {l}")

# sim ou é um número (calculando numericamente) ou um símbolo do sympy, para que possa ver a função interpoladora
#interpolacao([-1, 0, 1], [4, 1, -1], 0.5)
interpolacao([-1, 0, 1], [4, 1, -1], sy.Symbol('x'))

#lista_x = [x/10.0 for x in range(int(lista_x[0]*10), int(lista_x[-1]*10), 2)]
#interpolacao([0.5, 45.5, 100], list(map(lambda x: np.log(x), [0.5, 45.5, 100])), sy.Symbol('x'))

#print(np.log2(-1))