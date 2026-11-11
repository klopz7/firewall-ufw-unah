#!/bin/bash

DIR="/home/klopz/seguridad/bloqueo-uth"
ARCHIVO="$DIR/ips.txt"

if [[ $EUID -ne 0 ]]; then
    echo "Ejecuta este script como root"
    exit 1
fi

if [[ ! -f "$ARCHIVO" ]]; then
    echo "No se encontró el archivo: $ARCHIVO"
    exit 1
fi

while IFS= read -r ip; do
    [[ -z "$ip" ]] && continue

    echo "Desbloqueando IP: $ip"
    ufw --force delete deny out to "$ip" port 80 proto tcp
    ufw --force delete deny out to "$ip" port 443 proto tcp
    ufw --force delete deny out to "$ip" port 443 proto udp
done < "$ARCHIVO"

echo
ufw status numbered
