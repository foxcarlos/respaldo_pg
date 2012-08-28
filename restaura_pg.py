#!/usr/bin/env python

'''
Creado el 23/08/2012
@author: Carlos Garcia


Scripts en python que permite restaurar el respaldo de una base de datos
de PostgreSql Este archivo se ejecuta de la siguiente manera:
$ python restaura_pg.py

Para Restaurar la Base de Datos:
-d Nombre Base Datos
-U Usuario

pg_restore -d db -U postgres db.sql
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

os.environ['PGPASSWORD'] = clave[1]


def restaura(fecha_a_restaurar):
    '''
    string fecha
    '''
    nombre_archivo = nombrearchivo[1] + fecha_a_restaurar + '_.sql'
    ruta_y_archivo = os.path.join(rutarespaldo[1], nombre_archivo)
    #pg_restore -i -h localhost -p 5432 -U postgres -d mibase -v "/home/fox/backups/mibase.sql"

    eliminar_bd =   'dropdb  -h %s -p %s -U %s  %s' %\
            (ipservidor[1], puerto[1], usuariobasedatos[1], nombrebasedatos[1])

    #crear_bd = 'createdb -E UTF8 -O admhc -h 10.121.3.31 -p 5434 -U admhc nombrebasedatos'
    crear_bd = 'createdb -O %s -h %s -p %s -U %s %s' %\
            (usuariobasedatos[1], ipservidor[1], puerto[1], usuariobasedatos[1], nombrebasedatos[1])

    restaurar_bd = 'pg_restore -i -h %s -p %s -U %s -d %s -v "%s" ' %\
            (ipservidor[1], puerto[1], usuariobasedatos[1], nombrebasedatos[1], ruta_y_archivo)
    
    try:
        print eliminar_bd
        #os.system(eliminar_bd)
        print crear_bd
        print restaurar_bd
        #os.system(restaurar_bd)
    except:
        print "Ocurrio un error al momento de Restaurar la Base de datos"


if __name__ == '__main__':
    restaura(str(datetime.date.today().day))
    os.system('unset PGPASSWORD')
