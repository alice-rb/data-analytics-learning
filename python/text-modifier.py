import pandas as pd
import string
from collections import Counter
import os
import numpy as np
import matplotlib.pyplot as plt


print('-------------EJERCICIO 1 - Leer archivo y mostrar contenido---------------------')

def leer_poema(nombre_archivo):
        with open(nombre_archivo, 'r') as poema:
            for linea in poema:
                print(linea.strip())

leer_poema("poema.txt")

print('-------------EJERCICIO 2 - Contar líneas de texto en archivo---------------------')

def contar_lineas(nombre_archivo):
 
    try:
        with open(nombre_archivo,'r') as historia:
            lineas = historia.readlines()
            return len(lineas)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
        return 0
    
resultado = contar_lineas("story.txt")
print(f"El archivo tiene {resultado} líneas.")

print('-------------EJERCICIO 3 - Contar palabras de archivo---------------------')

def contar_palabras(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as documento:
            contenido = documento.read()
            palabras = contenido.split()
            return len(palabras)
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
        return 0

resultado = contar_palabras("story.txt")
print(f"El archivo tiene {resultado} palabras.")

print('-------------EJERCICIO 4 - Mostrar frecuencia de aparición de una palabra------------------------')

def buscar(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as documento:
            numero_linea = 1
            total = 0

            for linea in documento: 
                apariciones = linea.count("el")
                if apariciones > 0:
                    total += apariciones

                numero_linea += 1

            print(f'Total de veces que aparece "el" en todo el archivo: {total}')

    except FileNotFoundError:
        print(f'Error: El archivo "{archivo}" no existe.')
    except Exception as x:
        print(f"Se produjo un error inesperado: {x}")

buscar("notes.txt")

print('--------------EJERCICIO 5 - Mostrar cantidad de palabras en un archivo---------------------')

def display_words(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as documento:
            for linea in documento:
                palabras = linea.split()
                for palabra in palabras:
                    if len(palabra) < 4:
                        print(palabra)
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

display_words("story.txt")

print('-------------EJERCICIO 6 - Añadir separador entre palabras------------------')

try:
    with open("materia.txt", 'w', encoding='utf-8') as doc:
        doc.write("Ni se crea ni se destruye, se transforma")

except Exception as e:
        print(f"Se produjo un error al crear el archivo: {e}")

def hash_display(archivo, separador = "#"):

    try:
        with open(archivo, 'r', encoding='utf-8') as documento:
            contenido = documento.read()
            resultado = separador.join(contenido)
            print(resultado)
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

hash_display("materia.txt")

print('-----------EJERCICIO 7 - Creación de archivos------------------')

def archivos_abc():
    try:
        for letra in string.ascii_uppercase:
            nombre_archivo = f"{letra}.txt"
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                archivo.write(f"Archivo: '{letra}'.\n")
    except Exception as e:
        print(f"Se produjo un error al generar los archivos: {e}")

archivos_abc()

print('--------------EJERCICIO 8 - Añadir texto al final de un archivo------------------')

def texto(nombre_archivo, contenido_archivo):
    try:
        with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(contenido_archivo)

        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            print(archivo.read())

    except Exception as e:
        print(f"Se produjo un error: {e}")

texto("prueba.txt", "comen trigo en un trigal")

print('----------------EJERCICIO 9 - Conteo frecuencia palabras-----------------')

def frecuencia_palabra(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as documento:
            contenido = documento.read().lower()
            palabras = contenido.split()
            frecuencia = Counter(palabras)

            for palabra, conteo in frecuencia.most_common():
                print(f"{palabra}: {conteo}")

    except FileNotFoundError:
        print(f'Error: El archivo "{archivo}" no existe.')
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

frecuencia_palabra("notes.txt")

print('---------------EJERCICIO 10 - Verificar existencia de un archivo----------------')

def verificar(archivo):
    if os.path.isfile(archivo):
        print(f"El archivo '{archivo}' existe.")
    else:
        print(f"El archivo '{archivo}' no existe.")

verificar("notes.txt")

print('--------------DOCUMENTO PARA EJERCICIOS-------------------------')
df = pd.read_csv('C:\\Users\\Usuario\\Desktop\\Python\\csvAutomobile_data.csv', sep=',', index_col=False)

print('----------EJERCICIO T2.1 - Mostrar cinco primeras y cinco últimas filas------------------')

print(df.head())
print(df.tail())

print('----------EJERCICIO T2.2 - Limpiar datos, actualizar y reemplazar valores NaN------------------')

df.replace({'?':None,'NaN':None,'n.a':None}, inplace=True)
df.to_csv('csvAutomobile_data.csv', index=False)

print('----------EJERCICIO T2.3 - Buscar empresa coche más caro----------------')

if 'price' in df.columns:
    max_valor = df.loc[df['price'].idxmax()]
    max_marca = max_valor['company']
    max_precio = max_valor['price']
    print(f'Brand: {max_marca} \nPrice: {max_precio} €')
else:
    print('Not found')

print('---------EJERCICIO T2.4 - Datos Toyota------------------------------')

if 'company' in df.columns:
    toyota = df[df['company'].str.lower() == 'toyota']
    print(toyota)
    
else:
    print("Not found")

print('--------EJERCICIO T2.5 - Coches por empresa-----------------------------------')

if 'company' in df.columns:
    total = df['company'].value_counts()
    print(f"Coche por empresa: {total}")

else:
    print("Not found")

print('--------------EJERCICIO T2.6 - Precio más alto de cada empresa---------------------')

if 'company' in df.columns and 'price' in df.columns:
    precio_coche = df.loc[df.groupby('company')['price'].idxmax(),['company','price']]
    print(f"Coche más caro x empresa: {precio_coche}")

else:
    print("Error")

print('-------------EJERCICIO T2.7 - Kilometraje medio x empresa--------------------------')

if 'company' in df.columns and 'average-mileage' in df.columns:
    media_km = df.groupby('company')['average-mileage'].mean()
    media_km = media_km.sort_values(ascending=False)
    print(f"Media de kilometraje: {media_km.to_string()}")

else:
    print("Error")

print('--------------EJERCICIO T2.8 - Orden por precio-----------------------')

if 'price' in df.columns:
    orden = df.sort_values(by ='price',ascending=False)
    print(f"Orden por precio: {orden}")

else:
    print("Error")

print('----------------EJERCICIO T2.9 - Combinar dos dataframe-----------------------------')

german_cars = {'Company': ['Ford','Mercedes','BMW','Audi'], 'Price':[23845,171995,135925,71400]}
japanese_cars = {'Company': ['Toyota','Honda','Nissan','Mitsubishi'], 'Price':[29995,23600,61500,58980]}

df_german = pd.DataFrame(german_cars)
df_japan = pd.DataFrame(japanese_cars)

data_concatenada = pd.concat([df_german,df_japan], ignore_index=True)

print(f"Info unida: {data_concatenada}")

print('------------EJERCICIO T2.10 - Combinar dos dataframe-----------------------')
 
car_price = {'Company': ['Toyota','Honda','BMW','Audi'], 'Price':[23845,171995,135925,71400]}
car_horsepower = {'Company': ['Ford','Honda','BMW','Audi'], 'horsepower':[141,80,182,160]}

df_precio = pd.DataFrame(car_price)
df_horsepower = pd.DataFrame(car_horsepower)

df_combinado = pd.merge(df_precio,df_horsepower, on='Company', how='inner')

print(df_combinado)

print('-----------------EJERCICIO T3.1 - Array-----------------------------')

array = np.array([[1,2],[3,4],[5,6],[7,8]], dtype=np.uint16)
shape = array.shape
dimensiones = array.ndim
size = array.itemsize

print(shape,dimensiones,size)

print('----------------EJERCICIO T3.2 - Matriz de enteros-----------------------')

matrix = np.arange(100,200,10).reshape(5,2)

print(matrix)

print('------------EJERCICIO T3.3 - Array numpy--------------------------------')

sample_array = np.array ([[11,22,33],[44,55,66],[77,88,99]])
print(sample_array[:,2])

print('-------------EJERCICIO T3.4 - Array filas impares y columnas pares-------------------------')

sample_array = np.array([[3,6,9,12],[15,18,21,24],[27,30,33,36],[39,42,45,48],[51,54,57,60]])
print(sample_array[1::2,0::2])

print('------------EJERCICIO T3.5 - Matriz sumando dos matrices numPy-----------------------')

array_one = np.array([[5,6,9],[21,18,27]])
array_two = np.array([[15,33,24],[4,7,1]])

array_result = array_one + array_two
print(array_result**2)

print('-------------EJERCICIO T3.6 - Dividir la matriz en cuatro submatrices---------------------')

matriz = np.arange(10,34).reshape(8,3)
submatriz = np.vsplit(matriz,4)

for i, sub in enumerate(submatriz):
    print(sub)

print('-------------EJERCICIO T3.7 - Ordenar array--------------------------')

sample_array = np.array([[34,43,73],[82,22,12],[53,94,66]])
array_caso1 = np.argsort(sample_array[1])
caso1 = sample_array[:,array_caso1]
array_caso2 = np.argsort(sample_array[:,1])
caso2 = sample_array[array_caso2, :]

print(f"Caso1: {caso1} \n"
      f"Caso2: {caso2}")

print('-------------EJERCICIO T3.8 - Máximo del eje 0 y mínimo del eje 1------------------------------------')

sample_array = np.array([[34,43,73],[82,22,12],[53,94,66]])

eje0 = np.max(sample_array,axis=0)
eje1 = np.min(sample_array,axis=1)

print(eje0,eje1)

print('--------------EJERCICIO T3.9 - Eliminar columna e insertar nueva--------------------')

sample_array = np.array([[34,43,73],[82,22,12],[53,94,66]])
new_column = np.array([10,10,10]).reshape(-1,1)

array_drop = np.delete(sample_array,1,axis=1)
new_array = np.hstack((array_drop,new_column))

print(new_array)

print('--------------DOCUMENTO PARA EJERCICIOS-------------------------')
df = pd.read_csv('C:\\Users\\Usuario\\Desktop\\Python\\comp_data.csv', sep=',', index_col=False)

print('--------------EJERCICIO T4.1 - Leer beneficio company sales-------------------------')

meses = df["month_number"]
beneficio = df ["total_profit"]

plt.figure(figsize=(12,5))
plt.plot(meses,beneficio)
plt.xlabel("Número del mes") 
plt.ylabel("Beneficio total")
plt.title ("Beneficios por mes")
plt.xticks(meses)

plt.show()

print('------------------EJERCICIO T4.2 - Personalizar gráfico----------------------------------')

plt.plot(meses, beneficio, label="Profit data of last year",linestyle='--', linewidth=3, color='r',marker='o', mfc='k')
plt.legend(loc="lower right")

plt.show()

print('----------------EJERCICIO T4.3 - Ventas de productos en gráficos----------------------')

meses = df["month_number"]
unidades = df.columns[1:7]

plt.figure(figsize=(12,6))

for producto in unidades:
    plt.plot(meses, df[producto], label= f"{producto} Sales Data", marker='o')

plt.xlabel("Número mes") 
plt.ylabel("Unidad de ventas en numero")
plt.title("Ventas")
plt.xticks(meses)
plt.legend(loc="upper left")

plt.show()

print('----------------EJERCICIO T4.4 - Scatter pasta de dientes------------------------')

meses = df["month_number"]
dientes = df["toothpaste"]

plt.figure(figsize=(12,6))

plt.xlabel("Número del mes") 
plt.ylabel("Numero de unidades vendidas")
plt.title("Ventas pasta de dientes")
plt.xticks(meses)
plt.grid(True,linestyle='--',linewidth=1.5)
plt.scatter(meses,dientes,label="Ventas de pasta de dientes")
plt.legend(loc="upper left")

plt.show()

print('----------EJERCICIO T4.5 - Barras ventas crema y limpiador------------------------------')

meses = df["month_number"]
df.rename(columns={"facecream":"crema facial","facewash":"limpiador facial"},inplace=True)
facial = df.columns[1:3]
ancho = 0.4

plt.figure(figsize=(12,6))

plt.xlabel("Número del mes") 
plt.ylabel("Unidades de ventas en numero")
plt.title("Facewash and facecream sales data")

for i,producto in enumerate(facial):
    plt.bar(meses+i * ancho, df[producto], width=ancho, label= f"Ventas {producto}")

plt.xticks(meses)
plt.grid(True,linestyle='--',linewidth=1)
plt.legend(loc="upper left")

plt.show()

print('--------------EJERCICIO T4.6 - Barras jabón de baño-----------------------------')

meses = df["month_number"]
jabon = df["bathingsoap"] 
df.rename(columns={"bathingsoap":"jabón de baño"},inplace=True)

plt.figure(figsize=(12,6))

plt.xlabel("Número del mes") 
plt.ylabel("Unidades de ventas en numero")
plt.title("Ventas jabón de baño")

plt.bar(meses, jabon)
plt.xticks(meses)
plt.grid(True,linestyle='--',linewidth=1)

plt.savefig("C:/Users/Usuario/Desktop/Python/grafico_jabon.pdf")
plt.show()

print('------------------EJERCICIO T4.7 - Histograma beneficios---------------------------')

beneficio = df["total_profit"]

plt.figure(figsize=(12,6))
plt.hist(beneficio, range = (150000, 450000), bins = 12, label = "Profit" )

plt.xlabel("Profit en dolares") 
plt.ylabel("Frecuencia")
plt.title("Profit")

plt.show()

print('--------------EJERCICIO T4.8 - Pie ventas totales---------------------------')

year = df['month_number'].max()
df.rename(columns={"facecream":"Crema facial",
                   "facewash":"Limpiador facial",
                   "bathingsoap":"Gel de baño",
                   "toothpaste":"Pasta de dientes",
                   "shampoo":"Champú",
                   "moisturizer":"Hidratante"},inplace=True)
ventas_year = df[df['month_number']==year]
productos = ventas_year.columns[1:7]
ventas_totales = ventas_year[productos].sum()

plt.figure(figsize=(10,10))
plt.title("Sales data")
plt.pie(ventas_totales,labels = productos, autopct='%1.1f%%', startangle=90)
plt.legend(loc="lower right")

plt.show()

print('--------------EJERCICIO T4.9 - Subplot jabón --------------------------------')

meses = df["month_number"]
jabon = df["bathingsoap"] 
limpiador = df["facewash"]

plt.subplot(2,1,1)
plt.plot(meses,jabon,color='k',marker='o',linewidth=3)
plt.title("Ventas gel de baño")
plt.xticks([])
plt.yticks([7500,10000,12500])

plt.subplot(2,1,2)
plt.plot(meses,limpiador,color='r',marker='o',linewidth=3)
plt.xlabel("Numero del mes")
plt.title("Ventas limpiador facial")
plt.xticks(meses)
plt.yticks([1500,2000])

plt.show()

print('------------------EJERCICIO T4.10 - Diagrama pila ventas ----------------------------')

meses = df["month_number"]
df.rename(columns={"facecream":"Crema facial",
                   "facewash":"Limpiador facial",
                   "bathingsoap":"Gel de baño",
                   "toothpaste":"Pasta de dientes",
                   "shampoo":"Champú",
                   "moisturizer":"Hidratante"},inplace=True)
unidades = df.columns[1:7]
ventas = df[unidades].values.T
colores = ['m','b','r','k','g','y']

plt.figure(figsize=(12,6))

plt.stackplot(meses, ventas, labels=unidades, colors=colores)

plt.xlabel("Numero del mes")
plt.ylabel("Unidades de ventas en numero")
plt.title("Todas las ventas de productos en un stack plot")

plt.legend(loc="upper left")

plt.show()
