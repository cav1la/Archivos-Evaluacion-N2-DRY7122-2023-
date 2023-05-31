import os   # Se importa el módulo os para interactuar con el sistema operativo.

disk = os.statvfs('/')  # Se obtiene información sobre el sistema de archivos de la raíz '/' utilizando os.statvfs.

# Se calcula el espacio disponible en el disco multiplicando el número de bloques disponibles (f_bavail) por el tamaño de bloque (f_frsize).
disk_space_available = disk.f_bavail * disk.f_frsize    

# Se convierte el espacio disponible en el disco a gigabytes dividiéndolo por 1024 elevado a la potencia 3.
disk_space_available_gb = disk_space_available / (1024 ** 3)

print(f"Espacio disponible en el disco: {disk_space_available_gb:.2f} GB")  # Se muestra la cantidad de espacio disponible en el disco con dos decimales.

with open('/proc/meminfo') as file: # Se abre el archivo '/proc/meminfo' que contiene información sobre la memoria del sistema.
    for line in file:   # Se itera sobre cada línea del archivo.
        if line.startswith('MemAvailable:'):    # Se verifica si la línea comienza con 'MemAvailable:'.
            _, value, unit = line.split()       # Se divide la línea en sus componentes: etiqueta, valor y unidad.
            memory_available = int(value) * 1024    # Se convierte el valor de la memoria disponible de kilobytes a bytes.
            memory_available_gb = memory_available / (1024 ** 3)    # Se convierte la memoria disponible a gigabytes dividiéndola por 1024 elevado a la potencia 3.
            break   # Se sale del bucle después de encontrar la línea 'MemAvailable:'.

print(f"Memoria disponible: {memory_available_gb:.2f} GB")  # Se muestra la cantidad de memoria disponible con dos decimales.

cpu_cores = os.cpu_count()  # Se obtiene el número de núcleos de CPU disponibles utilizando os.cpu_count().

print(f"Núcleos de CPU disponibles: {cpu_cores}")   # Se muestra el número de núcleos de CPU disponibles.

network_info = os.popen('ifconfig').read()  # Se ejecuta el comando 'ifconfig' utilizando os.popen() para obtener información de red.

print(f"Información de red:\n{network_info}")   # Se muestra la información de red obtenida.