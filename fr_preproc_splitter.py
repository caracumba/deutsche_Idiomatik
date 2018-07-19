import re
import glob

'''preprocessing of the text for a splitter;
add a white space in cases like:
bekennen.Mit '''
def preproc_splitter(text2):
    it=re.finditer(r' [A-ZÄÖÜa-zäöüß"-]{2,}(\.)[A-ZÄÖÜa-zäöüß-„«»0-9]{1,}',text2)
    for m in it:
        old=str(m.group(0))
        new=re.sub(r'\.','. ',str(old))
        text2=re.sub(old,str(new), text2)
    return text2



