def lee_numero():
    numero = input('Ingrese numero de 5 digitos: ')
    return numero

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
    while len(dife) < 5:
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
    return nume_calculado, lista

def mostrar_constante(constante, lista):
    print(f'La constante de Kaprekar para numero de 5 digitos es: {constante}')
    print('Lista: ', lista)

if __name__ == '__main__':
    nume_or = lee_numero()
    constante, lista = ciclo_kaprekar(nume_or)
    mostrar_constante(constante, lista)