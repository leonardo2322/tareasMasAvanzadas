import os

ruta_imagenes = "paths_imagenes.txt"
rutas = os.listdir("/home/hidden/Imágenes/imagenesCuido/WhatsApp Images/")
archivo = open(ruta_imagenes,'w')
lista= []
for ruta in rutas:
    archivo.write((os.path.join(os.getcwd(),ruta)+"\n"))

archivo.close()

