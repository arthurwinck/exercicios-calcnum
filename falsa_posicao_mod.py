# Método de Falsa Posição por recursão
# R(x) = f(a) - ( (f(b)-f(a))/b-a )*(x-a)

from xdez import xdez

def falsa_posicao_mod_iter(a, b, funcao, precisao):
    iter = 0
    resA = funcao(a)
    resB = funcao(b)

    while True:
        iter += 1

        #Pode existir uma raíz aqui?
        if resA*resB < 0:
            
            x = (a*resB - b*resA)/(resB - resA)
            resX = funcao(x)

            if abs(resX) < precisao:
                print(f"raíz = {x} / precisão = {resX} / iterações {iter}")
                break

            if resA*resX < 0:
                pa = resB/(resB+resX)
                resA = resA*pa
                b = x
                resB = resX
            
            else:
                pb = resA/(resA+resX)
                resB = resB*pb
                a = x
                resA = resX

def falsa_posicao(a, b, funcao, precisao, iter):
    resA = funcao(a)
    resB = funcao(b)
    iter += 1

    #Pode existir uma raíz aqui?
    if resA*resB < 0:
        
        x = a - resA*(b - a)/(resB - resA)
        resX = funcao(x)

        if abs(resX) < precisao:
            print(f"raíz = {x} / precisão = {resX} / iterações {iter}")
            return x
    
        #Testar os dois subintervalos
        if resA*resX < 0:
            resFunc = falsa_posicao(a, x, funcao, precisao, iter)
            if resFunc != None:
                return resFunc
        else:
            resFunc = falsa_posicao(x, b, funcao, precisao, iter)
            if resFunc != None:
                return resFunc

    return None    

falsa_posicao_mod_iter(0, 2, xdez, 10**(-10))