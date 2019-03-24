python3 currency_convert_rb.py --help

python3 currency_convert_rb.py --field 2

python3 currency_convert_rb.py --field 2 --multiplier 0.8 -i data.csv -o data-fr.csv

python3 currency_convert_rb.py --field 2 --multiplier 1.25 -i data-fr.csv -o data.csv

python3 currency_convert_rb.py --field 2 --multiplier 0.8 < data.csv > data-fr.csv

python3 currency_convert_rb.py --field 2 --multiplier 1.25 < data-fr.csv > data.csv
