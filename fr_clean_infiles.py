import re
import glob

'''remove duplicate paragraphs'''
def clean_infiles(text,outfile):
    num=0
    belege={}
    for elem in text:
        quelle=re.findall(r' \(.[^\)]*\)',str(elem))
        try:
            quelle=quelle[-1]
            zeitung=re.findall(r' \(.[^ ]* (.[^\)]*)\)',str(quelle))
            n_zeitung=str(zeitung).strip("[]'")
            neue_zeitung=re.sub(r', [0-9.]{10};',' ',str(n_zeitung))
            titel=(str(neue_zeitung)+' '+str(elem[:10])+str(len(elem)))
            if titel in belege:
                if belege[titel] != len(elem):
                    outfile.write(str(elem)+'\n\n')
                    num+=1
            elif titel not in belege:
                belege[titel]=len(elem)
                outfile.write(str(elem)+'\n\n')
                num+=1
            else:
                print('zeitung_error: '+str(zeitung))
        except:
            continue
    print("number of paragraphs in the file without duplicates: "+str(num))
    return outfile



