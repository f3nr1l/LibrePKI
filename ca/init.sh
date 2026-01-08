#!/bin/sh
# Initialiser la CA
cfssl gencert -initca config.json | cfssljson -bare ca
# Démarrer CFSSL en mode API
cfssl serve -address=0.0.0.0 -port=8888
