import glob
import os
import re
import csv
import matplotlib.pyplot as plt
import numpy as np

'''Create graphs for idioms'''
null=0
book={}

name_columns2=['werden+p2','part2','haben+p2','sein+p2','konj+sein+p2',
              'konj+haben+p2','konj+verb+praet',
              'infinitiv','futur',
              'muss','kann','darf','soll','will','mag',
              'müsse','könne','dürfe','solle','wolle','möge',
              'wuerde+inf',
              'ich','nicht','kein','meta+adv','meta+adj',
              'man+sagt','heissen','relpro+f','relpro+m',
              'relpro+n','relpro+pl',
              'frage','praet','praes']

def make_graph(name,name_s,num,idiom,dir_name,dir_name2,weka):
    name_s=os.path.join(dir_name, name_s)
    file = open(name_s,'r',encoding='utf-8')
    text=file.read().strip().split('\n')
    for elem in text:
        print(elem)
        if 'outfile' in str(elem):
            try:
                par=re.findall('_(.[^ _]*).txt',str(elem))
                number=re.findall('- (.[0-9.]*)%',str(elem))
                num=round(float(number[0]),2)
                book[par[0]]=num
            except:
                continue

    for item in name_columns2:
        if item not in book:
            book[item]=0

    x=[book['nicht']+book['kein'],book['infinitiv'],book['muss']+book['kann']+book['darf']+book['soll']+book['will']+
       book['mag']+book['müsse']+book['könne']+book['dürfe']+
       book['solle']+book['wolle']+book['möge'], book['konj+sein+p2']+book['konj+haben+p2']+
       book['konj+verb+praet']+book['wuerde+inf'],book['werden+p2'],null,
       book['futur'],book['part2'],book['haben+p2']+book['sein+p2'],book['praet'],
       book['praes']]
    x2=[book['nicht']+book['kein'],book['infinitiv'],book['muss']+book['kann']+book['darf']+book['soll']+book['will']+
       book['mag']+book['müsse']+book['könne']+book['dürfe']+
       book['solle']+book['wolle']+book['möge'], book['konj+sein+p2']+book['konj+haben+p2']+
       book['konj+verb+praet']+book['wuerde+inf'],book['werden+p2'],
       book['futur'],book['part2'],book['haben+p2']+book['sein+p2'],book['praet'],
       book['praes']]

    file_weka = open(weka,'r',encoding='utf-8')
    text_weka=file_weka.read().strip()
    file_weka.close()
    file_weka = open(weka,'w',encoding='utf-8')
    file_weka.write(text_weka+'\n'+str(idiom))
    for item in x2:
        file_weka.write(','+str(item))
    file_weka.write('\n')
    file_weka.close()

    y=['Negation','Infinitiv mit zu','Modalverben','Konjunktiv II',
       'Passiv',' ','Futur I',
       'Partizip 2','Perfekt', 'Präteritum', 'Präsens'] 
    y_pos=np.arange(len(y))
    plt.axis([0,100,-1,11])
    figure=plt.barh(y_pos, x,alpha=0.4)
    plt.grid(True)
    plt.yticks(y_pos,y)
    plt.xlabel('Belege (%)')
    plt.title('Idiom: '+str(idiom))
    filename='plot_'+str(name)+'.png'
    filename=os.path.join(dir_name, filename)
    plt.tight_layout(pad=0.0,h_pad=0.0,w_pad=0.0)
    plt.savefig(filename)
    plt.show()
    file.close()
    file_weka.close()