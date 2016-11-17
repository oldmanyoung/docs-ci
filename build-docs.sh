#!/bin/sh
#echo "Hello world!"
echo starting...
cd github-code
mkdocs new new-project
cp -R project/documentation/ new-project
cd new-project
mkdocs build
pwd
ls
echo ...done
