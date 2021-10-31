
def C():
    codeC = "#include <stdio.h>\nint main() {\nprintf(\"Hello World!\");\nreturn 0;\n}"
    def file_create(code):
        with open("HelloWorld.c", "wt") as fout:
            fout.write(code)

    file_create(codeC)

    result = subprocess.run(["docker", "run", "--rm", "-w", "/usr/src/app", "-v", f"{os.getcwd()}:/usr/src/app",
                             "gcc", "bash", "-c", "gcc HelloWorld.c -o HelloWorld; ./HelloWorld"], stdout=subprocess.PIPE)
    print(result.stdout.decode())