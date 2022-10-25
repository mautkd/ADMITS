#Script que dispara no dojot lendo do CSV

t=1
u=2
d=`date +%s%N`
jamais="1479626031[ ]1895[ ]2435"

while IFS= read -r LinhaCsv #laço de repetição ate finalizar o arquivo csv
do
    #echo "$LinhaCsv" #mostra primeira linha
	t=1
    u=1
	t=$((t+RANDOM %40))
    u=$((u+RANDOM %100))
    d=`date +%s%N`
    sleep 1.5
mosquitto_pub -h 10.10.100.133 -p 1883 -t /admin/7a2166/attrs -m '{"temperatura":'$t',"umidade":'$u',"tempo":'$d',"data":'$LinhaCsv'}'
    echo "Temperatura = "$t" Umidade = "$u" tempo="$d "data ="$LinhaCsv ;
    sleep 1	
done < X_path.csv

