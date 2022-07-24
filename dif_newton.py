import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

def dif_newton(lista_x: list[int], lista_y  : list[int]):
    x = sy.Symbol('lista_x')
    n = len(lista_x)
    matriz = [[lista_x[i - n], lista_y[i - n], lista_y[i - n]] + [0]*(n-3) for i in range(n)]
    print(matriz)
    
    # for i in range(n):
    #     for j in range(i, 2):
    #         matriz[i][]

    print(matriz)
    # Adicionar offset da matriz + ordem 1
    for j in range(2, len(matriz)):
       for i in range(j, len(matriz[0])):
           matriz[i][j] = (matriz[i][j - 1] - matriz[i - 1][j - 1])/(lista_x[i] - lista_x[i - j + 1])

    # Simbólico
    for i in range(n):
        mult = matriz[i][i]
        multX = 1
        
        for j in range(i):
            # Multiplicação - guardar o multiplicatório para usar em cada termo do somatório
            multX *= 1

        # a[i][i] * (lista_x -xj)....
        mult *= multX


dif_newton([0, 1, 2], [2, 4, 6])