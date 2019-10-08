#!/bin/sh

name=$1

basedir=`dirname $0`
if [ ${basedir} == "." ]; then
basedir=`pwd`
fi

tem_dir="${basedir}/../templates/new_project"

mkdir app
mkdir -p app/templates
mkdir -p app/static
touch config.py
cp ${tem_dir}/base_file ${name}.py
cp ${tem_dir}/__init__ app/__init__.py

###########################################
# dot file creation

touch .fpc
cp ${tem_dir}/gitignore .gitignore