import os
import subprocess
import json

code_json = '''{
    "c": ''' "#include <stdio.h>\nint main() {\nprintf(\"Hello World!\");\nreturn 0;\n}" ''',
    "java": ''' "public class HelloWorld {\npublic static void main(String[] args)\n{\nSystem.out.println(\"Hello World\");\n}\n}" ''',
    "python": ''' "a=10\nprint(a)" '''
}'''
code_list = json.loads(code_json)

file_json =''' {
    "c": ''' "HelloWorld.c" ''',
    "java": ''' "HelloWorld.java" ''',
    "python": ''' "HelloWorld.py" '''
} '''
file_list = json.loads(file_json)

comm_json = '''{
    "c": ''' "docker", "run", "--rm", "-w", "/usr/src/app", "-v", f"{os.getcwd()}:/usr/src/app","gcc", "bash", "-c", "gcc HelloWorld.c -o HelloWorld; ./HelloWorld" ''',
    "java": ''' "docker", "run", "--rm", "-w", "/usr/src/app", "-v", f"{os.getcwd()}:/usr/src/app", "openjdk", "bash", "-c", "javac HelloWorld.java; java HelloWorld" ''',
    "python": ''' "docker", "run", "--rm", "python:3", "python", "-c" '''
}'''
run_list = json.loads(comm_json)
language = ''' 
{
  "code": [
    {
    "name": 
    "code": ''' "#include <stdio.h>\nint main() {\nprintf(\"Hello World!\");\nreturn 0;\n}" ''',
    "file_name": ''' "HelloWorld.c" ''',
    "run_command": ''' "docker", "run", "--rm", "-w", "/usr/src/app", "-v", f"{os.getcwd()}:/usr/src/app","gcc", "bash", "-c", "gcc HelloWorld.c -o HelloWorld; ./HelloWorld" '''
    }
  ]
  "file_name":[
    {
    "code": 
    "file_name":
    "run_command":
     }
  ]
  "run_command":[
    {
    "code": 
    "file_name":
    "run_command":
     }
  ]
} 
'''

def compile_run(lang):
    if lang in code_list:
        code = code_list[lang]

        def file_create(code):
            with open(file_list[lang], "wt") as fout:
                fout.write(code)

        file_create(code)
        result = subprocess.run([run_list[lang]], stdout=subprocess.PIPE)
        print(result.stdout.decode())
        return result
    return "hello"
