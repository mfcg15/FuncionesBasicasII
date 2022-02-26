#1
def countdown(numero):
    listaCountDown = "["
    for i in range(numero,-1,-1):
        if(i==0):
            listaCountDown += str(i)
        else:
            listaCountDown += str(i)+","
    listaCountDown += "]"
    return listaCountDown
print(countdown(5))

#2
def imprimir_y_devolver(arr):
    if(len(arr)>2):
        return "La lista debe tener solo dos numeros"
    else:
        print(arr[0])
        return arr[1]
print(imprimir_y_devolver([1,2,4]))

#3
def primero_mas_longitud(arr):
    suma = len(arr)
    suma = suma + arr[0]
    return suma
print(primero_mas_longitud([1,2,3,4,5]))


#4
def valores_mayores_que_el_segundo(arr):
    longitudArr = len(arr)
    listaMayores = "["
    contador = 0
    if(longitudArr>2):
        for i in arr:
            if(i == arr[longitudArr-1]):
                if(i > arr[1]):
                    listaMayores += str(i)
                    contador = contador+1
            else:
                if(i > arr[1]):
                    listaMayores += str(i)+","
                    contador = contador+1
        listaMayores += "]"
        print(contador)
        return listaMayores
    else:
        return False
print(valores_mayores_que_el_segundo([5,2,3,2,1,4]))
print(valores_mayores_que_el_segundo([3]))

#5
def length_and_value(tamaño,valor):
    arr = []
    for i in range(0,tamaño):
        arr.append(valor)
    return arr
print(length_and_value(4,7))
print(length_and_value(6,2))

