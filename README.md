## API Base Python

API REST construída com FastAPI, SQLAlchemy assíncrono e Alembic, organizada por módulos de domínio (`modules/users`, `modules/products`, `modules/health`).

## Estrutura

```text
app/
  api/            # composição do router principal
  core/           # configuração e engine assíncrona
  db/             # base declarativa e dependências de sessão
  modules/
    health/       # módulo de healthcheck (rotas)
    users/        # model, schemas, repository, service, routes
    products/     # model, schemas, repository, service, routes
alembic/          # migrações de banco
tests/            # testes de endpoints e fluxos
```

## Pré-requisitos

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- Docker (opcional, para Postgres/Redis via compose)

## Setup local

1. Instale dependências:

```bash
make install
```

2. Crie e ajuste `.env` com as variáveis esperadas em `app/core/config.py`.

3. Suba dependências locais (opcional):

```bash
docker compose up -d
```

4. Aplique migrações:

```bash
make upgrade
```

5. Rode a API:

```bash
make run
```

## Comandos úteis

- `make dev`: sobe API em `0.0.0.0:8000` com reload
- `make lint`: executa `mypy` em `app`
- `make format`: aplica `black` e `isort`
- `make test`: executa testes
- `make migration m="mensagem"`: cria nova migração

## Boas práticas adotadas

- Migrações Alembic lineares e descritivas
- Separação clara entre camadas de HTTP, regra de negócio e persistência
- Configuração centralizada via `BaseSettings`
