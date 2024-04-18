def lee_numero():
    nume_or = input('Lee numero: ')
    return nume_or

def may_men(nume_or):
    lista = []
    for digito in nume_or:
        lista.append(digito)
    lista.sort(reverse = True)
    salida = ''.join(lista)
    return salida

def men_may(nume_or):
    lista = list(nume_or)
    lista.sort()
    salida = ''.join(lista)
    return salida

def operacion_kaprekar(nume_or):
    anterior = ''
    ultimo = nume_or
    while anterior != ultimo:
        maymen = may_men(ultimo)
        menmay = men_may(ultimo)
        resta = int(maymen) - int(menmay)
        resta = str(resta)
        while len(resta) < 4:
            resta = '0' + resta
        anterior = ultimo
        ultimo = resta
    return ultimo

def mostrar_constante(constante):
    print('Constante: ', constante)

if __name__ == '__main__':
    nume_or = lee_numero()
    constante = operacion_kaprekar(nume_or)
    mostrar_constante(constante)