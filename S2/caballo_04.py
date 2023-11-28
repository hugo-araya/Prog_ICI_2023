def mover(ncuad, tablero, i, pos_x, pos_y, q, ejex, ejey):
    k = 0
    q = True
    while True:
        u = pos_x + ejex[k]
        v = pos_y + ejey[k]
        if (u >= 0 and u < N and v >= 0 and v < N):
            if (tablero[u][v] == 0):
                tablero[u][v] = i
                if (i < ncuad):
                    mover(ncuad, tablero,i+1,u,v,q, ejex, ejey)
                    if not q:
                        tablero[u][v] = 0
                else:
                    q = False
        k = k + 1
        if  q and k >= 8:
            break

if __name__ == '__main__':
    ejex = [ -1,-2,-2,-1, 1, 2, 2, 1 ]
    ejey = [ -2,-1, 1, 2, 2, 1,-1,-2 ]
    N = 5
    q = False
    tablero = []
    for i in range(N):
        colum = []
        for j in range(N):
            colum.append(0)
        tablero.append(colum)

    tablero[0][0] = 1
    mover(N*N, tablero,2,0,0,q, ejex, ejey)

    if not q :
        for i in range(N):
            for j in range(N):
                print(tablero[i][j], end = ' ')
            print()
    else:
        print("No existe solucion")
