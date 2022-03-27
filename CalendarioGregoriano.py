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
    # Se retorna falso en caso de que la tupla no contenga el formato correcto
    if not fecha_es_tupla(tupla):
        return False
    # Match para separar los casos de cada mes
    match tupla[1]:
        case Mes.ENERO.value:
            if tupla[2] <= fechas[Mes.ENERO.value]:
                return True
        case Mes.FEBRERO.value:
            diasFebrero = fechas[Mes.FEBRERO.value]
            # Tomar el caso del año bisiesto
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
        # En caso que se hubiera usado un número de mes que no existe en el calendario gregoriano
        case _:
            return False
    return False


def dia_siguiente(tupla):
    # Revisar si la fecha es valida
    if not fecha_es_valida(tupla):
        return False

    # Asegurar que si es febrero y bisiesto, sumarle 1 mas al total de dias
    cantidadDias = fechas[tupla[1]]
    if tupla[1] == 2:
        if bisiesto(tupla):
            cantidadDias += 1

    if tupla[2] < cantidadDias:
        return (tupla[0], tupla[1], tupla[2] + 1)

    elif tupla[1] < 12:
        return (tupla[0], tupla[1] + 1, 1)
    else:
        return(tupla[0] + 1, 1, 1)

def ordinal_dia(tupla):
    if not fecha_es_valida(tupla):
        return -1
    else:
        ordinal = tupla[2]
        for mes in range(tupla[1]):
            ordinal += fechas[mes]
        if bisiesto(tupla) and tupla[1] > 2:
            ordinal += 1
        return ordinal


if fecha_es_valida((2021, 2, 29)):
    print("Valido :)")
else:
    print("No valido :(")
