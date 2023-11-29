def lee_numero():
    numero = input('Ingrese numero de 4 digitos: ')
    return numero

def comprueba(numero):
    if numero[0] == numero[1] and numero[0] == numero[2] and numero[0] == numero[3]:
        return False
    else:
        return True

def may_men(nume_or):
    numero = []
    for digito in nume_or:
        numero.append(digito)
    numero.sort(reverse = True)
    nume_may_men = ''.join(numero)
    return nume_may_men

def men_may(nume_or):
    numero = list(nume_or)
    numero.sort()
    nume_may_men = ''.join(numero)
    return nume_may_men

def diferencia(nume_1, nume_2):
    dife = int(nume_1) - int(nume_2)
    dife = str(dife)
    while len(dife) < 4:
        dife = '0' + dife
    return dife

def ciclo_kaprekar(nume_or):
    lista = []
    anterior = ''
    nume_calculado = nume_or
    while anterior != nume_calculado:
        lista.append(nume_calculado)
        nume_1 = may_men(nume_calculado)
        nume_2 = men_may(nume_calculado)
        nume_1_2 = diferencia(nume_1, nume_2)
        anterior = nume_calculado
        nume_calculado = nume_1_2
    return nume_calculado

def mostrar(estatus):
    if estatus == True:
        print('La constante es la misma')
    else:
        print('La constante NO es la misma')

def genera_numeros(inicio, fin):
    sta = True
    for nume in range(inicio, fin):
        nume_str = str(nume)
        if comprueba(nume_str) == True:
             constante = ciclo_kaprekar(nume_str)
             if constante != '6174':
                 sta = False
    return sta

if __name__ == '__main__':
    estatus = genera_numeros(1000, 9999)
    mostrar(estatus)