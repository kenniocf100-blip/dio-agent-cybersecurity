# DIO Agent — Cybersecurity Analyst

Especialização educacional do [DIO Agent](https://github.com/digitalinnovationone/dio-agent) para apoiar estudos de análise de vulnerabilidades, AppSec e defesa cibernética.

O objetivo é orientar o estudante a trabalhar com evidências, confirmar autorização e escopo, avaliar impacto, probabilidade e severidade, propor correções e validar mitigações. A melhoria escolhida foi padronizar a triagem de risco com uma matriz qualitativa e um roteiro de perguntas antes de qualquer teste ativo.

## O que este projeto adiciona

- Skill `vulnerability-analysis` com fluxo de análise e matriz qualitativa de risco.
- Persona de agente com foco em AppSec e Blue Team.
- Base de conhecimento com vulnerabilidade, ameaça, risco, tríade CIA e boas práticas.
- Regras de contexto, autorização, evidências, mitigação e reteste.
- Laboratório local Flask/SQLite que demonstra SQL Injection e a correção por consulta parametrizada.

## Estrutura

```text
.
├── AGENTS.md
├── README.md
├── agent/
│   ├── persona.md
│   └── knowledge/
│       └── security-basics.md
├── skills/
│   └── vulnerability-analysis/
│       ├── SKILL.md
│       └── README.md
└── lab/
    └── sql-injection/
        ├── app_vulnerable.py
        ├── app_fixed.py
        ├── requirements.txt
        ├── test_sql_injection.py
        └── README.md
```

## Como usar com o DIO Agent e Hermes

1. Instale o Git e o Python 3.10+.
2. Instale o Hermes seguindo a [documentação oficial](https://hermes-agent.nousresearch.com/docs).
3. Clone o DIO Agent original e esta especialização:

   ```bash
   git clone https://github.com/digitalinnovationone/dio-agent.git
   git clone https://github.com/kenniocf100-blip/dio-agent-cybersecurity.git
   ```

4. Integre os arquivos da especialização à pasta do DIO Agent:
   - Copie `agent/persona.md` e `agent/knowledge/security-basics.md` para os caminhos equivalentes.
   - Copie a pasta `skills/vulnerability-analysis/` para `skills/`.
   - **Mescle** a linha da skill e as regras relevantes de `AGENTS.md` da especialização no `AGENTS.md` original. Preserve as demais skills e instruções do projeto-base; não apague o conteúdo original.
5. Abra a pasta raiz `dio-agent` no VS Code. No terminal integrado, confirme que o diretório atual é a pasta que contém `AGENTS.md` e execute:

   ```bash
   hermes
   ```

6. Peça ao agente para ler `AGENTS.md`, `agent/persona.md`, `agent/knowledge/security-basics.md` e `skills/vulnerability-analysis/SKILL.md`.

> O comando de instalação e a configuração inicial do Hermes podem mudar; siga a documentação oficial para a sua plataforma. Este repositório contém a camada de especialização, não o código-fonte do DIO Agent nem o próprio Hermes.

## Laboratório de SQL Injection

O laboratório usa Flask e SQLite localmente. A versão vulnerável concatena a entrada do usuário na consulta; a versão corrigida usa parâmetros SQL. Os testes automatizados verificam a diferença entre os comportamentos.

Consulte [lab/sql-injection/README.md](lab/sql-injection/README.md).

Para executar:

```bash
cd lab/sql-injection
python -m venv .venv
# Ative o ambiente virtual e instale as dependências:
python -m pip install -r requirements.txt
pytest -v
```

O resultado esperado são quatro testes aprovados. O laboratório deve permanecer local, sem exposição à internet.

## Exemplo de relatório

| Campo | Exemplo didático |
|---|---|
| ID | WEB-001 |
| Ativo | Aplicação local de laboratório |
| Achado | SQL Injection na autenticação |
| Evidência | Entrada manipulada altera a lógica da consulta vulnerável |
| Impacto | Possível autenticação indevida e exposição de dados |
| Probabilidade | Depende de exposição, acesso à rota e controles |
| Severidade | Alta (classificação ilustrativa; depende do contexto) |
| Recomendação | Usar consultas parametrizadas |
| Reteste | Reexecutar os testes positivo e negativo na versão corrigida |

## Evidências para o portfólio

As capturas devem ser feitas durante a execução real no seu ambiente, sem simular resultados. Salve-as em `evidencias/` e atualize esta seção com os arquivos adicionados.

Sugestões de capturas:
1. Revisão do `app_vulnerable.py`, mostrando a concatenação insegura da consulta SQL.
2. Análise do agente identificando a falha, evidências, impacto, probabilidade e severidade.
3. Revisão do `app_fixed.py`, mostrando a consulta parametrizada.
4. Reteste confirmando que a entrada manipulada é rejeitada pela versão corrigida.
5. Cenário de servidor Ubuntu: o agente deve perguntar sobre autorização, escopo, janela e plano de reversão antes de sugerir testes ativos.

Não publique tokens, senhas, dados pessoais ou endereços/IPs sensíveis nas imagens.

## Segurança e limites

- Teste somente ativos próprios ou com autorização explícita.
- Defina escopo, janela de teste, limites e plano de reversão.
- Não execute exploração ou varredura contra terceiros.
- Não inclua senhas, tokens ou dados pessoais em prompts, commits ou relatórios.
- Diferencie fatos observados de hipóteses; não invente CVEs, versões ou evidências.
- O exemplo de senha em texto puro existe apenas para simplificar o laboratório; não representa uma prática aceitável em produção.

## Referências

- [DIO Agent — projeto-base](https://github.com/digitalinnovationone/dio-agent)
- [Hermes — documentação oficial](https://hermes-agent.nousresearch.com/docs)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [CWE](https://cwe.mitre.org/)
- [Python sqlite3 — placeholders](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)
