from operator import truediv
from enum import Enum


fechas = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Mes(Enum):
    ENERO = 1
    FEBRERO = 2
    MARZO = 3
    ABRIL = 4
    MAYO = 5
    JUNIO = 6
    JULIO = 7
    AGOSTO = 8
    SETIEMBRE = 9
    OCTUBRE = 10
    NOVIEMBRE = 11
    DICIEMBRE = 12


def fecha_es_tupla(tupla):
    if(not isinstance(tupla, tuple)):
        print("Ingrese una tupla")
        return False
    elif len(tupla) != 3:
        print("Ingrese una tupla con el formato YYYY,MM,DD")
        return False
    for dato in tupla:
        if not isinstance(dato, int) or dato <= 0:
            print("Los datos deben ser numeros enteros positivos")
            return False
    if tupla[0] < 1582 or tupla[1] > 13 or tupla[2] > 31:
        print("Ingrese una fecha posterior al 1582/10/15")
        return False
    return True


def bisiesto(tupla):
    if not fecha_es_tupla(tupla):
        return False
    if tupla[0] % 100 > 0:
        return (tupla[0] % 100) % 4 == 0
    else:
        return (tupla[0]//100) % 4 == 0


def fecha_es_valida(tupla):
    if not fecha_es_tupla(tupla):
        return False
    match tupla[1]:
        case Mes.ENERO.value:
            if tupla[2] <= fechas[Mes.ENERO.value]:
                return True
        case Mes.FEBRERO.value:
            diasFebrero = fechas[Mes.FEBRERO.value]
            if bisiesto(tupla) == True:
                diasFebrero += 1
            if tupla[2] <= diasFebrero:
                return True
        case Mes.MARZO.value:
            if tupla[2] <= fechas[Mes.MARZO.value]:
                return True
        case Mes.ABRIL.value:
            if tupla[2] <= fechas[Mes.ABRIL.value]:
                return True
        case Mes.MAYO.value:
            if tupla[2] <= fechas[Mes.MAYO.value]:
                return True
        case Mes.JUNIO.value:
            if tupla[2] <= fechas[Mes.JUNIO.value]:
                return True
        case Mes.JULIO.value:
            if tupla[2] <= fechas[Mes.JULIO.value]:
                return True
        case Mes.AGOSTO.value:
            if tupla[2] <= fechas[Mes.AGOSTO.value]:
                return True
        case Mes.SETIEMBRE.value:
            if tupla[2] <= fechas[Mes.SETIEMBRE.value]:
                return True
        case Mes.OCTUBRE.value:
            if tupla[2] <= fechas[Mes.OCTUBRE.value]:
                return True
        case Mes.NOVIEMBRE.value:
            if tupla[2] <= fechas[Mes.NOVIEMBRE.value]:
                return True
        case Mes.DICIEMBRE.value:
            if tupla[2] <= fechas[Mes.DICIEMBRE.value]:
                return True
        case _:
            return False
    return False


if fecha_es_valida((2021, 2, 29)):
    print("Valido :)")
else:
    print("No valido :(")
