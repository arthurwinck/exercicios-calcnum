# Eliminação de gauss sem troca física de linhas

def gauss_sem_troca(matriz: list, b: list):
    x = [0]*len(matriz)
    posmap = [i for i in range(len(matriz))]
    
    # Pivotamento -----------------------

    for j in range(len(matriz[0]) - 1):
        maior = matriz[posmap[j]][j]
        linha_maior = j

        for i in range(len(matriz)):
            elem = matriz[posmap[i]][j]
            if abs(elem) > abs(maior):
                maior = matriz[posmap[i]][j]
                linha_maior = i

        if linha_maior > j:
            posmap[linha_maior], posmap[j] = posmap[j], posmap[linha_maior]

        for l in range(j+1, len(matriz)):
            mult = matriz[posmap[l]][j]/matriz[posmap[j]][j]
            for k in range(len(matriz[0])):
                matriz[posmap[l]][k] -= mult*matriz[posmap[j]][k]

            b[posmap[l]] -= mult*b[posmap[j]]


    #print(f"Matriz A: {matriz}")

    # print('[')
    # for i in range(len(matriz)):
    #     print('[', end='')
    #     for j in range(len(matriz[0])):
    #         print(f'{matriz[posmap[i]][j]}', end=" ")
    #     print(']')
    # print(']')

    #Retrosubstituição ---------------------------

    x[-1] = b[posmap[-1]]/matriz[posmap[-1]][-1]

    for i in range(len(matriz) - 2, -1, -1):
        soma = 0
        for j in range(i+1, len(matriz)):
            soma += matriz[posmap[i]][j]*x[j]

        x[i] = (b[posmap[i]] - soma)/matriz[posmap[i]][i]


    # Resíduo -----------------------
    r = [0]*len(matriz)

    for c in range(len(matriz)):
        soma = 0
        for v in range(len(matriz)):
            soma += matriz[posmap[c]][v]*x[v]

        r[c] = b[posmap[c]] - soma


    # print(f"Matriz A: {matriz}")
    # print(f"Vetor B: {b}")
    # print(f"Vetor X: {x}")
    # print(f"Vetor Resíduo: {r}")
    # print(f"Vetor O: {posmap}")
    return x

#gauss_sem_troca([[-0.421, 0.784 ,0.279], [0.448, 0.832 ,0.193], [0.421, 0.784, 0.207]], [0, 1, 0])
#gauss_sem_troca([[2, -4, -1], [-1, 1, 4], [4, 2, 3]], [-5, 1, 7])


gauss_sem_troca(matriz=[[1, 1, 1.5, 1, 1.5, 0, 0, 0, 0, 0],
    [0, 1, 0.01, 0.51, 1.5, 0.5, 0, 0, 0, 0],
    [2.9, 1, 2, 1, 1, 0, 5, 0, 0, 0],
    [9, 1, 0.2, 1, 1, 0, 0, 1.5, 0, 0],
    [1, 0, 2, 0, 0, 1, 1, 1, 0, 2],
    [0, 1, 0, 0, -2, 0, 1, -1, 1, 1], 
    [1, 0, 2, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 2, 0, 1, 1, 1, -1],
    [0, 0, 1, 0, 2, 1, -1, 0, -1, -1],
    [0, 1, 0, 0, 2, 0, 1, 0, 1, 1]
    ],
    b=[4, -3, 1, -1, -1, 0, -1, 1, 3, -2]
    )