from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/level_1.py")

# Underscores do not work in Pyinvoke task names
# You can make them work by changing the config as shown:
# http://docs.pyinvoke.org/en/latest/concepts/namespaces.html#dashes-vs-underscores
@task
def level1(ctx):
    ctx.run("python3 src/level_1.py")

@task
def level2(ctx):
    ctx.run("python3 src/level_2.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task
def coveragereport(ctx):
    ctx.run("coverage html")