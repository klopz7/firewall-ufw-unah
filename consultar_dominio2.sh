#!/bin/bash
for dominio in usap.hn www.usap.hn; do
	echo "----$dominio----"
	echo "IPV4"
	dig +short "$dominio" A
	echo "IPV6"
	dig +short "$dominio" AAAA
done

