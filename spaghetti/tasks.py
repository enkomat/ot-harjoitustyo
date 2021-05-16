from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task
def coveragereport(ctx):
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")