echo "Iniciando execução do script!"

echo "Step 1"
cd readmes/
rm *.md
rm -rf json
mkdir json 

echo "Step 2"
cd ../
python readmes/script_get_readme.py
python script_parser_json.py

echo "Step 3"
mv readmes/*.json readmes/json

echo "Fim da execução!"
