import glob
import os
import re
import csv

from textblob_de import TextBlobDE as TextBlob
from textblob_de.packages import pattern_de as pd

'''create a dictionary with all possible verb forms'''
from fr_conjugate import conjugate_verb

'''program fr_conjugate_mv creates lists of modal verbs'''
modals=[['muss', 'musst', 'müssen', 'müsst', 'musste',
         'musstest', 'mussten'],
        ['kann', 'kannst', 'können', 'könnt',
         'konnte', 'konntest', 'konnten'],
        ['darf', 'darfst', 'dürfen', 'dürft',
         'durfte', 'durftest', 'durften'],
        ['soll', 'sollst', 'sollen', 'sollt',
         'sollte', 'solltest', 'sollten', 'solltet'],
        ['will', 'willst', 'wollen', 'wollt',
         'wollte', 'wolltest', 'wollten', 'wolltet'],
        ['mag', 'magst', 'mögen', 'mögt', 
         'mochte', 'mochtest', 'mochten']]
modals_konj=[['müsse','müssest', 
         'müsste', 'müsstest', 'müssten', 'müsstet'],
        ['könne','könnest',
         'könnte', 'könntest', 'könnten', 'könntet'],
        ['dürfe','dürfest', 
         'dürfte', 'dürftest', 'dürften', 'dürftet'],
        ['solle','sollest'],
        ['wolle','wollest'],
        ['möge', 'mögest','möchte',
         'möchtest', 'möchten', 'möchtet']]
futur=['werde','wirst','wird','werden','werdet']

'''Metacommunicative adjectives and adverbs'''
man_sagt=['sagt man','man sagt']
meta_adj=['sprichwörtlich',
          'übertragen', 'berühmt', 'buchstäblich',
          'notorisch', 'figurativ', 'bildlich', 'bildhaft']

konj_wuerde=['würde','würdest','würdet','würden']
heissen=['heisst','heißt','hiesse','hieße']
konj_sein=['wäre','wären','sei','seien']
konj_haben=['hätte','hätten']
konj=konj_wuerde+konj_sein+konj_haben

'''Auxiliary verbs'''
werden=['wird','werde','wirst','werden','werdet',
        'wurde','wurden','wurdest','worden'] #geworden
haben=['haben','hast','hat','habe','habt','hatte',
       'hattest','hatten','hattet']
sein=['sind','bist','ist','bin','seid',
      'war','warst','waren','wart','gewesen']

'''Relative clauses'''
relpro_f=['der','die','deren']
relpro_m=['der','dessen','dem','den']
relpro_n=['das','dessen','dem']
relpro_pl=['die','deren','denen']
'''Negation'''
nicht='nicht'
kein=['kein','keines','keinem','keinen','keine','keiner']

def disambiguate_verb(i1,isub,tokens):
    '''Restrictions on unwanted tokens
     between two components'''
    i2=isub
    if i1>i2:
        tokens2=tokens[i2:i1]
    if i1<i2:
        tokens2=tokens[i1:i2]
    if 'und' not in tokens2:
        if ',' not in tokens2:
            if ':' not in tokens2:
                if ';' not in tokens2:
                    if 'oder' not in tokens2:
                        return 1

def disambiguate(i1,i2,tokens,isub):
    '''Restrictions on unwanted tokens
     between three components'''
    if i1>=i2:
        tokens2=tokens[i2:i1]
    if i1<i2:
        tokens2=tokens[i1:i2]
    if isub>=i1:
        tokens3=tokens[i1:isub]
    if isub<i1:
        tokens3=tokens[isub:i1]
    if 'und' not in tokens2:
        if ',' not in tokens2:
            if ':' not in tokens2:
                if ';' not in tokens2:
                    if 'oder' not in tokens2:
                        if ',' not in tokens3:
                            if ';' not in tokens3:
                                if 'und' not in tokens3:
                                    if 'oder' not in tokens3:
                                        if ':' not in tokens3:
                                            return 1
    else:
        return 0

def find_sub_attrib(book,component,tokens):
    '''Create a frequency list of elements,
        preceding the nominal component'''
    i_sub=tokens.index(component[0])
    if int(i_sub-1)>=0:
        sub_at=tokens[int(i_sub-1)]
    elif int(i_sub-1)<0:
        sub_at='none'
    if sub_at!=' ':
        book['sub+attrib']=sub_at
    elif sub_at==' ':
        sub_at=tokens[int(i_sub-2)]
        book['sub+attrib']=sub_at
    return book

def check_modifications(sentence,senten,tokens,verb,component,n,num_var,book,isub):
    '''Search for idiom modifications in every sentence'''
    verb_forms={}
    book['verb+forms']=''
    prefix=''
    detect=0
    conjugate_verb(verb, verb_forms)
    verb_ich=[verb_forms['present_1_sg_indicative'],
              verb_forms['past_1_sg_indicative'],
              verb_forms['past_progressive_indicative']]
    verb_inf=verb_forms['present_1_pl_indicative']
    verb_pl=verb_forms['present_1_pl_indicative']
    if ' ' in verb_inf:
        elems=verb_inf.split()
        verb_inf=elems[1]+elems[0]
        prefix=' '+elems[1]
    if ' ' not in verb_inf:
        infinitiv='zu '+verb_inf
    if ' ' in verb_pl:
        elems=verb_pl.split()
        infinitiv=elems[1]+'zu'+elems[0]
        if infinitiv=='aufzureissen':
            infinitiv='aufzureißen'
    verb_forms['infinitiv']=infinitiv
    partizip2=verb_forms['past_progressive_indicative']
    partizip1=verb_forms['present_progressive_indicative']
    verb3sgsubj=verb_forms['past_3_sg_subjunctive']
    verb3sgind=verb_forms['past_3_sg_indicative']
    for token in tokens:
        if str(token).strip() in str(verb_forms.values()).strip():
            if str(token) not in str(prefix):
                new_token=str(token)+str(prefix)
                try:
                    value=list(verb_forms.keys())[list(verb_forms.values()).index(new_token)]
                    if 'present' in str(value):
                        if verb_inf not in tokens:
                            book['praes']= num_var
                    if 'past' in str(value):
                        if 'progressive' not in str(value):
                            book['praet']= num_var
                except:
                    continue

            
    if partizip2 in tokens:
        detect=1
        i1=tokens.index(partizip2)
        for w in werden:
            if w in tokens:
                i2=tokens.index(w)
                if disambiguate(i1,i2,tokens,isub)==1:
                    book['werden+p2']= num_var
                    book['verb+forms']= str(book['verb+forms'])+'| '+'werden '+partizip2
        for h in haben:
            if h in tokens:
                i2=tokens.index(h)
                if disambiguate(i1,i2,tokens,isub)==1:
                    book['haben+p2']= num_var
                    book['verb+forms']=str(book['verb+forms'])+'| '+'haben '+partizip2
        for s in sein:
            if s in tokens:
                i2=tokens.index(s)
                if disambiguate(i1,i2,tokens,isub)==1:
                    book['sein+p2']= num_var
                    book['verb+forms']=str(book['verb+forms'])+'| '+'sein '+partizip2
        for konj_s in konj_sein:
            if konj_s in tokens:
                i2=tokens.index(konj_s)
                if disambiguate(i1,i2,tokens,isub)==1:
                    book['konj+sein+p2']= num_var
                    book['verb+forms']=str(book['verb+forms'])+'| '+'konj sein '+partizip2
        for konj_h in konj_haben:
            if konj_h in tokens:
                i2=tokens.index(konj_h)
                if disambiguate(i1,i2,tokens,isub)==1:
                    book['konj+haben+p2']= num_var
                    book['verb+forms']=str(book['verb+forms'])+'| '+'konj haben '+partizip2
        if partizip2!=verb_forms['present_3_sg_indicative']:
            if len(book['verb+forms'])==0:
                book['verb+forms']=str(book['verb+forms'])+'| '+'partizip 2 '+partizip2
                book['part2']= num_var
    if verb3sgsubj!=verb3sgind:
        if verb3sgsubj in tokens:
            detect=1
            book['konj+verb+praet']= num_var
            book['verb+forms']=str(book['verb+forms'])+'| '+verb3sgsubj
    if infinitiv in senten:
        detect=1
        book['infinitiv']= num_var
        book['verb+forms']=str(book['verb+forms'])+'| '+infinitiv
    if verb_inf in tokens:
        detect=1
        search_praes=1
        i1=tokens.index(verb_inf)
        for fut in futur:
            if fut in tokens:
                i2=tokens.index(fut)
                if disambiguate(i1,i2,tokens,isub)==1:
                    book['futur']= num_var
                    book['verb+forms']=str(book['verb+forms'])+'| '+'werden '+verb_inf
                    search_praes=0
        for mod in modals:
            for m in mod:
                if m in tokens:
                    i2=tokens.index(m)
                    if disambiguate(i1,i2,tokens,isub)==1:
                        mv=mod[0]
                        book[mv]= num_var
                        book['verb+forms']=str(book['verb+forms'])+'| '+'modalverb '+verb_inf
                        search_praes=0
        for mod_k in modals_konj:
            for m in mod_k:
                if m in tokens:
                    i2=tokens.index(m)
                    if disambiguate(i1,i2,tokens,isub)==1:
                        mvk=mod_k[0]
                        book[mvk]= num_var
                        book['verb+forms']=str(book['verb+forms'])+'| '+'konj modalverb '+verb_inf
                        search_praes=0
        for wuerde in konj_wuerde:
            if wuerde in tokens:
                i2=tokens.index(wuerde)
                if disambiguate(i1,i2,tokens,isub)==1:
                    book['verb+forms']=str(book['verb+forms'])+'| '+'wuerde '+verb_inf
                    book['wuerde+inf']=num_var
                    search_praes=0
        if search_praes==1:
            book['praes']= num_var
    if 'ich' in tokens:
        i1=tokens.index('ich')
        for i in verb_ich:
            elems=i.split()
            if elems[0] in tokens:
                if elems[-1] in tokens:
                    i2=tokens.index(elems[0])
                    if disambiguate(i1,i2,tokens,isub)==1:
                        book['ich']= num_var
    for item in sorted(verb_forms):
        if book['verb+forms']!='':
            verb=book['verb+forms']
            v=verb.split()
            v=v[-1].split()
        else:
            v=verb_forms[item].split()
        if v[0] in tokens:
            if v[-1] in tokens:
                i1=tokens.index(v[0])
                if disambiguate_verb(i1,isub,tokens)==1:
                    detect=1
                    if len(book['verb+forms'])==0:
                        if v[0]!=v[-1]:
                            book['verb+forms']=str(book['verb+forms'])+'| '+v[0]+' '+v[-1]
                        else:
                            book['verb+forms']=str(book['verb+forms'])+'| '+v[0]
                    find_sub_attrib(book,component,tokens)
                    if nicht in tokens:
                        i2=tokens.index('nicht')
                        if disambiguate(i1,i2,tokens,isub)==1:
                            book['nicht']=num_var
                    for k in kein:
                        seq=str(k)+' '+str(component[0])
                        if seq in senten:
                            book['kein']=num_var
                
                    for mf in meta_adj:
                        if mf in tokens:
                            book['meta+adv']=num_var
                        if mf in senten:
                            if mf not in tokens:
                                book['meta+adj']= num_var
                    for ms in man_sagt:
                        if ms in senten:
                            book['man+sagt']= num_var
                    for hei in heissen:
                        if hei in tokens:
                             book['heissen']= num_var
                    if '?' in senten:
                        i2=tokens.index('?')
                        if i2>i1:
                            if disambiguate(i1,i2,tokens,isub)==1:
                                book['frage']=num_var
    return book,detect
