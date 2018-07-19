import glob
import os
import re
import csv

'''Analyze the csv-table: create a frequency list
for all modifications and their combinations'''
def csv(name,dir_name):
    name_csv=name+'.csv'
    name_csv=os.path.join(dir_name, name_csv)
    outfile='outfile_'+name+'.txt'
    outfile2='2outfile_'+name+'.txt'

    outfile=os.path.join(dir_name, outfile)
    outfile2=os.path.join(dir_name, outfile2)

    file = open(name_csv,'r',encoding='utf-8')
    text=file.read().strip().split('\n\n')
    outfile = open(outfile, 'w', encoding='utf-8')
    outfile2 = open(outfile2, 'w', encoding='utf-8')


    name_columns=['Nr','werden+p2','part2','haben+p2','sein+p2','konj+sein+p2',
                  'konj+haben+p2','konj+verb+praet',
                  'infinitiv','futur',
                  'muss','kann','darf','soll','will','mag',
                  'müsse','könne','dürfe','solle','wolle','möge',
                  'wuerde+inf',
                  'ich','nicht','kein','meta+adv','meta+adj',
                  'man_sagt','heissen','relpro+f','relpro+m',
                  'relpro+n','relpro+pl',
                  'frage','sub+attrib','verb+forms']
    book={}
    for elem in text[1:]:
        if elem!='\n':
            if elem!='':
                row=elem.split(',')
                new_row=''
                for item in row[1:-2]:
                    if item=='':
                        item='0'
                    new_row=new_row+item
                new=new_row.strip('"')
                outfile2.write(str(row[0])+' '+new+'\n')
                if new in book:
                    book[new]+=1
                else:
                    book[new]=1

    for item in sorted(book, key=book.get, reverse = True):
        if int(book[item])==1:
            break
        outfile.write(item+' '+str(book[item])+'\n')
        m=1
        for elem in item:
            if elem=='1':
                outfile.write(name_columns[m]+'\n')
            m+=1

    file.close()
    outfile.close()
    outfile2.close()