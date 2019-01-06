#####本脚本使用方法：复制以下命令一次执行。然后人工判断结果是否正确。
#####
#####
python currency_convert.py --field 2 --multiplier 0.8 < data.csv > data-fr.csv
python currency_convert.py --field 2 --multiplier 0.8 -i data.csv > data-fr.csv
python currency_convert.py --field 2 --multiplier 0.8 -i data.csv -o data-fr2.csv
python currency_convert.py --field 2 --multiplier 0.8 -i data.csv
python currency_convert.py --help
python currency_convert.py --field 2 --multiplier 0.8 -i "pivotsense,7.99,Pivotal Sense (ltd.),1483820006,/dl area/pivotsense.tgz,/r/ps.tgz"
python currency_convert.py --field 2 --multiplier 0.8 -i data-fr.csv > data3.csv