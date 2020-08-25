# Navedex Api 👽️

Instalação 🚀️
---

* Crie um ambiente virtual com python3
    * [pyenv](https://github.com/pyenv/pyenv)
    ou
    * [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html)


* Clone o repositório dentro do ambiente virtual
```shell=
$ git clone git@github.com:JonRoosevelt/navedex-api.git
```
* Entre na pasta e instale os requisitos
```shell=
pip install -r requirements.txt
```
* Será necessário ter uma instancia do postgres instalada e rodando na sua máquina.
    * Edite o arquivo `settings.py` a partir da linha 109 e coloque suas credenciais do banco
    ```python=109
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '<nome_da_database>',
            'USER': '<usuario_do_postgres>',
            'PASSWORD': '<senha_do_posgres>',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    ```
    
* Crie as migrations e aplique-as:
    ```shell=
    python manage.py makemigrations
    python manage.py migrate
    ```
* Rode os testes 👨‍🔬️
    ```shell=
    python manage.py test
    ```
* Link da documentação (Postman)
[Documentação Api](https://documenter.getpostman.com/view/1528220/TVCY6CAB)

* Link do Roadmap do processo
[Roadmap](https://www.notion.so/5a4280f7dd854da39d65d5720734e48d?v=a84951d8db63471e936b0a81dcbe7f28)

***
Dificuldades
---

* Logo no início do projeto, acabei vacilando e adicionei um import do unittest.testcases.TestCase no lugar do django.test.testcases.TestCase, que me causou vários problemas e muitos dias agarrado, até que percebi o meu erro 🤦‍♂️️
* Embora trabalhe diriamente com python/django/drf, alguns processos não são feitos por todos os devs da empresa, então estava desacostumado com algumas coisas e outras nunca havia feito, como a própria autenticação com token jwt. 
* Falando em JWT, acho que os testes dele foram um ponto baixo. Não fiquei satisfeito, mas acabei tendo de subir assim mesmo.
* Tive dificuldade em criar a documentação com insomnia, que é o client http que costumo utilizar, então fiz no próprio Postman, que acabou ficando melhor.
* Num ultimo momento, estava verificando e acredito que a relação entre os navers e os projetos não está funcionando totalmente, no endpoint de STORE ou UPDATE dos projetos. Só peguei este problema agora na geração da documentação ao testar pelo postman.

Considerações Finais
---
De maneira geral, fiquei satisfeito com o desafio, foram 4 desses 10 dias de 12, 13 horas seguidas (fins de semana), com mais algumas horas durante a semana.
Acho que consegui fazer bastante testes e explorar o DRF.
Foi legal ter conseguido fazer a autenticação em JWT também.
Aguardo o feedback!!!
