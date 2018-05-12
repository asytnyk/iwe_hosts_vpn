FROM python:3.6-alpine
RUN apk add --no-cache openvpn

COPY bin/client_connect.py /usr/local/bin/
RUN chmod +x /usr/local/bin/client_connect.py

COPY bin/requirements.txt /tmp
RUN cd /usr/local/bin && python -m venv venv
RUN cd /usr/local/bin && venv/bin/pip install -r /tmp/requirements.txt

COPY boot.sh /usr/local/bin/boot.sh
RUN chmod +x /usr/local/bin/boot.sh

WORKDIR /etc/openvpn
COPY cert cert
COPY conf conf
RUN chmod 600 cert/beta.iwe.cloud.key cert/ta.key

EXPOSE 1194

ENTRYPOINT ["/usr/local/bin/boot.sh"]
