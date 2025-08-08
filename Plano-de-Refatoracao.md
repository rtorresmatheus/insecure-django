# Plano de Refatoração Prioritário

Este documento consolida a priorização dos principais problemas de segurança e qualidade (code smells) do projeto, além de sugerir abordagens práticas para refatoração.

---

## 1. Vulnerabilidades Críticas (Prioridade Alta)

### Exposição de Dados Sensíveis
- **Problema:** Segredos e senhas hardcoded em arquivos de código ou configuração.
- **Solução:** Utilize variáveis de ambiente e remova segredos do versionamento.
- **Exemplo:**
  ```python
  import os
  SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
  ```

### Uso de Prints para Debug
- **Problema:** Uso de `print()` para debug em produção.
- **Solução:** Substitua por logging estruturado.
- **Exemplo:**
  ```python
  import logging
  logger = logging.getLogger(__name__)
  logger.error('Mensagem de erro')
  ```

### Falhas CSRF, XSS, SSRF e Injeção
- **Problema:** Rotas e templates vulneráveis a ataques comuns.
- **Solução:**
  - Sempre use `{% csrf_token %}` em formulários.
  - Escape variáveis em templates.
  - Valide e sanitize entradas do usuário.
  - Use bibliotecas seguras para requisições HTTP.

---

## 2. Code Smells Importantes (Prioridade Média)

### Testes Automatizados Ausentes
- **Problema:** Falta de testes unitários e de integração.
- **Solução:** Implemente testes para as principais rotas e funções usando `pytest` ou o framework do Django.

### Nomes Pouco Descritivos
- **Problema:** Arquivos, funções e variáveis com nomes genéricos.
- **Solução:** Renomeie para refletir claramente o propósito de cada elemento.

### Logging Inexistente
- **Problema:** Ausência de logging estruturado.
- **Solução:** Implemente e padronize o uso do módulo `logging`.

---

## Resumo Consolidado

| Problema                       | Prioridade | Sugestão de Refatoração                                  |
|--------------------------------|------------|---------------------------------------------------------|
| Exposição de dados sensíveis   | Alta       | Usar variáveis de ambiente                              |
| Uso de prints para debug       | Alta       | Substituir por logging estruturado                      |
| Falhas CSRF/XSS/SSRF/Injeção   | Alta       | Corrigir templates, validar entradas, usar libs seguras |
| Testes ausentes                | Média      | Criar testes automatizados                              |
| Nomes pouco descritivos        | Média      | Renomear arquivos, funções e variáveis                  |
| Logging inexistente            | Média      | Implementar logging estruturado                         |

---

Siga este plano para atacar primeiro as vulnerabilidades críticas e, em seguida, os code smells mais relevantes. Para cada etapa, consulte os exemplos e recomendações acima.
