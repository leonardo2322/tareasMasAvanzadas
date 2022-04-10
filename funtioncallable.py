def funcion(nombre): 
    return "Hola " + nombre

def llamada_de_retorno(func=""): 
    if func in globals(): 
        if callable(globals()[func]): 
            return globals()[func]("Laura") 
    else: 
        return "Función no encontrada" 

print (llamada_de_retorno("funcion"))

nombre_de_la_funcion = "funcion"

if nombre_de_la_funcion in locals(): 
    if callable(locals()[nombre_de_la_funcion]): 
        print (locals()[nombre_de_la_funcion]("Facundo")) 
else:
    print ("Función no encontrada")