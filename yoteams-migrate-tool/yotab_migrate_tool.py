import shutil
import sys
import os

def main():
    # create teamsapp.local.yml
    with open("teamsapp.template.yml", 'r') as f:
        template = f.read()
    with open("../teamsapp.local.yml", 'w') as f:
        f.write(template)
    
    # create launch.json
    with open("launch.template.json", 'r') as f:
        template = f.read()
    with open("../.vscode/launch.json", 'w') as f:
        f.write(template)
    
    # create tasks.json
    with open("tasks.template.json", 'r') as f:
        template = f.read()
    with open("../.vscode/tasks.json", 'w') as f:
        f.write(template)
    
    # move .env to .env.local
    os.rename("../.env", ".env.local")
    os.mkdir("env")
    shutil.move(".env.local", "env/.env.local")