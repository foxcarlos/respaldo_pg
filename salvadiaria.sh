#!/bin/sh

pg_dump --host 10.121.6.38 --port 5432 --username "postgres" --no-password  --format plain --inserts --verbose --file "/home/rrhh-coromoto-app/SalvasBD/rrhh-estable$(date +%d%m%Y).sql" "rrhh-estable"
#pg_dump --host 127.0.0.1 --port 5432 --username "postgres" --no-password  --format plain --inserts --verbose --file "/home/rrhh-coromoto-app/SalvasBD/rrhh-desarrollo$(date +%d%m%Y).sql" "rrhh-desarrollo"

