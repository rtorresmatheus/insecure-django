# insecure-django

Este projeto é uma implementação propositalmente insegura do Django, criada para promover o estudo de Testes de Segurança e Práticas de Codificação Segura. **Não utilize este código em produção.**

> ⚠️ **Atenção:** Este repositório contém vulnerabilidades críticas de segurança, intencionalmente inseridas para fins educacionais.

---

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Executar](#como-executar)
- [Requisitos](#requisitos)
- [Exemplos de Uso](#exemplos-de-uso)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Aviso Legal](#aviso-legal)

---

## Sobre o Projeto

O `insecure-django` foi desenvolvido para demonstrar falhas comuns de segurança em aplicações web baseadas em Django. O objetivo é servir como base para treinamentos, testes de ferramentas de segurança e exercícios de refatoração.

---

## Funcionalidades

- Exemplos de vulnerabilidades como CSRF, XSS, Injeção de Código, entre outras.
- Templates e rotas para exploração de falhas.
- Scripts de prova de conceito (PoC) para ataques.
- Estrutura modular para facilitar a análise e refatoração.

---

## Estrutura do Projeto

```
insecure-django/
├── csrf-hacker/                # Exemplos de ataques CSRF
├── http-requests-poc/          # Provas de conceito de requisições HTTP
├── insecure_django/            # Configurações principais do Django
├── prototype-poc/              # Exemplos de poluição de protótipos
├── serialize-deserialize-poc/  # Exemplos de serialização insegura
├── static/                     # Arquivos estáticos (CSS, JS, imagens)
├── staticstorage/              # Armazenamento de arquivos estáticos
├── templates/                  # Templates HTML
├── xploitPickl/                # App Django com falhas de serialização
├── xploitpp/                   # App Django com outras vulnerabilidades
├── xploitSOP_CORS_CSRF/        # App Django com falhas de SOP/CORS/CSRF
├── xploitSSRF/                 # App Django com falhas de SSRF
├── manage.py                   # Utilitário de gerenciamento Django
├── requirements.txt            # Dependências do projeto
└── README.md                   # Este arquivo
```

---

## Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/rtorresmatheus/insecure-django.git
   cd insecure-django
   ```

2. **Instale o Python 3 e o Django:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute as migrações:**
   ```bash
   python manage.py migrate
   ```

4. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

5. **Acesse a aplicação:**
   - Abra o navegador em: [http://localhost:8000](http://localhost:8000)

---

## Requisitos

- Python 3.x
- Django (veja a versão em `requirements.txt`)
- Outras dependências listadas em `requirements.txt`

---

## Exemplos de Uso

- Testes de ferramentas de análise de segurança.
- Exercícios de identificação e correção de vulnerabilidades.
- Treinamentos de equipes de desenvolvimento seguro.

---

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork este repositório.
2. Crie uma branch para sua feature ou correção (`git checkout -b minha-feature`).
3. Commit suas alterações (`git commit -m 'Minha contribuição'`).
4. Push para a branch (`git push origin minha-feature`).
5. Abra um Pull Request.

---

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Aviso Legal

Este projeto é apenas para fins educacionais e de pesquisa. O uso deste código em ambientes de produção ou para fins maliciosos é estritamente proibido. O autor não se responsabiliza por qualquer dano causado pelo uso deste repositório.