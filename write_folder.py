import os
import re

dir_name='data'
os.makedirs(dir_name)

def write(name,name_txt,name_csv,name_columns,components):
    file_txt = open(name_txt,'r',encoding='utf-8')
    file_csv=  open(name_csv,'r',encoding='utf-8')
    csv=file_csv.read().split('\n\n')
    text=file_txt.read().split('\n\n')
    num=1
    sub_attrib={}
    verbs={}
    count=0
    for comp in components:
        col=1
        for item in name_columns[1:-2]:
            file_name=str('!outfile_'+str(name)+'_'+str(num)+'_'+str(item)+'.txt')
            #outfile_belege = open(file_name, 'w', encoding='utf-8')
            outfile = os.path.join(dir_name, file_name)
            outfile_belege=open(outfile,'w', encoding='utf-8')
            for elem in csv[1:-1]:
                elem=elem.split(',')
                number=re.findall('_(..*)_',str(elem[0]))
                number=int(number[0])
                if col==1:
                    sub_at=elem[-2]
                    verb=elem[-1]
                    verb_items=verb.split('|')
                    if sub_at in sub_attrib:
                        sub_attrib[sub_at]+=1
                    if sub_at not in sub_attrib:
                        sub_attrib[sub_at]=1
                    for item in verb_items:
                        if len(item)>1:
                            item=item.strip()
                            if item in verbs:
                                verbs[item]+=1
                            if item not in verbs:
                                verbs[item]=1
                if elem[col]==str(num):
                    count+=1
                    outfile_belege.write(text[number-1]+'\n\n')          
            outfile_belege.close()  
            col+=1
        num+=1
    file_txt.close()
    file_csv.close()
    print("number of found  modifications: " +str(count))
