# q deberia ser una lista con un solo elemento
def inicializar(N):
    ejex = [ -1,-2,-2,-1, 1, 2, 2, 1 ]
    ejey = [ -2,-1, 1, 2, 2, 1,-1,-2 ]
    q = [True]
    tablero = []
    for i in range(N):
        colum = []
        for j in range(N):
            colum.append(0)
        tablero.append(colum)
    return ejex, ejey, q, tablero

def mover(ncuad, tablero, i, pos_x, pos_y, q, ejex, ejey):
    k = 0
    q[0] = True
    while True:
        u = pos_x + ejex[k]
        v = pos_y + ejey[k]
        if (u >= 0 and u < N and v >= 0 and v < N):
            if (tablero[u][v] == 0):
                tablero[u][v] = i
                if (i < ncuad):
                    mover(ncuad, tablero,i+1,u,v,q, ejex, ejey)
                    if q[0] == True:
                        tablero[u][v] = 0
                else:
                    q[0] = False
        k = k + 1
        if not q[0] or k >= 8:   
            break

def mostrar(tablero, q):
    if not q[0] :
        for i in range(N):
            for j in range(N):
                nro = tablero[i][j]
                print('%3s'%str(nro), end = '')
            print()
    else:
        print("No existe solucion")

if __name__ == '__main__':
    N = 5
    ejex, ejey, q, tablero = inicializar(N)
    tablero[2][2] = 1 # Movimiento inicial
    mover(N*N, tablero,2,0,0,q, ejex, ejey)
    mostrar(tablero, q)


    
