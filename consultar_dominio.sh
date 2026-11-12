#!/bin/bash
sitio1="$1"
sitio2="$2"
for dominio in "$sitio1" "$sitio2"; do
	echo "----$dominio----"
	echo "IPV4"
	dig +short "$dominio" A
	echo "IPV6"
	dig +short "$dominio" AAAA
done > /home/klopz/seguridad/listarip_dominio.txt

