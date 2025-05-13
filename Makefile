ruff:
	ruff check && ruff format --diff

format:
	ruff check --fix && ruff format

mypy:
	mypy .

check: format ruff mypy