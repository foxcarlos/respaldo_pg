respaldo_pg
===========
Pequeño pero util Script en python que permite  hacer respaldo de una base de datos de PostGreSql y Restaurar el respaldo
en otro servidor de base de datos PostGreSql.

Este Proyecto consta de 3 Archivos.
- respaldo_pg.conf
- respaldo_pg.py
- restaura_pg.py


respaldo_pg.conf:Contiene los parametros necesarios para el buen funcionamiento del script de respaldo y de restauracion
=================

[POSTGRESQL]
#La eqtiqueta POSTGRESQL contiene todo lo relacionado con el Servidor de base de Datos en Produccion
#Es decir aqui debe ir la configuracion del Servidor que deseo respaldar

ipservidor = Direccion ip del Servidor Ej: 10.121.6.4
nombrebasedatos = Nombre de la base de datos Ej: bdhcoromoto 
usuariobasedatos = Usuario cn acceso a la Base de Datos Ej: admhc
rutarespaldo = Ruta donde se almacenara el Archivo que contendra el respaldo Ej: /media/respaldo_pg
nombrearchivo = Nombre que tendra el Archivo que genera el respaldo Ej: pg_bdhcoromoto_
clavepostgresql = Clave del Servidor de base de datos Ej: carlos16
puerto = Puerto de la base de datos Ej: 5432

[POSTGRESQL_RESPALDO]
#En esta Seccion se deben colocar los los parametros necesarios donde se guardaran la restauracion  de la 
#Base de Datos de respaldo, esto solo aplica en caso de que desees ejecutar el Script restaura_pg.py

ipservidor = Direccion Ip del Sevidor de Respaldo 10.121.3.31
nombrebasedatos = Nombre de la base de datos Ej: bdhcoromoto 
usuariobasedatos = Usuario cn acceso a la Base de Datos Ej: admhc
rutarespaldo = Ruta donde se almacenara el Archivo que contendra el respaldo Ej: /media/respaldo_pg
nombrearchivo = Nombre que tendra el Archivo que genera el respaldo Ej: pg_bdhcoromoto_
clavepostgresql = Clave del Servidor de base de datos Ej: carlos16
puerto = Puerto de la base de datos Ej: 5432
