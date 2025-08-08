# Planejamento de Refatoração

Este documento tem como objetivo contabilizar e categorizar os problemas encontrados no projeto, separando-os por tipo (Segurança ou Qualidade), para auxiliar no planejamento das ações de refatoração.

## Resumo dos Problemas

| Tipo        | Quantidade | Exemplos/Localização                                 |
|-------------|------------|-----------------------------------------------------|
| Segurança   | 2          | - README.md: Projeto contém vulnerabilidades críticas\n- Possível exposição de variáveis sensíveis em SCSS e templates |
| Qualidade   | 4          | - Uso de `print` para debug em `xploitPickl/views.py`\n- Comentários de teste não implementados em `tests.py`\n- Uso de nomes genéricos em templates\n- Estrutura de arquivos duplicada |

## Detalhamento dos Problemas

### Segurança
- **README.md**: O projeto declara explicitamente a presença de vulnerabilidades críticas.\n  - "Critical Security Vulnerabilities are in this project."
- **Exposição de informações**: Variáveis como `$password-image` e `$login-image` em arquivos SCSS podem indicar exposição de dados sensíveis ou práticas inseguras.

### Qualidade
- **Uso de prints para debug**: Encontrado em `xploitPickl/views.py` (linhas 38, 42, 43, 47). Substituir por logging adequado.
- **Testes não implementados**: `xploitPickl/tests.py` contém apenas comentários padrão.
- **Nomes e estrutura**: Alguns arquivos e templates possuem nomes genéricos ou duplicados, dificultando a manutenção.
- **Comentários e anotações**: Ausência de anotações claras sobre pontos de refatoração ou problemas conhecidos.

## Próximos Passos
1. Substituir todos os `print` por logging estruturado.
2. Implementar testes automatizados nos arquivos de teste.
3. Revisar variáveis e dados sensíveis em arquivos de configuração e templates.
4. Melhorar a nomenclatura e organização dos arquivos.
5. Adicionar anotações claras sobre pontos críticos de refatoração.

---

*Documento gerado automaticamente para auxiliar no planejamento de refatoração do projeto.*
