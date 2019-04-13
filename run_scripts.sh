echo "Iniciando execução do script!"

echo "Step 1"
cd readmes/
rm *.md
cd json/
rm *.json

echo "Step 2"
npm i markdown-to-json

echo "Step 3"
cd ../../
python readmes/script_get_readme.py
python script_parser_json.py

echo "Fim da execução!"