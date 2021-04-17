from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/level_1.py")

@task
def test(ctx):
    ctx.run("python3 src/tests/util_test.py")
    ctx.run("python3 src/tests/level_1_test.py")