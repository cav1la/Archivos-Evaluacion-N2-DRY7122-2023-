import requests #se importa para realizar una solicitud HTTP a una URL
import csv      #se importa para trabajar con archivos CSV

url = "https://dummyjson.com/quotes"    #URL de donde podremos obtener los datos

response = requests.get(url)    #Realiza la solicitud HTTP a la URL
data = response.json()          #Se obtiene la respuesta solicitada en JSON y se guarda en 'data' que es el nombre que se le dio

#Extraer citas y autores del JSON obtenido
quotes = data['quotes']                             
authors = [quote['author'] for quote in quotes]
texts = [quote['quote'] for quote in quotes]

archivo = 'endpoint.csv'   #Nombre del archivo CSV que se creará

with open(archivo, 'w', newline='') as file:   #Abrir el archivo CSV en modo de escritura y configurar el escritor CSV
    writer = csv.writer(file, delimiter=';')    #Se agrega un ';' para realizar un cambio de columna
    writer.writerow(['Autor', 'Texto'])         #Es lo que se escribe en la primera fila con los encabezados

    for author, text in zip(authors, texts):    #Escribir cada cita y autor en el archivo CSV
        writer.writerow([author, text])         #Se escribe una fila con el autor y el texto
        writer.writerow(['', ''])               #Se escribe una fila vacía para separar las citas

print(f"Los datos de la URL fueron guardados en el archivo: '{archivo}'.")   # Mensaje de confirmación
