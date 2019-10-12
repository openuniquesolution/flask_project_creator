import shutil
import sys
from jinja2 import FileSystemLoader, Environment

if sys.version_info < (3, 0):
    from shutilwhich import which
else:
    from shutil import which
import os
import subprocess

base_dir = os.path.dirname(os.path.realpath(__file__))
tem_dir = "%s/../templates/new_project" % (base_dir)

def rest_project(name):
    os.mkdir(os.path.join(name, "app", "controller"))
    os.mkdir(os.path.join(name, "app", "models"))

def component_project(name):
    os.mkdir(os.path.join(name, "app", "templates"))
    os.mkdir(os.path.join(name, "app", "static"))
    shutil.copyfile(
        os.path.join(tem_dir, "404"),
        os.path.join(name, "app", "templates", "404.html")
    )

def layer_project(name):
    pass

def git_enable(name):
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


def rendeer_template(template_name, dest_file , map_var):
    file_loader = FileSystemLoader(tem_dir)
    env = Environment(loader=file_loader)
    tm = env.get_template(template_name)
    out = tm.render(map_var)
    
    with open(dest_file, "w", encoding='utf-8') as file_out:
       file_out.write(out) 


def main(args):
    name = args.name
    
    os.mkdir(name)
    os.mkdir(os.path.join(name, "app"))

    shutil.copyfile(
        os.path.join(tem_dir, "base_file"),
        os.path.join(name, "%s.py"%(name))
    )
    os.chmod(os.path.join(name, "%s.py"%(name)), mode=555)
    shutil.copyfile(
        os.path.join(tem_dir, "config"),
        os.path.join(name, "config.py")
    )
    shutil.copyfile(
        os.path.join(tem_dir, "__init__"),
        os.path.join(name, "app", "__init__.py")
    )

    function_to_call = {
        "rest": rest_project,
        "component": component_project,
        "layer": layer_project
    }

    cwd = os.getcwd()
    fullpath = os.path.join(cwd, name)

    fpc_var_value = {
    'appname': name,
    'virtualenv': args.venv,
    'path': fullpath,
    'git': args.git,
    'Structure': args.structure
    }

    function_to_call[args.structure](name)

    if args.git:
        git_enable(name)

    if args.venv:
        venv_enable(name)

    rendeer_template(
        "fpc",
        os.path.join(fullpath,".fpc"),
        fpc_var_value
    )