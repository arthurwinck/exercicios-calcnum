import math as mt
from bissecao import bissecao
from exponencial import exponencial

#f(x) = ex – 2cos(x) no intervalo inicial [0 ; 2]

def expcos(x):
    return exponencial(x, 10**(-8)) - float(2*mt.cos(x))

#exponencial(5,10**(-10))
#print(expcos(2))
res = bissecao(0,2, expcos, 10**(-8))