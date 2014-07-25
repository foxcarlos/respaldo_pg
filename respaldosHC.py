# -*- coding: utf-8 *-*

import os
import datetime
import sys
import subprocess

'''RemoteUser = 'usuario'
RemoteHost = '192.168.1.52'
RemotePort = '22'
RemoteDir = '/home/backups/'

import os
import re
import sys
import time
import commands

# Carpetas que queremos copiar..
Syncs = ['/etc', '/var/www', '/var/lib/mysql', '/var/spool/cron/crontabs']

print '\nRemote Backup\n'

for Sync in Syncs:
    print "Sync: " + Sync
    SyncCmd = 'rsync -e "/usr/bin/ssh -p' + RemotePort + '" -a --progress --stats --delete -l -z -v -r -p ' + Sync + ' ' + RemoteUser + '@' + RemoteHost + ':' + RemoteDir
        [status,output]=commands.getstatusoutput(SyncCmd)
    print SyncCmd'''

'''def sinc():
    zip_Hc2 = "zip -r /media/serv_resp_hc2/HC22.zip  /media/publico/hc2"
    tarGz_ServCoromoto = "tar -zcvf /media/serv_resp_noche/SHC22NOCHE.tar.gz  /media/serv_coromoto"
    tar_Hc2 = "tar -zcvf /media/serv_resp_hc2/HC22.tar.gz  /media/publico/hc2"

    sincronizar = 'rsync -avz --no-whole-file --delete /media/serv_coromoto/ /home/cgarcia/sync/'
    os.system(sincronizar)'''

def serv_resp_tarde():
    '''Respaldo de Serv_Coromoto en Serv_Resp_Tarde
    Se Ejecuta todos los dias a las 5pm y debe tener el formato
    siguiente:SHCDDTARDE.ZIP'''

    fecha = datetime.datetime.now()
    dia = fecha.strftime('%d')
    archivoZipNombre = 'SHC{0}TARDE.zip'.format(dia)
    rutaDesde = '/media/serv_coromoto'
    rutaHasta = '/media/serv_resp_tarde/'
    rutaArchivoZipNombre = os.path.join(rutaHasta, archivoZipNombre)
    
    comandoLinux = 'zip -r {0} {1}'.format(rutaArchivoZipNombre, rutaDesde)
    return comandoLinux

def serv_resp_noche():
    '''Respaldo de Serv_Coromoto en Serv_Resp_Noche
    Se Ejecuta todos los dias a las 5am y debe tener el formato
    siguiente:SHCDDNOCHE.ZIP'''

    fecha = datetime.datetime.now()
    dia = fecha.strftime('%d')
    archivoZipNombre = 'SHC{0}NOCHE.zip'.format(dia)
    rutaDesde = '/media/serv_coromoto'
    rutaHasta = '/media/serv_resp_noche/'
    rutaArchivoZipNombre = os.path.join(rutaHasta, archivoZipNombre)
    
    comandoLinux = 'zip -r {0} {1}'.format(rutaArchivoZipNombre, rutaDesde)
    return comandoLinux

def serv_resp_hc2():
    '''Respaldo de Serv_Coromoto en Serv_Resp_Tarde
    Se Ejecuta todos los dias a las 5pm y debe tener el formato
    siguiente:SHCDDTARDE.ZIP'''

    fecha = datetime.datetime.now()
    dia = fecha.strftime('%d')
    archivoZipNombre = 'HC-{0}.zip'.format(dia)
    rutaDesde = '/media/publico/hc2'
    rutaHasta = '/media/serv_resp_hc2/'
    rutaArchivoZipNombre = os.path.join(rutaHasta, archivoZipNombre)
    
    comandoLinux = 'zip -r {0} {1}'.format(rutaArchivoZipNombre, rutaDesde)
    return comandoLinux

def respaldomensual():
    '''Respaldo de Serv_Coromoto en RespaldoMensual dentro de 
    Serv_Resp_Tarde Se Ejecuta todos los dias 1 de cada mes las 5pm 
    y debe tener el formato siguiente:MM-HCDDNOCHE.ZIP'''

    fecha = datetime.datetime.now()
    dia = fecha.strftime('%d')

    if dia == '01':
        mes = fecha.strftime('%m')
        
        archivoZipNombre = '{0}-SHC{0}NOCHE.zip'.format(mes, dia)
        rutaDesde = '/media/serv_coromoto'
        rutaHasta = '/media/serv_resp_tarde/respaldomensual'
        rutaArchivoZipNombre = os.path.join(rutaHasta, archivoZipNombre)
        
        comandoLinux = 'zip -r {0} {1}'.format(rutaArchivoZipNombre, rutaDesde)
        return comandoLinux

if __name__ == '__main__':
    parametroPasado = sys.argv[1]
    print('Parametro pasado desde crontab', parametroPasado, datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    
    if parametroPasado == 'TARDE':
        devuelto = serv_resp_tarde()
        print(devuelto, datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        comando = subprocess.Popen(devuelto.split(), stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    elif parametroPasado == 'NOCHE':
        devuelto = serv_resp_noche()

    elif parametroPasado == 'HC2':
        devuelto = serv_resp_hc2()

    elif parametroPasado == 'MENSUAL':
        devuelto = respaldomensual()

    elif parametroPasado == 'PRUEBA':
        devuelto = 'zip -r /home/cgarcia/prueba/aComprimido.zip /home/cgarcia/prueba/a'
        print(devuelto, datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        comando = subprocess.Popen(devuelto.split(), stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        #print(comando.stdout.read())

