import numpy as np
import pandas as pd

# tipo 0: polinomial, tipo 1: exponencial
def ajuste_curva(matriz: list, x: list, y: list, tipo: int):

    n = len(x) #Número de pontos
    m = 0 #Grau de ajuste

    # Se o tipo é exponencial, y = ln(y)
    if tipo == 1:
        # lambda blablabla y = ln(y)
        y = list(map(lambda x: np.log2(x), y))
        # parâmetro m sempre 1 quando exponencial
        m = 1
    
    for i in range(m):
        # Só precisamos calcular a diagonal, já que a matriz é simétrica
        for j in range(i, m):
            matriz[i][j] = m[i][j]*x[k]**(i+j-2)
            
        if i != j:
            # Simetria
            matriz[j][i] = matriz[i][j]
    
    b = []
    b[1] = 0
    for k in range(n):
        b[i] = b[i]+ x[k]*x[k]**(i-1)

    # d = determinante(matriz)
    # Cálculo de mal-condicionamento
    # C1 = cond(matriz)

    #Resolver com gauss / método direto
    #c = A\b'

    if tipo == 0: #Se o tipo é polinomial precisamos do somatório de g
        g = []

        for k in range(n):
            g[k] = 0
            for i in range(m):
                g[k] = g[k] + c[1]*x[k]**(i-1)
    else:
        # c1 e c2 já são o resultado
        c[0] = np.exp(c1)

        for k in range(n):
            # Para cada ponto xi, temos a função g(xi)
            g[k] = c[0]*np.exp(c[1]*x[k]) 

    # Plotar gráfico com pandas

# Escolher entre 2 ajustes, escolher a melhor curva = menor desvio padrão dos pontos