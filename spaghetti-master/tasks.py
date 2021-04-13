from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/level_1.py")

def level_1(ctx):
    ctx.run("python3 src/level_1.py")