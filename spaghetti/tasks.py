from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/start_game.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task
def coveragereport(ctx):
    ctx.run("coverage html")