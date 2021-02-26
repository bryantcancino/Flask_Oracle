# Flask Simple

Prueba de concepto de un servicio con Flask

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
#docker exec -i -t 15b0b5cd93c3 /bin/bash
```

### Local
En la raiz ejecutar los siguientes comandos:

```shell
python3 /web/app.py 
```


## Ejecutar la prueba unitaria


Traer los productos ejecutando el siguiente Curl:
```shell
curl --location --request GET 'http://localhost:5001/products' \
--header 'Content-Type: application/json'
```

Nuevo producto:
```shell
curl --location --request POST 'http://localhost:5001/products' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "lavadora",
    "price": "120"
}'
```

Traer el producto lavadora:
```shell
curl --location --request GET 'http://localhost:5001/products/lavadora' \
--header 'Content-Type: application/json'
```

Traer el producto lavadora:
```shell
curl --location --request GET 'http://localhost:5001/products/lavadora' \
--header 'Content-Type: application/json'
```


Modificar el producto lavadora:
```shell
curl --location --request PUT 'http://localhost:5001/products/lavadora' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "lavadora",
    "price": "10",
    "quantity": 4
}'
```

Eliminar el producto lavadora:
```shell
curl --location --request DELETE 'http://localhost:5001/products/lavadora' \
--header 'Content-Type: application/json'
```# Flask_Simple
