# Guia de Instalação

Siga os passos abaixo para instalar e executar o projeto insecure-django em seu ambiente local.

## Pré-requisitos

- Python 3.x
- pip
- Git

## Passos para Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/rtorresmatheus/insecure-django.git
   cd insecure-django
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

4. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

5. Acesse a aplicação em [http://localhost:8000](http://localhost:8000)
