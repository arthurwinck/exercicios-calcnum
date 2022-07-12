def dif_newton(x: list[int], y: list[int]):
    n = len(x)
    matriz = [[x[i - n], y[i - n], y[i - n]] + [0]*(n-3) for i in range(n)]
    print(matriz)
    
    # for i in range(n):
    #     for j in range(i, 2):
    #         matriz[i][]

    print(matriz)
    # Adicionar offset da matriz + ordem 1
    for j in range(2, len(matriz)):
       for i in range(j, len(matriz[0])):
           matriz[i][j] = (matriz[i][j - 1] - matriz[i - 1][j - 1])/(x[i] - x[i - j + 1])

    for i in range(n):
        mult = 1
        for j in range(n):
            # Multiplicação
            mult *= 1

dif_newton([0, 1, 2], [2, 4, 6])