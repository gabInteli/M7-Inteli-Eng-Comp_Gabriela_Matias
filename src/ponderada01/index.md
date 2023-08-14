# Criação de um Repositório no Docker Hub para o Container FastAPI

Este guia irá explicar o processo de criação de um repositório no Docker Hub contendo o seu container de FastAPI com o servidor que exibe o seu currículo.

## Tecnologias Utilizadas

A seguir estão as principais tecnologias utilizadas neste projeto:

### [FastAPI](https://fastapi.tiangolo.com/)

<img src="https://cdn.worldvectorlogo.com/logos/fastapi-1.svg" style="width:10%"/>

FastAPI é um framework moderno e de alto desempenho para construção de APIs com Python 3. É utilizado para criar o servidor que exibe o seu currículo.

### [Docker](https://www.docker.com/)

<img src="https://cdn-icons-png.flaticon.com/512/919/919853.png" style="width:10%"/>

Docker é uma plataforma de contêiner que permite empacotar, distribuir e executar aplicativos em ambientes isolados. Utilizamos o Docker para criar e distribuir o contêiner do FastAPI.

## Passo a Passo

### Passo 0: Criar um Server com FastAPI Servindo o HTML do Currículo

1. Criar um arquivo `main.py` contendo a estrutura da rota a ser direcionada para o nosso index.html que contem o currículo.  

2. Acionar o server por meio do comando: 

    `python -m uvicorn main:app --reload`

### Passo 1: Construir o Container

1. Crie um arquivo `Dockerfile` na raiz do seu projeto contendo as instruções para construir o seu container.

   ```Dockerfile
   # imagem base
        FROM python:3.11
    # diretório da imagem que vamos trabalhar
        WORKDIR /code

    # definição dos requirements 
        COPY ./requirements.txt /code/requirements.txt

        RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
    #
        COPY . /code

    #Definição de acesso ao server
        CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]```

O Dockfile pode ser acessado nos arquivos desse repositório. 

2. Construção do Container: 
Foi executado o seguinte comando para construir o seu container:

    ```docker build -t nome-de-seu-container```

### Passo 2: Criar um Repositório no Docker Hub
No Docker Hub foi criado um repositório pulico onde posteriormente foi armazenado nosso container. 

### Passo 3: Fazer o Push para o Docker Hub
O container foi setado com a tag com o nome do repositório no Docker Hub:

```
    docker tag gabInteli/curriculo-gab
```

Em seguida foi feito o push do do container para o Docker Hub:

```
    docker push gabInteli/curriculo-gab
```

### Passo 4: Usar o Container do Docker Hub
A partir disso é possível executar o container em qualquer máquina que tenha o Docker instalado:

```
docker run -p 4000:80 gabInteli/curriculo-gab
```
Assim é possível acessar o server com FastAPI no navegador em http://localhost:4000.



