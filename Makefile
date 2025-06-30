ruff:
	ruff check && ruff format --diff

format:
	ruff check --fix && ruff format

mypy:
	mypy --strict .

test:
	pytest

check: format mypy test