# Diagnostico Inicial do Healthcheck

Checklist de revisao para [app/main.py](../app/main.py):

## 1. Riscos tecnicos
- [ ] Healthcheck superficial: so valida que a API subiu, nao dependencias (DB, fila, cache).
- [ ] Contrato fragil para clientes: `timestamp` em ISO pode variar em formato esperado pelo consumidor.
- [ ] Sem versionamento de rota (`/v1/health`), pode dificultar evolucao futura.
- [ ] Sem observabilidade no endpoint (logs/metricas), diagnostico em incidente fica mais dificil.

## 2. O que pode quebrar em producao
- [ ] Orquestrador considerar servico "saudavel" mesmo com dependencias criticas fora.
- [ ] Cliente quebrar parse de data se esperar outro formato (ex.: epoch em vez de ISO-8601).
- [ ] Drift de dependencias se ambiente nao for reproduzido exatamente.
- [ ] Mudancas futuras no payload sem contrato/teste podem quebrar integracoes.

## 3. Testes minimos a criar
- [ ] `GET /health` retorna `200`.
- [ ] Resposta contem `status` e `timestamp`.
- [ ] `status == "ok"`.
- [ ] `timestamp` e parseavel como datetime e com timezone UTC.
- [ ] `Content-Type` e `application/json`.
- [ ] Metodo invalido (ex.: `POST /health`) retorna `405`.
