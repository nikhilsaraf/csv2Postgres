#!/bin/bash
db=$1
echo "db: $db"
dir=$2
echo "csv dir: $dir"
files=`ls $dir`
echo "files: $files"
for file in $files; do
    python load.py $db "$dir$file" ${file%????};
done;
