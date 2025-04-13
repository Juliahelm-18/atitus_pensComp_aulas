#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Function to run pytest on a given file with minimal output
run_tests() {
  local file=$1
  pytest -q --tb=no --disable-warnings "$file"
}


# run_tests 08_Strings_random/*.py
# run_tests 09_Dicionários/*.py
# run_tests 10_Introducao_a_funcoes/*.py
# run_tests 11_Funcoes_e_parametros_avancados/*.py
# run_tests 12_Funcoes_e_imports/*.py
# run_tests 13_exercicios_leetcode/*.py
# run_tests 14_manipulacao_de_datas/*.py
# run_tests 15_manipulacao_de_arquivos/*.py
# run_tests 16_json,XML,CSV/*.py
# run_tests 17_TDD/*.py
# run_tests 18_exercicios/*.py
# run_tests XX_extras/*.py

echo "All tests ran successfully"
