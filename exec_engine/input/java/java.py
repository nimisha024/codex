
def java():
    codeJava = "public class HelloWorld {\npublic static void main(String[] args)\n{\nSystem.out.println(\"Hello World\");\n}\n}"
    def file_create(code):
        with open("HelloWorld.java", "wt") as fout:
            fout.write(code)

    file_create(codeJava)
    result = subprocess.run(["docker", "run", "--rm", "-w", "/usr/src/app", "-v", f"{os.getcwd()}:/usr/src/app",
                             "openjdk", "bash", "-c", "javac HelloWorld.java; java HelloWorld"], stdout=subprocess.PIPE)
    print(result.stdout.decode())
