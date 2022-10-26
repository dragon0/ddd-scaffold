# Poetry can run commands in the virtualenv,
# as well as scripts defined in pyproject.toml
# https://python-poetry.org/docs/cli/#run
run:
	poetry run ddd_scaffold

# All of the tasks defined in tasks.py can be run via poetry run invoke
test:
	poetry run invoke coverage

# Run after generating coverage files to view a report
coverage-report:
	poetry run coverage report

run test coverage-report: env

env: .venv
.venv: poetry.lock
	poetry env info --path > /dev/null 2>&1 || ( poetry install && poetry env info --path > .venv )
