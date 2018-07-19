import re
import glob
import os

'''Write the number of paragraphs in all text files'''
def statistic_files(name,number,dir_name,dir_name2):
    file = os.path.join(dir_name, name)
    file = open(file,'w',encoding='utf-8')

    files={}
    names=glob.glob(dir_name2+r'\*.txt')
    for name in names:
        infile=open(name, 'r', encoding='utf-8')
        text=infile.read().strip()
        if len(text)>=1:
            text=text.split('\n\n')
            if name not in files:
                files[name] =len(text)
            else: 
                print(name)
        infile.close()
    m=0
    for item in sorted(files, key=files.get, reverse = True):
        procent=float(int(files[item])/number*100)
        file.write(str(m)+':'+' '+item+'  '+
                   str(files[item])+'  -  '+str(procent)+'%'+ '\n')         
        m+=1

    file.close()