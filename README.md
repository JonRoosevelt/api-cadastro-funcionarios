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
