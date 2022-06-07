# Escolhemos valor inicial zero para sistemas iterativo de sistemas lineares, o algoritmo se "ajeita"
def gaus_jacobi(matriz: list, b: list, precisao: float):
    lista_x0 = [0]*len(matriz[0])
    lista_x = lista_x0[:]
    iter = 0

    while True:
        for i in range(len(matriz)):
            soma = 0
            for j in range(len(matriz[0])):
                if i != j:
                    soma += matriz[i][j]*lista_x0[j]

            lista_x[i] = (b[i] - soma)/matriz[i][i]

        lista_desvio = list(map(lambda x, y: abs(x - y), lista_x, lista_x0))
        iter += 1

        if sum(lista_desvio) < precisao:
            break
        
        lista_x0 = lista_x[:]

    print(f"Resultado: {lista_x} com {iter} iterações")

gaus_jacobi([[3, -1, -1], [1, 3, 1], [2, -2, 4]], [1,5,4], 10**(-8))