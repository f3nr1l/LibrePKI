FROM alpine:latest
RUN apk add --no-cache cfssl
WORKDIR /ca
COPY config.json init.sh /ca/
RUN chmod +x init.sh
ENTRYPOINT ["./init.sh"]
