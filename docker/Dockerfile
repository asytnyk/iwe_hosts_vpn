FROM python:3.6-alpine
RUN apk add --no-cache openvpn

WORKDIR /etc/openvpn
COPY cert cert
COPY conf conf
COPY bin bin
RUN chmod +x bin/client-connect.py

COPY boot.sh /usr/local/bin/boot.sh
RUN chmod +x /usr/local/bin/boot.sh

EXPOSE 1194

ENTRYPOINT ["/usr/local/bin/boot.sh"]
