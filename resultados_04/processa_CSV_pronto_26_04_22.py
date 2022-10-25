import csv
# importing datetime module
import datetime
import time
import os, time

print("Inicio Script Python3");
#os.environ['TZ'] = 'America/Fortaleza'
#time.tzset()

with open('N3_5_m.csv') as csv_file:
    
    csv_reader = csv_file.readlines()
    #transforma em lista de 3 elementos
    arquivo = open('saida_N3_5_m.csv', 'w') 
    cont=0
    col2 = 0
    col3 = 0
    col4 = 0
    col7 = 0
    a =0
    cabecalho = 0
    print("Antes do FOR");
    for x in csv_reader:    
        tamanho_texto=len(x);
        dado=x[tamanho_texto-14:tamanho_texto-2] #pega somente hora registrada no mongodb
        dado_ano=x[tamanho_texto-25:tamanho_texto-15] #pega somente a data do nmongodb (ano, mes , dia)
        dado_completo=x[0:tamanho_texto-1] # x[tamanho_texto-49:tamanho_texto-26]
        value=x[0:tamanho_texto-26]
        lista = dado.split(':')
        lista_ano = dado_ano.split('-')
        lista_completo = dado_completo.split(';')
        lista_value = value.split(';')
        if(len(lista) ==3) :
                (hora,minuto,sec) = lista
                (ano, mes, dia) = lista_ano
                (id_device, attr, value) = lista_value
                #print(lista)
                hora = int(hora)-3
                if (hora <0):
                    hora = hora*(-1)
                print(hora);
                sec2 = sec
                sec2 = sec2.replace('.','')
                milisec = int(sec2)
                sec = int(float(sec))
                date_time = datetime.datetime(int(ano),int(mes),int(dia),int(hora),int(minuto),int(sec),int(milisec)).timestamp()
                date_time2 = str(date_time).replace('.','')
                unix_time = date_time2		
		#unix_time =long( time.mktime(date_time.timetuple())*1000)
                texto_value = str(id_device)+str(attr)+str(value)
		#mostrando resultado na tela
                a = unix_time
                b = value
                if( a == unix_time):
                        cont = cont+1
                        col1 = cont
                        if(attr == 'temperatura'):
                                col2 = value
                        elif(attr == 'umidade'):
                                col3 = value
                        elif(attr == 'tempo'):
                                col4 = value
                        elif(attr == 'data'):
                                col7 = value
                        col5 = unix_time
                col6 =(float(col5) - float(col4))
                saida2 ='Id = '+str(col1)+' Temperatura = '+str(col2)+' Umidade = '+str(col3)+' Tempo = '+str(col4)+' Data = '+str(col7)+' Unix_time = '+str(col5)+' Discrepancia = '+str(col6)
                saida =str(col1)+','+str(col2)+','+str(col3)+','+str(col7)+','+','+str(col4)+','+str(col5)+','+str(col6)
                print(saida2)			
                #print(lista_completo,'UNIX TIme convertido = ',unix_time,)
                if(cabecalho ==0):
                     arquivo.write('ID, Temperatura, Umidade, Tempo, Data,Unix_time, Discrepancia ,  \n')
                     cabecalho=1
                arquivo.write(str(saida)+'\n')

arquivo.close()
csv_file.close()	

print("Fim Script Python3");













			

