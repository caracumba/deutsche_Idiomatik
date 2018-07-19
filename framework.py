import glob
import os
import re
import csv

from textblob_de import TextBlobDE as TextBlob
from textblob_de.packages import pattern_de as pd

name=input("enter the filename without file extension: ")
name_txt=name+'.txt'
name_csv=name+'.csv'
name_outfile=str('clean_'+name+'.txt')
verb=input("enter the verb in infinitive form: ").lower()
component=input("enter the noun or other component (it must be only one word): ").lower()
components=[[str(component)]]

weka="data_weka.txt"

dir_name=name+'_outfiles'
os.makedirs(dir_name)
dir_name2=name+'_outfiles\modifications'
os.makedirs(dir_name2)

'''open the file, check its length'''
file = open(name_txt,'r',encoding='utf-8')
file_csv = os.path.join(dir_name, name_csv)
file_csv= open(file_csv,'w',encoding='utf-8')

outfile = os.path.join(dir_name, name_outfile)
outfile = open(outfile, 'w', encoding='utf-8')

text=file.read().strip().split('\n\n')
print("number of paragraphs in the file: "+str(len(text)))


'''create a csv-table for idioms modifications'''
name_columns=['Nr','werden+p2','part2','haben+p2','sein+p2','konj+sein+p2',
              'konj+haben+p2','konj+verb+praet',
              'infinitiv','futur',
              'muss','kann','darf','soll','will','mag',
              'müsse','könne','dürfe','solle','wolle','möge',
              'wuerde+inf',
              'ich','nicht','kein','meta+adv','meta+adj',
              'man+sagt','heissen','relpro+f','relpro+m',
              'relpro+n','relpro+pl',
              'frage','praet','praes','sub+attrib','verb+forms']

writer=csv.DictWriter(file_csv, fieldnames=name_columns)
writer.writeheader()

'''remove duplicate paragraphs'''
from fr_clean_infiles import clean_infiles
clean_infiles(text,outfile)

'''result for the idiom Farbe bekennen:
number of paragraphs sinked from 3531 to 3452'''

file.close()
outfile.close()

'''open the file without duplicates'''
name_clean_outfile='clean_'+name_txt
outfile = os.path.join(dir_name, name_clean_outfile)
infile= open(outfile, 'r', encoding='utf-8')
text2=infile.read().strip()

'''preprocessing of the text for a splitter;
add a white space in cases like:
bekennen.Mit '''
from fr_preproc_splitter import preproc_splitter
text2=preproc_splitter(str(text2))
text2=text2.split('\n\n')
print("number of paragraphs in the file after preprocessing: "+str(len(text2)))

n=0
from test_modifik import check_modifications

num=0
verbs={}

for elem in text2:
    n+=1
    '''Remove data about the source in every paragraph'''
    zeitung=re.findall(r' \([A-Z0-9]{3,6}.[A-Z0-9]{1,3}.[0-9:]{3,6} ..*\)',str(elem))
    elem_ohne_quelle=str(elem[:-len(zeitung[0])])

    blob = TextBlob(elem_ohne_quelle)
    sentences=blob.sentences
    for sentence in sentences:
        senten=re.sub(r"[«»„”“/./(/)/']","",str(sentence).lower())
        senten=re.sub(r'["]','',str(senten))
        blob2 = TextBlob(str(senten))
        tokens=blob2.tokens
        num_var=1
        for component in components:
            '''if the sentence contains idiom components,
                search for modifications
                create a csv-table containing all information
                about modifications found for the idiom'''
            name_var=str(component[0])
            identify=str(num_var)+'_'+name_var+'_'
            key='_'+str(n)+'_'+str(num_var)
            book={}
            book={'Nr':key}
            if component[0] in tokens:
                if component[-1] in tokens:
                    isub=tokens.index(component[0])
                    book,detect=check_modifications(sentence,senten,tokens,
                                        verb,component,n,num_var,book,isub)
                    if len(book)>2:
                        writer.writerow(book)
                        if detect==1:
                            num+=1
            num_var+=1

file_csv.close()
print('number of paragraphs containing the idiom: '+str(num))

'''Write files with paragraphs containing the idiom
for every modification in the created csv-table'''
from write_from_csv import write
write(name,name_outfile,name_csv,name_columns,components,dir_name,dir_name2)
             
'''Собираются статистические данные по полученным файлам'''
from statistics import statistic_files
name_s='statictics_'+name_txt
statistic_files(name_s,num,dir_name,dir_name2)

'''Анализируется csv-таблица: какие модификации и
какое сочетание модификаций самое частотное'''
from analyze_csv import csv
csv(name,dir_name)

'''Make a graph, save it to the folder outfiles'''
from stuff_for_plots_new import make_graph
idiom=input("enter the title of the graph (idiom): ")
name_s='statictics_'+name_txt
make_graph(name,name_s,num,idiom,dir_name,dir_name2,weka)

file.close()
file_csv.close()