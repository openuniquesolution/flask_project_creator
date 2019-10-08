#!/bin/sh

name=$1

basedir=`dirname $0`
if [ ${basedir} == "." ]; then
basedir=`pwd`
fi
cp ${basedir}/../templates/new_project/base_file ${name}.py
mkdir -p ${name}/templates
mkdir -p ${name}/static