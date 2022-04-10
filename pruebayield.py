
def valores(numb):
    for num1 in numb:
        yield num1 * num1
        


for num in valores([2,4,3]):
    print(num)

libro = {
    'nombre':'python',
    'texto':'enseñanza'
}

match libro:
    case {'nombre':nombre,
        'tamaño':tamaño
    }:
        print('esto es un tamaño')
    case {
        'nombre':nombre,
        'texto':texto
    }:
        print('esto es un libro')

    case _:
        print('no se encontro nada comparado')


def square(number: int | float) -> int | float:
    return number ** 2

print(square(3.5))

def calcular(importe, descuento): 
    return importe - (importe * descuento / 100) 

datos = [1500, 10] 
print (calcular(*datos))