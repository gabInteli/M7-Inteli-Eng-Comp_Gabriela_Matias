## Criação de um CRUD utilizando Python, Flask, SQLAlchemy e com proteção de rotas.
Esse repositório tem como objetivo apresentar a aplicação desenvolvida de CRUD com rotas protegidas e sua Dockerização.
O sistema de autenticação foi desenvolvido com base em um middleware externo criado pelo usuário [Babatunde13](https://github.com/Babatunde13) e disponibilizado no site [Loginradius](https://www.loginradius.com/blog/engineering/guest-post/securing-flask-api-with-jwt/), tendo foco no uso de JWT com uma api em Flask e então, sendo reescrito de acordo com as necessidades deste projeto. <br><br>
Aqui temos dois containers, um responsável pelo **Frontend e Backend**(sendo desenvolvido com HTML5, CSS, Flask e SQLAlchemy) e um responsável pela **Database**(feita em PostgreSQL), a imagem do Frontend e Backend pode ser encontrada dentro do Dockerfile disponibilizado no projeto, ou em nosso [Docker Hub](https://hub.docker.com/layers/joaocarazzato/modulo7/ponderada2/images/sha256-0210f70759b816154a7d1367e88c734620143e2cb9af0d45e9e79323d3e4b8c7?context=repo). Enquanto isso, a imagem utilizada para o Database é a oficial disponibilizada ao PostgreSQL, e também pode ser encontrada no [Docker Hub](https://hub.docker.com/_/postgres). 

```
|
|- src
    |
    |- static
        |
        |- style.css
        |
    |
    |- templates
        |
        |- dashboard.html
        |- index.html
        |- postpublish.html
        |- signup.html
        |
    |
    |- Dockerfile
    |- auth_middleware.py
    |- docker-compose.yml
    |- main.py
    |- requirements.txt
    |- table_creation.py
|

```

## Como executar a aplicação?
Para executarmos nossa aplicação, é muito simples. 
Primeiro, partimos do presuposto que o Docker já está instalado e funcionando, então iniciaremos a aplicação da seguinte forma:

Para iniciar a aplicação, se direcione até a pasta onde estão localizados o Dockerfile e o docker-compose:

```
@/ponderada2/entregavel/src
```

Em seguida, execute o comando:
```
docker-compose up
```

Com isso, você já terá a aplicação sendo executada, onde você poderá visualizar tanto o Frontend quanto a Database. Para visualizar o Frontend: [http://localhost:5000](http://localhost:5000), para visualizar o Database precisaremos ter o [DBeaver](https://dbeaver.io) instalado. Em seguida, precisamos realizar uma conexão com os seguintes dados de exemplo:
```
POSTGRES HOST: localhost
POSTGRES DB: postgres
POSTGRES USER: postgres
POSTGRES PASSWORD: password
```

Com isso, você já estará pronto para usar a aplicação, podendo visualizar os dados e utilizar o Frontend!

**(Para finalizar a execução da aplicação, utilize ``Control + C`` e caso queira apagá-la em seguida, utilize ``docker compose down``).**