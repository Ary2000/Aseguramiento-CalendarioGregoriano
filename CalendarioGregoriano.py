from operator import truediv
from enum import Enum


fechas = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
codigodMes = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]

headersMeses = ["          Enero             |            Febrebro          |            Marzo             |             Abril            |",
                "          Mayo              |             Junio            |            Julio             |             Agosto           |",
                "        Setiembre           |            Octubre           |           Noviembre          |           Diciembre          |"
                ]


class MesImpri:
    def __init__(self, numeroMes, cantidadDias, diaSemana, esBisiesto):
        self.numeroMes = numeroMes
        self.cantidadDias = cantidadDias
        self.diaSemana = diaSemana
        self.calendario = []
        self.esBisiesto = esBisiesto
        self.crearArreglo()

    def crearArreglo(self):
        arregloTemporal = []
        for i in range(6):
            arregloTemporal.append([0]*7)
        diaActual = 1
        dia = self.diaSemana
        for semana in range(6):
            # for dia in range(7):
            while(dia < 7):
                if(diaActual > self.cantidadDias):
                    if not(self.numeroMes == 2 and self.esBisiesto and diaActual <= 29):
                        break
                arregloTemporal[semana][dia] = diaActual
                diaActual += 1
                dia += 1
            dia = 0
        self.calendario = arregloTemporal


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


def bisiesto(anio):
    if anio < 1582:
        return False
    if anio % 100 > 0:
        return (anio % 100) % 4 == 0
    else:
        return (anio//100) % 4 == 0


def fecha_es_valida(tupla):
    # Se retorna falso en caso de que la tupla no contenga el formato correcto
    if not fecha_es_tupla(tupla):
        return False
    if tupla[0] <= 1582 and tupla[1] <= 10 and tupla[2] < 15:
        return False
    # Match para separar los casos de cada mes
    match tupla[1]:
        case Mes.ENERO.value:
            if tupla[2] <= fechas[Mes.ENERO.value - 1]:
                return True
        case Mes.FEBRERO.value:
            diasFebrero = fechas[Mes.FEBRERO.value - 1]
            # Tomar el caso del año bisiesto
            if bisiesto(tupla[0]) == True:
                diasFebrero += 1
            if tupla[2] <= diasFebrero:
                return True
        case Mes.MARZO.value:
            if tupla[2] <= fechas[Mes.MARZO.value - 1]:
                return True
        case Mes.ABRIL.value:
            if tupla[2] <= fechas[Mes.ABRIL.value - 1]:
                return True
        case Mes.MAYO.value:
            if tupla[2] <= fechas[Mes.MAYO.value - 1]:
                return True
        case Mes.JUNIO.value:
            if tupla[2] <= fechas[Mes.JUNIO.value - 1]:
                return True
        case Mes.JULIO.value:
            if tupla[2] <= fechas[Mes.JULIO.value - 1]:
                return True
        case Mes.AGOSTO.value:
            if tupla[2] <= fechas[Mes.AGOSTO.value - 1]:
                return True
        case Mes.SETIEMBRE.value:
            if tupla[2] <= fechas[Mes.SETIEMBRE.value - 1]:
                return True
        case Mes.OCTUBRE.value:
            if tupla[2] <= fechas[Mes.OCTUBRE.value - 1]:
                return True
        case Mes.NOVIEMBRE.value:
            if tupla[2] <= fechas[Mes.NOVIEMBRE.value - 1]:
                return True
        case Mes.DICIEMBRE.value:
            if tupla[2] <= fechas[Mes.DICIEMBRE.value - 1]:
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
    cantidadDias = fechas[tupla[1] - 1]
    if tupla[1] == 2:
        if bisiesto(tupla[0]):
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
        for mes in range(tupla[1] - 1):
            ordinal += fechas[mes]
        if bisiesto(tupla[0]) and tupla[1] > 2:
            ordinal += 1
        return ordinal


def obtenerDiaSemana(tupla):
    a = tupla[2]
    b = codigodMes[tupla[1] - 1]
    c = tupla[0] % 100
    d = c // 4
    suma = (a + b + c + d)
    if (tupla[1] == 1 or tupla[1] == 2) and bisiesto(tupla[0]):
        suma -= 1
    respuesta = suma % 7
    if tupla[0] >= 2000:
        respuesta -= 1
    if respuesta < 0:
        respuesta = 6
    return respuesta


def imprimir_3x4(anno):
    # Crear lista con todos los meses dentro
    todosMeses = [
        MesImpri(1, fechas[0], obtenerDiaSemana((anno, 1, 1)), False),
        MesImpri(2, fechas[1], obtenerDiaSemana((anno, 2, 1)), bisiesto(anno)),
        MesImpri(3, fechas[2], obtenerDiaSemana((anno, 3, 1)), False),
        MesImpri(4, fechas[3], obtenerDiaSemana((anno, 4, 1)), False),
        MesImpri(5, fechas[4], obtenerDiaSemana((anno, 5, 1)), False),
        MesImpri(6, fechas[5], obtenerDiaSemana((anno, 6, 1)), False),
        MesImpri(7, fechas[6], obtenerDiaSemana((anno, 7, 1)), False),
        MesImpri(8, fechas[7], obtenerDiaSemana((anno, 8, 1)), False),
        MesImpri(9, fechas[8], obtenerDiaSemana((anno, 9, 1)), False),
        MesImpri(10, fechas[9], obtenerDiaSemana((anno, 10, 1)), False),
        MesImpri(11, fechas[10], obtenerDiaSemana((anno, 11, 1)), False),
        MesImpri(12, fechas[11], obtenerDiaSemana((anno, 12, 1)), False)
    ]

    # Para el header de los nombres de los meses
    contadorMeses = 0
    for numMes in range(0, 12, 4):
        print(headersMeses[contadorMeses])
        print("D   L   K   M   J   V   S   |  D   L   K   M   J   V   S   |  D   L   K   M   J   V   S   |  D   L   K   M   J   V   S   |")
        for semana in range(6):
            lineaCalendario = [todosMeses[numMes].calendario[semana], todosMeses[numMes + 1].calendario[semana],
                               todosMeses[numMes + 2].calendario[semana], todosMeses[numMes + 3].calendario[semana]]
            # Ciclo para imprimir toda la tanda de meses
            for semanaMes in lineaCalendario:
                # Ciclo para imprimir la linea
                for diaSemana in semanaMes:
                    if(diaSemana < 10):
                        if(diaSemana == 0):
                            print("    ", end="")
                        else:
                            print(diaSemana, "  ", end="")
                    else:
                        print(diaSemana, " ", end="")
                print("|  ", end="")
            print("")
        contadorMeses += 1


imprimir_3x4(2022)
