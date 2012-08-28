#!/usr/bin/env python

'''
Creado el 09/12/2011

@author: Carlos Garcia

Scripts en python que permite hacer un respaldo de una base de datos
que reside en PostgreSql, para ejecutar este archivo es necesario
que se configure los parametros en el archivo respaldo_pg.conf

Este archivo se ejecuta de la siguiente manera:
$ python respaldo_postgresql.py

'''

import datetime
import os
import sys
from rutinas.varias import *

ruta = os.path.dirname(sys.argv[0])
archivo = os.path.join(ruta, 'respaldo_pg.conf')
fc = FileConfig(archivo)

os.environ['PGPASSWORD'] = 'shc21152115'


def respaldo_pg():
    '''
     Metodo que permite realizar el respaldo  a una base de datos de postgresql
    '''

    valores = fc.opcion_consultar('POSTGRESQL')

    ipservidor = valores[0][1]
    nombrebasedatos = valores[1][1]
    usuariobasedatos = valores[2][1]
    rutarespaldo = valores[3][1]
    nombrearchivo = valores[4][1]

    t = datetime.datetime.now()
    fecha_dia = t.strftime('%d_')

    archivofinal = os.path.join(rutarespaldo, nombrearchivo + fecha_dia + '.sql')
    comando = 'pg_dump'

    comando_a_ejecutar = '%s -Fc -b -h %s %s -U %s > "%s"' % \
        (comando, ipservidor, nombrebasedatos, usuariobasedatos, archivofinal)
    return comando_a_ejecutar

if __name__ == '__main__':
    print 'Espere un momento ejecutando Proceso de Respaldo...'
    respaldar = respaldo_pg()
    print respaldar
    os.system(respaldar)
    print '*** Respaldo Realizado con Exito ***'
