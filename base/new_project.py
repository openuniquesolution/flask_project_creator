import os
import shutil
from .util import git_enable, venv_enable, rendeer_template

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


def pre_common_project_files_work(name):
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

def post_common_project_files_work(args):
    cwd = os.getcwd()
    fullpath = os.path.join(cwd, args.name)

    fpc_var_value = {
    'appname': args.name,
    'virtualenv': args.venv,
    'path': fullpath,
    'git': args.git,
    'Structure': args.structure
    }

    rendeer_template(
        tem_dir,
        "fpc",
        os.path.join(fullpath,".fpc"),
        fpc_var_value
    )


def main(args):
    name = args.name
    pre_common_project_files_work(name)
    function_to_call = {
        "rest": rest_project,
        "component": component_project,
        "layer": layer_project
    }

    function_to_call[args.structure](name)

    if args.git:
        git_enable(name, tem_dir)

    if args.venv:
        venv_enable(name)

    post_common_project_files_work(args)