def dec_lu_crout(matriz: list[list[int]], b: list):
    n = len(b)

    # Montagem da L

    mat_l = [[0]*len(matriz[0]) for _ in range(len(matriz))]
    mat_u = [[0]*len(matriz[0]) for _ in range(len(matriz))]
    x = [0]*len(matriz[0])
    y = [0]*len(matriz[0])

    # k -> coluna de U
    for k in range(n):
        # i -> linha de L
        for i in range(k, n):
            soma = 0

            print(f"i = {i}, k = {k}")
            
            for t in range(k):
                soma += mat_l[i][t]*mat_u[t][k]
                print("bingudo")
            
            mat_l[i][k] = matriz[i][k] - soma
            print(f"matriz = {mat_l[i][k]}, soma = {soma}")
            


        mat_u[k][k] = 1

        for j in range(k+1, n):
            soma = 0
            for t in range(k):
                soma += mat_l[k][t]*mat_u[t][j]

            mat_u[k][j] = (matriz[k][j] - soma)/mat_l[k][k]

    print(f"Matriz L: {mat_l}")
    print(f"Matriz U: {mat_u}")
    

    # Substituição Direta
    y[0] = b[0]/mat_l[0][0]

    for i in range(1, n):
        soma = 0
        for j in range(i):
            soma += mat_l[i][j]*y[j]

        y[i] = (b[i] - soma)/mat_l[i][i]

    # Retrosubstituição
    x[-1] = y[-1]/mat_u[-1][-1]

    for i in range(len(matriz) - 2, -1, -1):
        soma = 0
        for j in range(i+1, len(matriz)):
            soma += mat_u[i][j]*x[j]

        x[i] = (y[i] - soma)/mat_u[i][i]

    print(f"Vetor Y: {y}")
    print(f"Vetor X: {x}")
    
#dec_lu_crout([[2, -1, 2], [2, 3, 3], [6, -1, 8]], [-2, -5, 0])
dec_lu_crout([[1, 1, 2], [3, -5, 1], [2, 1, -1]], [27, -9, -1])
 