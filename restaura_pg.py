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

import os
import sys
from rutinas.varias import *


ruta = os.path.dirname(sys.argv[0])
archivo = os.path.join(ruta, 'respaldo_pg.conf')
fc = FileConfig(archivo)


def restaura(fecha_a_restaurar):
    '''
    string fecha
    '''

    ipservidor, nombrebasedatos, usuariobasedatos,\
    rutarespaldo, nombrearchivo, clave = \
            fc.opcion_consultar('POSTGRESQL')
    nombre_archivo =  nombrearchivo + fecha_a_restaurar + '_.sql' 
    ruta_y_archivo = os.path.join(rutarespaldo,nombre_archivo)
    #comando = 'pg_restore -d %s -U %s ' % (nombrebasededatos, usuariobasededatos, nombre_archivo)
    #pg_restore -i -h localhost -p 5432 -U postgres -d mibase -v "/home/damian/backups/mibase.backup"
    comando_a_ejecutar = 'pg_restore -i -h %s -U %s -d %s -v %s ' % (ipservidor, usuariobasedatos, nombrebasedatos, nombre_y_archivo)
    print comando_a_ejecutar

if __name__ == '__main__':
    restaura('23')
