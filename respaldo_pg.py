#!/usr/bin/env python

'''
Creado el 09/12/2011

@author: Carlos Garcia

Scripts en python que permite hacer un respaldo de una base de datos  que
reside en PostgreSql Este archivo se ejecuta de la siguiente manera:
$ python respaldo_postgresql.py

Para Restaurar la Base de Datos:
-d Nombre Base Datos
-U Usuario

pg_restore -d db -U postgres db.tar
'''

import time
import datetime
import os
import sys
from rutinas.varias import *

ruta = os.path.dirname(sys.argv[0])
archivo = os.path.join(ruta, 'respaldo_pg.conf')
fc = FileConfig(archivo)


def nombre_archivo():
    '''
    Permite Crear el nombre del archivo que tendra el respaldo
    tomando como nombre la fecha dd-mm-aa y la hora hh:mm:ss
    Quedando de la siguiente manera suponiendo que fue realizado
    en la siguiente fecha (24/12/2011 10:30:00) , el resultado seria
    el siguiente: 24_12_2011_103000

    t = time.localtime()
    dia = t.tm_mday
    mes = t.tm_mon
    ano = t.tm_year

    hora = t.tm_hour
    minutos = t.tm_min
    seg = t.tm_sec

    nombre = '%s-%s-%s_%s:%s:%s' % (dia, mes, ano, hora, minutos, seg)
    '''

    t = datetime.datetime.now()
    #nombre = t.strftime('%d_%m_%Y_%I%M%S')
    nombre = t.strftime('%d_')

    return nombre


def respaldo_pg():
    '''
    Toma los parametros del diccionario con el cual se arma el nombre y
    la ruta que tendra el archivo del respaldo asi como tambien arma
    el comando final a ejecutar
    '''

    valores = fc.opcion_consultar('POSTGRESQL')
    
    ipservidor = valores[0][1]
    nombrebasedatos = valores[1][1]
    usuariobasedatos = valores[2][1]
    rutarespaldo =  valores[3][1]
    #rutarespaldo = os.path.dirname(sys.argv[0])
    nombrearchivo = valores[4][1]
   
    archivofinal = os.path.join(rutarespaldo, nombrearchivo + \
    nombre_archivo() + '.tar')
    comando = 'pg_dump'

    '''
    -Parametros a pasar(Estos tambien se pudieran colocar dentro del
    archivo config.cfg),
    - pero por ahora lo dejaremos asi directo como texto
    -Ft Significa Format tar
    -b Inclute campos Blobs
    -h es el host o la ip del servidor
    -W password
    '''
    comando_a_ejecutar = '%s -Ft -b -h %s %s -U %s -w shc21152115 > "%s"' % \
        (comando, ipservidor, nombrebasedatos, usuariobasedatos, archivofinal)
    return comando_a_ejecutar

if __name__ == '__main__':
    print 'Espere un momento ejecutando Proceso de Respaldo...'
    respaldar = respaldo_pg()
    print respaldar
    os.system(respaldar)
    print '*** Respaldo Realizado con Exito ***'

    
