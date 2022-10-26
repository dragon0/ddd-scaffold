from invoke import task

PYTEST_OPTIONS = "--log-file='tests.log' --log-file-level=DEBUG"


@task
def test(c):
    '''Run test suite once'''
    c.run(f"pytest {PYTEST_OPTIONS}", pty=True)


@task
def watch(c):
    c.run(f"pytest-watch -- {PYTEST_OPTIONS}", pty=True)


@task
def autoformat(c):
    c.run("autopep8 -r -i ddd_scaffold tests")

@task
def lint(c):
    c.run("flake8 ddd_scaffold tests")
    c.run("pylint ddd_scaffold tests")


@task(lint)
def ci_test(c):
    '''Run tests and generate result and coverage XML reports'''
    try:
        c.run("pytest --junitxml=testresults.xml --cov=ddd_scaffold/", pty=True)
    finally:
        c.run("coverage xml")


@task(ci_test)
def coverage(c):
    c.run("coverage html")
