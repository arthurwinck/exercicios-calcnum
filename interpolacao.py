from gauss_sem_troca import gauss_sem_troca as gst
import numpy as np

def funcao(a: list, lista_x: list, x: int):
    y = list(map(lambda x, y: abs(x - y), lista_x, a))


def interpolacao(x: list[int], y: list[int]):
    n = len(x)

    V = [[0]*n for _ in range(n)]     

    for i in range(n):
        for j in range(n):
            V[i][j] = x[i]**j

    print(V)
    a = gst(V, y)
    print(a)
    #a = np.linalg.lstsq(V, x)
    #print(a)

interpolacao([-1, 0, 1], [4, 1, -1])

    