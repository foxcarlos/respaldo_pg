#!/usr/bin/env python

'''
Creado el 23/08/2012
@author: Carlos Garcia
twitter:@foxcarlos
email:foxcarlos@gmail.com

Scripts en python que permite restaurar el respaldo de una base de datos
de PostgreSql, al igual que el archivo respaldo_pg.py este tambien depende
del archuivo de configuracion respaldo_pg.conf el cual contiene inforamcion
acerca de los parametros necesario para poder realizar el respaldo y restore
de la Base de Datos

Este archivo se ejecuta de la siguiente manera:
$ python restaura_pg.py 28 # si se desea restaurar el respaldo del dia 28 

Si solo desea restaurar el respaldo del  dia anterior entonces se ejecuta
sin pasarle ningun parametro.
$ python restaura_pg.py

NOTA:La biblioteca "from rutinas.varias import * debe estar contenida dentro del
path de python, recuerda que es necesario que la descargues desde el repositorio
git clone https://github.com/foxcarlos/rutinas.git
'''

import datetime
import os
import sys
from rutinas.varias import *


ruta = os.path.dirname(sys.argv[0])
archivo = os.path.join(ruta, 'respaldo_pg.conf')
fc = FileConfig(archivo)

ipservidor, nombrebasedatos, usuariobasedatos,\
        rutarespaldo, nombrearchivo,\
        clave, puerto = fc.opcion_consultar('POSTGRESQL_RESPALDO')

def restaura(fecha_a_restaurar):
    '''
    string numero
    Fecha a restaurar contiene el numero del dia a restaurar
    '''
    nombre_archivo = nombrearchivo[1] + fecha_a_restaurar + '_.sql'
    ruta_y_archivo = os.path.join(rutarespaldo[1], nombre_archivo)

    #Verificamos que exista el archivo a restaurar
    if os.path.isfile(ruta_y_archivo):
        #Primero se procede a eliminar la base de datos del respaldo
        eliminar_bd = 'dropdb  -h %s -p %s -U %s  %s' %\
                (ipservidor[1], puerto[1], usuariobasedatos[1], nombrebasedatos[1])
        #Se crea nuevamente la base de datos vacia
        crear_bd = 'createdb -O %s -h %s -p %s -U %s %s' %\
        (usuariobasedatos[1], ipservidor[1], puerto[1], usuariobasedatos[1], nombrebasedatos[1])

        #Se restaura el respaldo 
        restaurar_bd = 'pg_restore -i -h %s -p %s -U %s -d %s -v "%s" ' %\
        (ipservidor[1], puerto[1], usuariobasedatos[1], nombrebasedatos[1], ruta_y_archivo)
        try:
            print eliminar_bd
            os.system(eliminar_bd)
            print crear_bd
            os.system(crear_bd)
            print restaurar_bd
            os.system(restaurar_bd)
        except:
            print "Ocurrio un error al momento de Restaurar la Base de datos"
    else:
        print 'No se encontro el archivo %s' % (ruta_y_archivo)


def main(opcion):
    '''
    Parametros recibidos 1: string numero del dia a restarurar.   
    Si no se pasa ningun parametro el toma por defecto el respaldo
    del dia anterior.
    '''
    
    if len(opcion) <= 0:
        fecha = str(datetime.date.today().day - 1) 
    else:
        fecha = opcion
    
    restaura(fecha)


if __name__ == '__main__':
    try:
        recibido = sys.argv[1]
    except:
        recibido = ''   
    
    os.environ['PGPASSWORD'] = clave[1]
    main(recibido)
    os.system('unset PGPASSWORD')
