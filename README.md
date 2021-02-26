# Flask Simple

Prueba de concepto de un servicio con Flask consumiendo un Stored Procedure de Oracle

## Requisitos

1. Docker
1. Flask 1.1.1
2. Python 3.6


## Ejecutar proyecto

### En Docker
En la raiz ejecutar los siguientes comandos:

```shell
docker build -t flask_oracle:0.1 -f Dockerfile .
docker run -p 5002:5002 flask_oracle:0.1
```

### Local
En la raiz ejecutar los siguientes comandos:

```shell
python3 web/app.py 
```


## Ejecutar la prueba unitaria


Ejecutar el siguiente Curl:
```shell
curl --location --request GET 'http://localhost:5002/'
```