FROM python:3.6.6-slim-stretch

RUN apt-get update && apt-get install -y libaio1 wget unzip

WORKDIR /opt/oracle
RUN wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip && \
    unzip instantclient-basiclite-linuxx64.zip && rm -f instantclient-basiclite-linuxx64.zip && \
    cd /opt/oracle/instantclient* && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci && \
    echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf && ldconfig
RUN python -m pip install cx_Oracle==8.1.0

COPY requirements.txt .
RUN pip install --upgrade -r requirements.txt

COPY web web

ENTRYPOINT [ "python3.6", "./web/app.py" ]