import csv
# importing datetime module
import datetime
import time
import os, time

print("Inicio Script Python3");
#os.environ['TZ'] = 'America/Fortaleza'
#time.tzset()

with open('LOG_REDE_1_A_CADA_5_MINUTOS.CSV') as csv_file:
    
    csv_reader = csv_file.readlines()
    #transforma em lista de 3 elementos
    arquivo = open('saida_LOG_5m.csv', 'w') 
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
        dado=x[tamanho_texto-9:tamanho_texto-1] #pega somente hora registrada no mongodb
        dado_ano=x[tamanho_texto-20:tamanho_texto-10] #pega somente a data do nmongodb (ano, mes , dia)
        dado_completo=x[0:tamanho_texto-1] # x[tamanho_texto-49:tamanho_texto-26]
        value=x[0:tamanho_texto-21]
        lista = dado.split(':')
        lista_ano = dado_ano.split('-')
        lista_completo = dado_completo.split(';')
        lista_value = value.split(';')
        if(len(lista) ==3) :
                (hora,minuto,sec) = lista
                (ano,mes,dia) = lista_ano
                (value) = lista_value
                (KBIn,PktIn,KBOut,PktOut,ano2,hora2)=lista_completo
                hora = int(hora)-3
                if (hora <0):
                    hora = hora*(-1)
                sec2 = sec
                sec2 = sec2.replace('.','')
                milisec = int(sec2)
                sec = int(float(sec))
                date_time = datetime.datetime(int(ano),int(mes),int(dia),int(hora),int(minuto),int(sec),int(milisec)).timestamp()
                date_time2 = str(date_time).replace('.','')
                unix_time = date_time2	
                a = unix_time
                b = value
                cont = cont+1
                col1 = cont
                col2 = KBIn
                col3 = PktIn
                col4 = KBOut
                col7 = PktOut
                col5 = str(ano)+'-'+str(mes)+'-'+str(dia)+'-'+str(hora)+':'+str(minuto)+':'+str(sec)
                col6 = unix_time
                saida2 ='Id = '+str(col1)+'KBIn = '+str(col2)+' PktIn = '+str(col3)+' KBOut = '+str(col4)+' PktOut = '+str(col7)+' Data_original = '+str(col5)+' Unix_time = '+str(col6)
                saida =str(col1)+','+str(col2)+','+str(col3)+','+str(col7)+','+str(col4)+','+str(col5)+','+str(col6)
                print(saida2)			
                #print(lista_completo,'UNIX TIme convertido = ',unix_time,)
                if(cabecalho ==0):
                     arquivo.write('ID,KBIn,PktIn,KBOut,PktOut,Data_original,Unix_time  \n')
                     cabecalho=1
                arquivo.write(str(saida)+'\n')

arquivo.close()
csv_file.close()	

print("Fim Script Python3");













			


