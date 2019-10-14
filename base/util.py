from jinja2 import FileSystemLoader, Environment
import shutil
import sys
import os
import subprocess

def git_enable(name, tem_dir):
    output, error = subprocess.Popen(
        ['git', 'init', name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).communicate()
    if error:
        with open('git_error.log', 'w') as fd:
            fd.write(error.decode('utf-8'))
            print("Error with git init")
            sys.exit(2)
    shutil.copyfile(
        os.path.join(tem_dir,'gitignore'),
        os.path.join(name, '.gitignore')
    )

def venv_enable(name):
    pass
    virtualenv_exe = which('pyvenv')
    if virtualenv_exe:
        output, error = subprocess.Popen(
            [virtualenv_exe, os.path.join('env')],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        ).communicate()
        if error:
            with open('virtualenv_error.log', 'w') as fd:
                fd.write(error.decode('utf-8'))
                print("An error occurred with virtualenv")
                sys.exit(2)
        venv_bin = os.path.join('env/bin')
        output, error = subprocess.Popen(
            [
                os.path.join(venv_bin, 'pip'),
                'install',
                '-r',
                os.path.join(name, 'requirements.txt')
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        ).communicate()
        if error:
            with open('pip_error.log', 'w') as fd:
                fd.write(error.decode('utf-8'))
                sys.exit(2)
    else:
        print("Could not find virtualenv executable. Ignoring")


def rendeer_template(template_base_folder, template_name, dest_file , map_var):
    file_loader = FileSystemLoader(template_base_folder)
    env = Environment(loader=file_loader)
    tm = env.get_template(template_name)
    out = tm.render(map_var)
    
    with open(dest_file, "w", encoding='utf-8') as file_out:
       file_out.write(out)