fechas = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def fecha_es_tupla(tupla):
    if(not isinstance(tupla,tuple)):
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
    if tupla[0]%100 > 0:
        return (tupla[0]%100)%4 == 0
    else:
        return (tupla[0]//100)%4 == 0
