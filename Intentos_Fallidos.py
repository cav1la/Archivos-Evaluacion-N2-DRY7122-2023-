import datetime # El módulo datetime para trabajar con fechas y horas
import re       # El módulo re para trabajar con expresiones regulares

hora_actual = datetime.datetime.now().time() # Se obtiene la hora actual

# Se calcula la hora de cierre anterior, restando una hora a la hora actual y ajustando los minutos, segundos y microsegundos a 0
hora_cerrada_anterior = (datetime.datetime.now() - datetime.timedelta(hours=1)).replace(minute=0, second=0, microsecond=0).time()

# Se verifica si hubo un cambio de día comparando las horas de cierre anterior y actual
if hora_cerrada_anterior.hour > hora_actual.hour:
    cambio_dia = True
else:
    cambio_dia = False

# Se establece el rango de tiempo dentro del cual se buscarán los registros, dependiendo del cambio de día o no
if cambio_dia:
    rango_inicio = datetime.time(hour=hora_cerrada_anterior.hour, minute=0)
    rango_fin = datetime.time(hour=23, minute=59)
else:
    rango_inicio = datetime.time(hour=hora_cerrada_anterior.hour, minute=0)
    rango_fin = datetime.time(hour=hora_actual.hour, minute=59)

archivo_registros = '/var/log/secure' or '/var/log/Auth.log'    # Se define el archivo de registros a analizar

intentos_fallidos = 0   # Variable para contar los intentos fallidos de inicio de sesión

# Abre el archivo de registros especificado en modo de lectura utilizando la declaración "with", lo que garantiza que el archivo se cierre adecuadamente después de su uso.
with open(archivo_registros, 'r') as archivo:
    for linea in archivo:
        if 'Failed password' or 'incorrect password' in linea:  # Verifica si la línea contiene las cadenas 'Failed password' o 'incorrect password'.
            hora_registro = re.search(r'\b\d{2}:\d{2}:\d{2}\b', linea)  # Se busca una hora en formato HH:MM:SS en cada línea del archivo de registros
            if hora_registro:
                hora_registro = datetime.datetime.strptime(hora_registro.group(), '%H:%M:%S').time()  # Se convierte la hora encontrada en formato de cadena a objeto de tiempo
                
                if rango_inicio <= hora_registro <= rango_fin:  # Si la hora de registro está dentro del rango establecido, se incrementa el contador
                    intentos_fallidos += 1  # Si la hora de registro está dentro del rango, se incrementa el contador de intentos fallidos.

# Se muestra el resultado final del conteo de intentos fallidos de inicio de sesión en el rango de tiempo especificado
print(f"La cantidad total de intentos fallidos de inicio de sesión en el rango {rango_inicio} - {rango_fin} es: {intentos_fallidos}")