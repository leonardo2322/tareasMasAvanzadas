def funcion(): 
    return "Hola Mundo1" 

def saludar(nombre, mensaje='Hola'): 
    print (mensaje, nombre) 
    print (mi_funcion())

def funcion2():
    return "Hola Mundo2"

def llamada_de_retorno(func=""): 
    """Llamada de retorno a nivel global""" 
    return globals()[func]()

# print (llamada_de_retorno("funcion")) 

# Llamada de retorno a nivel local 
print(llamada_de_retorno('funcion'))
nombre_de_la_funcion = "funcion2" 
print (locals()[nombre_de_la_funcion]())