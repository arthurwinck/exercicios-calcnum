#Método de bisseção por recursao
def bissecao(a, b, funcao, precisao):
    resA = funcao(a)
    resB = funcao(b)

    #Pode existir uma raíz aqui?
    if resA*resB < 0:
        x = (a+b)/2
        resX = funcao(x)

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
