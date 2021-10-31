
def python():
    codeP = "a=10\nprint(a)"
    result = subprocess.run(["docker", "run", "--rm", "python:3", "python", "-c", codeP], stdout=subprocess.PIPE)
    print(result.stdout.decode())
