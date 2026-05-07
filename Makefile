run:
	uv run uvicorn app.main:app --reload

format:
	uv run black .
	uv run isort .

lint:
	uv run mypy app

test:
	uv run pytest

migration:
	uv run alembic revision --autogenerate -m "$(m)"

upgrade:
	uv run alembic upgrade head

install:
	uv sync

freeze:
	uv lock

dev: 
	uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000