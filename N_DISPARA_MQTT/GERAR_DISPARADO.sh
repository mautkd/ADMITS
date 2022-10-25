#Script que dispara no dojot lendo do CSV
#jamais="1479626031[ ]1895[ ]2435"
while IFS= read -r LinhaCsv #laço de repetição ate finalizar o arquivo csv
do
    echo "
		t=1
		u=1
		t=modificar_temperatura
		u=modificar_umidade
		d=modificar_tempo"
	echo "sleep 1.5"
	echo $LinhaCsv 
	echo "sleep 1"	
done < mosquitto_1por_segundo.csv

