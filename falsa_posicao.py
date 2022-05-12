# Método de Falsa Posição por recursão
# R(x) = f(a) - ( (f(b)-f(a))/b-a )*(x-a)

def falsa_posicao(a, b, funcao, precisao):
    resA = funcao(a)
    resB = funcao(b)

    #Pode existir uma raíz aqui?
    if resA*resB < 0:
        
        # Refazer para método de falsa posição
        #retaX = resA + (resB-resA)/(b-a)*(x-a)
        resX = resA + (resB-resA)/(b-a)*(x-a)

        #resX = funcao(x)

        #print(f"a: {a} b: {b} x: {x}")

        #Será que o ponto médio satisfaz (é raíz) a precisão?
        if abs(resX) < precisao:
            print(f"x = {x}, resX = {resX}")
            return x
    
        #Testar os dois subintervalos
        if resA*resX < 0:
            resFunc = bissecao(a, x, funcao, precisao)
            if resFunc != None:
                return resFunc
        else:
            resFunc = bissecao(x, b, funcao, precisao)
            if resFunc != None:
                return resFunc

    return None    
