from exponencial import exponencial
import math as mt

#f(x) = e^x * sen(x) - 1 

def expsen(x):
    return exponencial(x, 10**(-8))*mt.sin(x)-1
