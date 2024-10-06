import os
import shutil

# Función para crear una carpeta si no existe
def crear_carpeta(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)
        print(f"Carpeta '{ruta}' creada.")
    else:
        print(f"La carpeta '{ruta}' ya existe.")

# Función para mover archivos a una carpeta específica
def mover_archivos(origen, destino, extensiones):
    crear_carpeta(destino)
    archivos = [archivo for archivo in os.listdir(origen) if archivo.endswith(tuple(extensiones))]
    
    for archivo in archivos:
        archivo_origen = os.path.join(origen, archivo)
        archivo_destino = os.path.join(destino, archivo)
        shutil.move(archivo_origen, archivo_destino)
        print(f"Moviendo {archivo} a {destino}")

# Función principal
def main():
    origen = "C:\\Users\\marti\\Downloads"
    destino = "C:\\Users\\marti\\Downloads\\imagenes"
    
    # Lista de extensiones que quieres mover
    extensiones = [".jpeg", ".jpg", ".png"]

    mover_archivos(origen, destino, extensiones)

if __name__ == "__main__":
    main()

#ff