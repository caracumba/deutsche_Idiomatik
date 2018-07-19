import glob
import os
import re
import csv

'''For every idiom write a file with its occurences 
in Präsens and Präteritum'''

def write(name,name_columns,verbs):
    name_txt='clean_'+str(name)+'.txt'
    name_csv=str(name)+'.csv'
    file_txt = open(name_txt,'r',encoding='utf-8')
    file_csv=  open(name_csv,'r',encoding='utf-8')
    csv=file_csv.read().split('\n\n')
    text=file_txt.read().split('\n\n')
    num=1
    count=0
    for it in verbs:
        file_name=str('!outfile_'+str(name)+'_'+str(num)+'_verbs_'+str(it)+'.txt')
        outfile_belege = open(file_name, 'w', encoding='utf-8')
        for elem in csv[1:-1]:
            elem=elem.split(',')
            number=re.findall('_(..*)_',str(elem[0]))
            number=int(number[0])
            verb=elem[-1]
            verb_items=verb.split('|')
            for item in verb_items:
                item=item.strip()
                if item==it:
                    outfile_belege.write(text[number-1]+'\n\n')        
        outfile_belege.close()  
    file_txt.close()
    file_csv.close()
