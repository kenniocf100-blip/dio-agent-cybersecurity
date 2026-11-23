# Fundamentos de Segurança da Informação

## Conceitos essenciais

- **Ativo:** dado, sistema, serviço ou recurso que possui valor para uma pessoa ou organização.
- **Ameaça:** circunstância ou agente capaz de causar dano a um ativo.
- **Vulnerabilidade:** fraqueza em um ativo ou controle que pode ser explorada por uma ameaça.
- **Risco:** combinação contextual da probabilidade de um evento e de suas consequências.
- **Exploit:** técnica ou código que aproveita uma vulnerabilidade.
- **Mitigação:** medida que reduz a probabilidade ou o impacto de um risco.
- **Correção (remediação):** ação que elimina ou trata a causa da vulnerabilidade.
- **Evidência:** informação observável que sustenta um achado, como trecho de código, log ou resultado reproduzível.

## Tríade CIA

- **Confidencialidade:** somente pessoas e sistemas autorizados acessam a informação.
- **Integridade:** dados e sistemas permanecem corretos e não são alterados indevidamente.
- **Disponibilidade:** sistemas e informações ficam acessíveis quando necessários.

## Análise de risco

Considere pelo menos:
1. Ativo afetado e sua importância.
2. Condições necessárias para explorar a falha.
3. Privilégios e interação exigidos.
4. Impacto potencial em confidencialidade, integridade e disponibilidade.
5. Controles existentes e exposição do ativo.
6. Incertezas e evidências que faltam.

Não atribua severidade apenas pelo nome da vulnerabilidade. Justifique a classificação com o contexto. Se usar CVSS, informe a versão, os vetores e a fonte; não invente uma pontuação.

## Boas práticas defensivas

- Aplicar atualizações e corrigir dependências vulneráveis.
- Usar autenticação forte, autorização por menor privilégio e gestão segura de sessões.
- Validar entradas conforme o contexto e usar consultas parametrizadas em SQL.
- Proteger segredos fora do código-fonte.
- Registrar eventos relevantes sem armazenar credenciais ou dados sensíveis desnecessários.
- Realizar backups e testar restauração.
- Segmentar redes e restringir serviços expostos.
- Revisar configurações, permissões e dependências.
- Criar testes de regressão para impedir que falhas corrigidas retornem.

## Referenciais

- **OWASP Top 10:** categorias de riscos comuns em aplicações web.
- **CWE:** catálogo de tipos de fraquezas de software e hardware.
- **MITRE ATT&CK:** base de conhecimento de táticas e técnicas observadas em atividades adversárias; não é uma escala de severidade.
- **CVSS:** sistema para expressar severidade técnica de vulnerabilidades, que deve ser aplicado com vetores e contexto apropriados.

## Limites de avaliação

Um scanner pode produzir falsos positivos e falsos negativos. Confirme achados com evidências adequadas, dentro do escopo autorizado. Registre limitações e não declare segurança absoluta.
