FROM alpine:latest

# Installer les dépendances nécessaires
RUN apk add --no-cache wget tar

# Télécharger et installer CFSSL
RUN wget -q -O /usr/local/bin/cfssl https://github.com/cloudflare/cfssl/releases/download/v1.6.4/cfssl_1.6.4_linux_amd64 \
    && wget -q -O /usr/local/bin/cfssljson https://github.com/cloudflare/cfssl/releases/download/v1.6.4/cfssljson_1.6.4_linux_amd64 \
    && chmod +x /usr/local/bin/cfssl /usr/local/bin/cfssljson

WORKDIR /ca
COPY config.json init.sh /ca/
RUN chmod +x init.sh

ENTRYPOINT ["./init.sh"]
