#!/bin/bash
echo "Iniciando execução do script!"

echo "Step 1"
cd readmes/
rm *.md
rm -rf json
mkdir json

echo "Step 2"
npm i -g markdown-to-json

echo "Step 3"
cd ../
python readmes/script_get_readme.py
python script_parser_json.py
sleep 3
python concatenate_json.py

echo "Step 4"
mv readmes/*.json readmes/json

echo "Fim da execução!"
