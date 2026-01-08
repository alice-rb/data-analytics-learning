import json
from datetime import datetime

## EJERCICIO 1 ##
with open('ej1.json',encoding='utf-8') as archivo:
    datos = json.load(archivo)

libros = datos['bookstore']['book']

#1
def librosContar(libros):
    return len(libros)
#2    
def librosPrecio(libros, min, max):
    listado_libros = []
    for libro in libros:
        precio = float(libro['price'])
        if min <= precio <= max:
            listado_libros.append((libro['title']['__text'],libro['price']))
    return listado_libros
#3        
def librosTitulo (libros,string):
    listado_libros = []
    for libro in libros:
        if libro['title']['__text'].startswith(string):
            listado_libros.append((libro['title']['__text'],libro['year']))
    return listado_libros
#4        
def librosAutores (libros):
    listado = []
    for libro in libros:
        titulo = libro['title']['__text']
        autores = libro['author']
        if isinstance(autores,list):
            lista_autores = autores
        else:
            lista_autores = [autores]
        listado.append((titulo,lista_autores))
    return listado
#5
def librosCategory (libros,categoria):
    return [libro['title']['__text'] for libro in libros if libro['_category']==categoria]
#6
def librosMasAutores (libros,titulo):
    for libro in libros:
        if libro['title']['__text'] == titulo:
            autores = libro['author']
            if isinstance(autores,list):
                return autores
            else:
                return [autores]  
    return []
#7
def librosCaros(libros):
    caro = max(libros, key=lambda x:float (x['price']))
    return caro['title']['__text'], caro['price']
#8
def librosAño(libros, año):
    listado = []
    for libro in libros:
        if libro['year'] == str(año):
            listado.append(libro['title']['__text'])
    return listado
#9      
def librosMultiAutor(libros):
    titulos = []
    for libro in libros:
        if isinstance (libro['author'], list) and len(libro['author']) > 1:
            titulos.append(libro['title']['__text'])
    return titulos
#10        
def librosPrecioActualizar(libros,titulo,new_price, path='ej1.json'):
    for libro in libros:
        if libro['title']['__text'] == titulo:
            libro['price'] = str(new_price)
            with open(path,'w',encoding='utf-8') as f:
                json.dump({'bookstore': {'book': libros}}, f, indent=4)
            return True
    return False
#11
def librosEliminar(libros,titulo,path='ej1.json'):
    new_libros = [libro for libro in libros if libro['title']['__text'] != titulo]
    with open(path, 'w',encoding='utf-8') as f:
        json.dump({'bookstore':{'book': new_libros}}, f, indent=4)
    return True
#12
def librosOrdenados(libros):
    listado = []
    for libro in libros:
        listado.append((libro['title']['__text'], libro['year']))
    return sorted(listado, key=lambda x: x[1])
#13
def librosPrecioBajoPromedio(libros):
    precios = [float(libro['price']) for libro in libros]
    promedio = sum(precios) / len(precios)
    return [libro['title']['__text'] for libro in libros if float(libro['price']) < promedio], promedio

# print(librosContar(libros))
# print(librosPrecio(libros,10,50))
# print(librosTitulo(libros,'Harry'.gvgggggf))
# print(librosAutores(libros))
# print(librosCategory(libros,'WEB'))
# print(librosMasAutores(libros,'XQuery Kick Start'))
# print(librosCaros(libros))
# print(librosAño(libros,2005))
# print(librosMultiAutor(libros))
# print(librosPrecioActualizar(libros,'Harry Potter',50.90))
# print(librosEliminar(libros,'Everyday Italian'))
# print(librosOrdenados(libros))
# print(librosPrecioBajoPromedio(libros))

#-------------------------------------------------------------------------
## EJERCICIO 2 ## 
with open ('ej2.json','r',encoding='utf-8') as f:
    pruebas = json.load(f)

def fechaCorta(fecha):
    try:
        return datetime.strptime(fecha,'%Y-%m-%dT%H:%M:%S')
    except (ValueError,TypeError):
        return None
#1
def contarPruebas(pruebas):
    return len(pruebas)
#2
def pruebas2Horas(pruebas):
    listado = []
    for prueba in pruebas:
        if prueba['Horas'] > 2:
            listado.append(prueba['Titulo'])
    return listado
#3
def pruebasNoPresenciales(pruebas):
    listado = []
    for prueba in pruebas:
        tipo = prueba.get('TipoFormacion','').lower()
        if 'no' in tipo:
            listado.append(prueba.get('URL'))
    return listado
#4
def pruebaID(pruebas,id):
    for prueba in pruebas:
        if prueba['ID'] == id:
            profesores = [prof['NombreCompleto'] for prof in prueba['Profesorado']]
            return prueba['Titulo'], profesores
    return None
#5
def pruebasTitulosProfes(pruebas):
    listado = []
    for prueba in pruebas:
        profesores = [prof['NombreCompleto'] for prof in prueba['Profesorado']]
        listado.append((prueba['Titulo'],profesores))
    return listado
#6
def pruebasIniFin(pruebas):
    listado = {}
    for prueba in pruebas:
        listado[prueba['ID']] = (prueba['InicioImparticion'], prueba['FinImparticion'])
    return listado
#7
def pruebasLargas(pruebas):
    listado = []
    for prueba in pruebas:
        if prueba['Horas'] > 3 and 'Presencial' in prueba['TipoFormacion']:
            listado.append(prueba['Titulo'])
    return listado
#8
def pruebasTipo(pruebas):
    listado = {}
    for prueba in pruebas:
        tipo_actual = prueba.get('TipoFormacion').lower().replace('-',' ').strip()
        if 'no' in tipo_actual:
            tipo = 'No Presencial'
        else:
            tipo = 'Presencial'
        listado[tipo] = listado.get(tipo,0) + 1
    return listado
#9
def pruebasCortaLarga(pruebas):
    pr_corta = min(pruebas, key=lambda x: x['Horas'])
    pr_larga = max(pruebas, key=lambda x: x['Horas'])
    return (pr_corta['Titulo'], pr_corta['Horas']), (pr_larga['Titulo'], pr_larga['Horas'])
#10
def pruebasFechas(pruebas,fecha):
    try:
        if '/' in fecha:
            fecha_act = datetime.strptime(fecha, '%y/%m/%d')
        else:
            fecha_act = datetime.strptime(fecha, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Formato no válido')
    
    listado = []
    for prueba in pruebas:
        inicio = fechaCorta(prueba['InicioImparticion'])
        final = fechaCorta(prueba['FinImparticion'])
        if inicio and inicio.date() == fecha_act.date():
            listado.append(prueba['Titulo'])
        elif final and final.date() == fecha_act.date():
            listado.append(prueba['Titulo'])
    return listado
#11
def pruebasProfesorado(pruebas, palabra):
    listado = []
    for prueba in pruebas:
        for profesor in prueba['Profesorado']:
            if palabra.lower() in profesor['NombreCompleto'].lower():
                listado.append(prueba['Titulo'])
                break
    return listado
#12
def pruebasTitulo(pruebas,titulo):
    for prueba in pruebas:
        if prueba['Titulo'] == titulo:
            return prueba
    return None

# print(contarPruebas(pruebas))
# print(pruebas2Horas(pruebas))
# print(pruebasNoPresenciales(pruebas))
# print(pruebaID(pruebas,'A15050163'))
# print(pruebasTitulosProfes(pruebas))
# print(pruebasIniFin(pruebas))
# print(pruebasLargas(pruebas))
# print(pruebasTipo(pruebas))
# print(pruebasCortaLarga(pruebas))
# print(pruebasFechas(pruebas,'15/02/05'))
# print(pruebasProfesorado(pruebas,'Beatriz'))
# print(pruebasTitulo(pruebas, 'Francés - Prueba de nivel - Para cursos segundo cuatrimestre'))

#-------------------------------------------------------------------------
## EJERCICIO 3 ## 
with open ('ej3.json',encoding='utf-8') as f:
    data = json.load(f)

prov = data['lista']['provincia']

#1
def totalProvincias():
    return [p['nombre']['__cdata'] for p in prov]
#2
def totalMunicip():
    municipios = []
    for p in prov:
        local = p['localidades']['localidad']
        if isinstance(local,dict):
            municipios.append(local['__cdata'])
        else:
            municipios.extend([l['__cdata'] for l in local])
    return municipios
#3
def allProvincia():
    listado = {}
    for p in prov:
        nombre = p['nombre']['__cdata']
        local = p['localidades']['localidad']
        if isinstance(local,dict):
            listado[nombre] = 1
        else:
            listado[nombre] = len(local)
    return listado
#4
def munXProv(provincia):
    for p in prov:
        if p['nombre']['__cdata'].lower() == provincia.lower():
            local = p['localidades']['localidad']
            if isinstance(local,dict):
                return [local['__cdata']]
            return [l['__cdata'] for l in local]
    return []
#5
def provXMun(municipio):
    for p in prov:
        local = p['localidades']['localidad']
        if isinstance(local,dict):
            if local['__cdata'].lower() == municipio.lower():
                return p['nombre']['__cdata']
        else:
            for l in local:
                if l['__cdata'].lower() == municipio.lower():
                    return p['nombre']['__cdata']
    return None
#6
def provXID(ids):
    listado = {}
    for p in prov:
        if p['_id'] in ids:
            local = p['localidades']['localidad']
            if isinstance(local,dict):
                listado[p['nombre']['__cdata']] = [local['__cdata']]
            else:
                listado[p['nombre']['__cdata']] = [l['__cdata'] for l in local]
    return listado
#7
def totalInfo():
    total_p = len(prov)
    total_m = len(totalMunicip())
    return (f'Provincias totales:{ total_p}. Municipios totales: {total_m}')
#8
def provNoMun():
    listado = []
    for p in prov:
        local = p['localidades'].get('localidad')
        if not local:
            listado.append(p['nombre']['__cdata'])
    return listado
#9
def munRepetidos():
    listado = {}
    for p in prov:
        nombre_p = p['nombre']['__cdata']
        local = p['localidades']['localidad']
        if isinstance(local,dict):
            muni = local['__cdata']
            listado.setdefault(muni, []).append(nombre_p)
        else:
            for l in local:
                muni = l['__cdata']
                listado.setdefault(muni, []).append(nombre_p)
    return {m: ps for m, ps in listado.items() if len(ps) > 1}

# print(totalProvincias())
# print(totalMunicip())
# print(allProvincia())
# print(munXProv('Barcelona'))
# print(provXMun('Santa Barbara'))
# print(provXID('16'))
# print(totalInfo())
# print(provNoMun())
# print(munRepetidos())

