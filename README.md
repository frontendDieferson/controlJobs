# Control| Jobs
<p align="center">Aplicação com Python e Django para controle de Jobs</p>

Aplicação para contratação de freelances.

Desenvolvida uma aplicação completa para conectar empresas e freelances.

## Tecnologias e práticas utilizadas
- Python
- Django 4
- SQLite
- Arquitetura MVT

## Funcionalidades
- Autenticação e Cadastro de Usuário
- Edição de Perfil
- Reset de Senha
- Listagem, Detalhes e Aceite de Jobs
- Atualização de Perfil, Listagem de Jobs Aceitos e Envio de Arquivos

![image](https://user-images.githubusercontent.com/62387982/162999162-d2166ea5-f5a4-4c81-9a64-8b015ef4644c.png)

![image](https://user-images.githubusercontent.com/62387982/163001557-399e9726-7ac3-4556-ae07-7d03abffffdf.png)

![image](https://user-images.githubusercontent.com/62387982/163002240-36a0bac8-8ea7-4cca-86eb-e481a084d870.png)

![image](https://user-images.githubusercontent.com/62387982/163002379-9174444e-b140-466f-a3be-dce53a6c4b01.png)

![image](https://user-images.githubusercontent.com/62387982/163002512-5e9859e9-fa36-481d-bfa1-025b10ad8233.png)

## Comandos

### pip
```
pip list --outdate
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
```

### virtualenv (windows)
```
python -m venv env
env\Scripts\activate.bat
env\Scripts\deactivate.bat
```

### Instalar bibliotecas, gravar/instalar requerimentos
```
(env) pip install django
(env) pip install pillow

(env) pip freeze > requirements.txt
(env) pip install -r requirements.txt
```

### Criar projeto
```
(env) django-admin startproject controlJobs .
```

### Criar apps
```
(env) python manage.py startapp authentication
(env) python manage.py startapp jobs
```

### Migrations
```
(env) python manage.py makemigrations
(env) python manage.py migrate
```
### Executar projeto
```
(env) python manage.py runserver
```


