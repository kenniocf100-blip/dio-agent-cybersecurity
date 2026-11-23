# DIO Agent — Cybersecurity Analyst

Especialização educacional do [DIO Agent](https://github.com/digitalinnovationone/dio-agent) para apoiar estudos de análise de vulnerabilidades, AppSec e defesa cibernética.

O objetivo é orientar o estudante a trabalhar com evidências, confirmar autorização e escopo, avaliar riscos, propor correções e validar mitigações. O agente não substitui scanners, auditorias ou profissionais responsáveis.

## O que este projeto adiciona

- Skill orientativa de análise de vulnerabilidades.
- Persona de agente com foco em AppSec e Blue Team.
- Base de conhecimento com conceitos fundamentais.
- Modelo de fluxo para priorização e relatório de achados.
- Laboratório local que demonstra SQL Injection e sua correção por consulta parametrizada.

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

## Como integrar ao DIO Agent

Este repositório contém os arquivos de especialização. Para usar a personalização junto ao projeto-base:

1. Clone o projeto original: `git clone https://github.com/digitalinnovationone/dio-agent.git`
2. Copie para a pasta do projeto-base os arquivos e diretórios deste repositório, preservando os arquivos originais.
3. Abra a pasta do projeto-base em um harness compatível com instruções `AGENTS.md` e skills, como Claude Code, Codex ou OpenCode.
4. Peça ao agente para ler `AGENTS.md` e a skill `skills/vulnerability-analysis/SKILL.md`.

> Observação: este repositório é uma camada de especialização/documentação. Ele não inclui nem substitui o código-fonte do DIO Agent original, nem afirma que o agente-base foi executado ou validado aqui.

## Laboratório de SQL Injection

O laboratório usa Flask e SQLite localmente para comparar uma consulta vulnerável com uma consulta parametrizada. Ele não acessa serviços externos e seus testes rodam pelo cliente de testes do Flask.

Consulte [lab/sql-injection/README.md](lab/sql-injection/README.md).

## Modelo resumido de relatório

| Campo | Exemplo didático |
|---|---|
| ID | WEB-001 |
| Ativo | Aplicação local de laboratório |
| Achado | SQL Injection na autenticação |
| Evidência | Entrada manipulada altera a lógica da consulta vulnerável |
| Impacto | Possível autenticação indevida e exposição de dados |
| Severidade | Alta (classificação ilustrativa; depende do contexto) |
| Recomendação | Usar consultas parametrizadas |
| Reteste | Reexecutar o teste negativo na versão corrigida |

## Segurança e limites

- Teste somente ativos próprios ou com autorização explícita.
- Defina escopo, janela de teste, limites e plano de reversão.
- Não execute exploração ou varredura contra terceiros.
- Não inclua senhas, tokens ou dados pessoais em prompts, commits ou relatórios.
- Diferencie fatos observados de hipóteses; não invente CVEs, versões ou evidências.

## Referências

- [DIO Agent — projeto-base](https://github.com/digitalinnovationone/dio-agent)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [CWE](https://cwe.mitre.org/)
- [Python sqlite3 — placeholders](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)
