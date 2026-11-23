# Laboratório local — SQL Injection

## Objetivo

Demonstrar, em uma aplicação didática local, como a concatenação de entrada em uma consulta SQL pode permitir SQL Injection e como consultas parametrizadas evitam que a entrada seja interpretada como parte do comando.

O laboratório não realiza conexão externa. Os testes usam o cliente de testes do Flask.

## Requisitos

- Python 3.10 ou superior
- pip

## Preparação

Entre nesta pasta:

```bash
cd lab/sql-injection
python -m venv .venv
```

Ative o ambiente virtual:

**Windows PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS**
```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## Executar os testes

```bash
pytest -v
```

Resultado esperado: quatro testes aprovados. O teste de demonstração confirma que a aplicação vulnerável aceita uma entrada manipulada; o teste da versão corrigida confirma que a mesma entrada é tratada como dado e rejeitada.

## Executar manualmente (opcional)

Em um terminal, inicie a versão vulnerável:

```bash
python app_vulnerable.py
```

Ela escuta apenas em `127.0.0.1:5001`. Em outro terminal, envie uma requisição local:

```bash
curl -i -X POST http://127.0.0.1:5001/login -H "Content-Type: application/json" -d "{\"username\":\"admin' -- \",\"password\":\"wrong\"}"
```

A versão corrigida usa a porta 5002:

```bash
python app_fixed.py
```

Repita a requisição apontando para `http://127.0.0.1:5002/login`. A entrada manipulada deve ser rejeitada.

## Entenda a correção

A versão vulnerável monta a consulta incorporando diretamente os valores fornecidos pelo usuário. Na versão corrigida, os valores são passados separadamente como parâmetros:

```python
query = "SELECT username FROM users WHERE username = ? AND password = ?"
connection.execute(query, (username, password))
```

O banco trata os parâmetros como dados, e não como parte da sintaxe SQL. Em aplicações reais, também use hash de senha adequado, controles de autenticação, limitação de tentativas e mensagens de erro seguras. O exemplo é didático e não deve ser usado como sistema de autenticação real.

## Segurança

Execute apenas este laboratório local. Não exponha a versão vulnerável à rede, não a publique em hospedagem e não adapte o teste para sistemas de terceiros.
