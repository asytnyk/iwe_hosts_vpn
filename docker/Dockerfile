FROM python:3.6-alpine
RUN apk add --no-cache openvpn

WORKDIR /etc/openvpn
COPY cert cert
COPY conf conf

COPY bin/client_connect.py bin/
RUN chmod +x bin/client_connect.py

COPY bin/requirements.txt bin/
RUN cd bin && python -m venv venv
RUN cd bin && venv/bin/pip install -r requirements.txt

COPY boot.sh /usr/local/bin/boot.sh
RUN chmod +x /usr/local/bin/boot.sh

EXPOSE 1194

ENTRYPOINT ["/usr/local/bin/boot.sh"]
