import sympy as sy
import numpy as np
import matplotlib.pyplot as pyp

#criar função no sympy
#-2x-y
# -1.000 -0.9000 -0.83000, -0.78

#Resultado analítico: -3e^(-x) -2x + 2

# Colocar x na função exata para comparar resultados

#Calcular erro: módulo de y exato - y descoberto

def edo_euler(a: float, b: float, n: int, y1: float, func: function):
    h = (b-a)/n
    x = [] # criar vetor x = [a:h:b]
    y = []
    y[0] = y1

    for i in range(n):
        y[i+1] = y[i] + h*func(x[i], y[i])

def edo_runge_kutta(a: float, b: float, n: int, y1: float, func: function):
    h = (b-a)/n
    x = [] # criar vetor x = [a:h:b]
    y = []
    y[0] = y1

    for i in range(n):
        k1 = h*func(x[i], y[i])
        y[i+1] = y[i] + (k1 + h*(func(x[i]+h, y[i]+k1)))/2

    #Erro módulo da subtração y encontrado de y exato
    #y = list(map(lambda x: np.log2(x), y))

def edo_runge_kutta_quarta(a: float, b: float, n: int, y1: float, func: function):
    h = (b-a)/n
    x = [] # criar vetor x = [a:h:b]
    y = []
    y[0] = y1

    for i in range(n):
        k1 = h*func(x[i], y[i])
        k2 = h*func(x[i] + h/2, y[i])
        k3
        k4
        y[i+1] = y[i] + (k1 + h*(func(x[i]+h, y[i]+k1)))/2

    #Erro módulo da subtração y encontrado de y exato
    #y = list(map(lambda x: np.log2(x), y))


