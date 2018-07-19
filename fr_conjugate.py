from textblob_de import TextBlobDE as TextBlob
from textblob_de.packages import pattern_de as pd
import re

'''Create a dictionary of verb forms'''
def conjugate_verb(verb,verb_forms):
    verb2=''
    if verb=='ausschlagen':
        verb='schlagen'
        verb2='ausschlagen'
    if verb=='aufgeben':
        verb='geben'
        verb2='aufgeben'
    if verb=='austellen':
        verb='stellen'
        verb2='ausstellen'
    verb_forms['present_1_sg_indicative']=pd.conjugate(verb, tense=pd.PRESENT, person=1, number=pd.SG, mood=pd.INDICATIVE)
    verb_forms['present_2_sg_indicative']=pd.conjugate(verb, tense=pd.PRESENT, person=2, number=pd.SG, mood=pd.INDICATIVE)
    verb_forms['present_3_sg_indicative']=pd.conjugate(verb, tense=pd.PRESENT, person=3, number=pd.SG, mood=pd.INDICATIVE)
    verb_forms['present_1_pl_indicative']=pd.conjugate(verb, tense=pd.PRESENT, person=1, number=pd.PL, mood=pd.INDICATIVE)
    verb_forms['present_2_pl_indicative']=pd.conjugate(verb, tense=pd.PRESENT, person=2, number=pd.PL, mood=pd.INDICATIVE)
    verb_forms['present_3_pl_indicative']=pd.conjugate(verb, tense=pd.PRESENT, person=3, number=pd.PL, mood=pd.INDICATIVE)
    verb_forms['present_progressive_indicative']=pd.conjugate(verb, aspect=pd.PROGRESSIVE, mood=pd.INDICATIVE)
    verb_forms['present_1_pl_imperative']=pd.conjugate(verb, tense=pd.PRESENT, person=1, number=pd.PL, mood=pd.IMPERATIVE)
    verb_forms['present_2_sg_imperative']=pd.conjugate(verb, tense=pd.PRESENT, person=2, number=pd.SG, mood=pd.IMPERATIVE)
    verb_forms['present_2_pl_imperative']=pd.conjugate(verb, tense=pd.PRESENT, person=2, number=pd.PL, mood=pd.IMPERATIVE)
    verb_forms['present_1_sg_subjunctive']=pd.conjugate(verb, tense=pd.PRESENT, person=1, number=pd.SG, mood=pd.SUBJUNCTIVE)
    verb_forms['present_2_sg_subjunctive']=pd.conjugate(verb, tense=pd.PRESENT, person=2, number=pd.SG, mood=pd.SUBJUNCTIVE)
    verb_forms['present_3_sg_subjunctive']=pd.conjugate(verb, tense=pd.PRESENT, person=3, number=pd.SG, mood=pd.SUBJUNCTIVE)
    verb_forms['present_1_pl_subjunctive']=pd.conjugate(verb, tense=pd.PRESENT, person=1, number=pd.PL, mood=pd.SUBJUNCTIVE)
    verb_forms['present_2_pl_subjunctive']=pd.conjugate(verb, tense=pd.PRESENT, person=2, number=pd.PL, mood=pd.SUBJUNCTIVE)
    verb_forms['present_3_pl_subjunctive']=pd.conjugate(verb, tense=pd.PRESENT, person=3, number=pd.PL, mood=pd.SUBJUNCTIVE)
    verb_forms['past_1_sg_indicative']=pd.conjugate(verb, tense=pd.PAST, person=1, number=pd.SG, mood=pd.INDICATIVE)
    verb_forms['past_2_sg_indicative']=pd.conjugate(verb, tense=pd.PAST, person=2, number=pd.SG, mood=pd.INDICATIVE)
    verb_forms['past_3_sg_indicative']=pd.conjugate(verb, tense=pd.PAST, person=3, number=pd.SG, mood=pd.INDICATIVE)
    verb_forms['past_1_pl_indicative']=pd.conjugate(verb, tense=pd.PAST, person=1, number=pd.PL, mood=pd.INDICATIVE)
    verb_forms['past_2_pl_indicative']=pd.conjugate(verb, tense=pd.PAST, person=2, number=pd.PL, mood=pd.INDICATIVE)
    verb_forms['past_3_pl_indicative']=pd.conjugate(verb, tense=pd.PAST, person=3, number=pd.PL, mood=pd.INDICATIVE)
    verb_forms['past_progressive_indicative']=pd.conjugate(verb, tense=pd.PAST, aspect=pd.PROGRESSIVE, mood=pd.INDICATIVE)
    verb_forms['past_1_sg_subjunctive']=pd.conjugate(verb, tense=pd.PAST, person=1, number=pd.SG, mood=pd.SUBJUNCTIVE)
    verb_forms['past_2_sg_subjunctive']=pd.conjugate(verb, tense=pd.PAST, person=2, number=pd.SG, mood=pd.SUBJUNCTIVE)
    verb_forms['past_3_sg_subjunctive']=pd.conjugate(verb, tense=pd.PAST, person=3, number=pd.SG, mood=pd.SUBJUNCTIVE)
    verb_forms['past_1_pl_subjunctive']=pd.conjugate(verb, tense=pd.PAST, person=1, number=pd.PL, mood=pd.SUBJUNCTIVE)
    verb_forms['past_2_pl_subjunctive']=pd.conjugate(verb, tense=pd.PAST, person=2, number=pd.PL, mood=pd.SUBJUNCTIVE)
    verb_forms['past_3_pl_subjunctive']=pd.conjugate(verb, tense=pd.PAST, person=3, number=pd.PL, mood=pd.SUBJUNCTIVE)
    if ' ' in verb_forms['present_1_sg_indicative']:
        for item in sorted(verb_forms):
            if ' ' in verb_forms[item]:
                item2=str(item)+str('2')
                items=verb_forms[item].split()
                new_elem=items[1]+items[0]
                verb_forms[item2]=new_elem
    if verb2=='ausschlagen':
        for item in sorted(verb_forms):
            item1=verb_forms[item]+' '+'aus'
            item2='aus'+verb_forms[item]
            verb_forms[item]=item1
            new_item=item+'2'
            verb_forms[new_item]=item2
        verb_forms['past_progressive_indicative'] ='ausgeschlagen'
        verb='ausschlagen'
    if verb2=='aufgeben':
        for item in sorted(verb_forms):
            item1=verb_forms[item]+' '+'auf'
            item2='auf'+verb_forms[item]
            verb_forms[item]=item1
            new_item=item+'2'
            verb_forms[new_item]=item2
        verb_forms['past_progressive_indicative'] ='aufgegeben'
        verb='aufgeben'
    if verb2=='ausstellen':
        for item in sorted(verb_forms):
            item1=verb_forms[item]+' '+'aus'
            item2='aus'+verb_forms[item]
            verb_forms[item]=item1
            new_item=item+'2'
            verb_forms[new_item]=item2
        verb_forms['past_progressive_indicative'] ='ausgestellt'
        verb='ausstellen'
    if 'ss' in str(verb):
        for item in sorted(verb_forms):
            if 'ss' in verb_forms[item]:
                item3=str(item)+str('3')
                new_elem=re.sub('ss','ß',str(verb_forms[item]))
                verb_forms[item3]=new_elem
    if verb=='sitzen':
        for item in sorted(verb_forms):
            if 'ss' in verb_forms[item]:
                item3=str(item)+str('3')
                new_elem=re.sub('ss','ß',str(verb_forms[item]))
                verb_forms[item3]=new_elem       
    if verb=='aufreissen':
        verb_forms['past_progressive_indicative']='aufgerissen'
        verb_forms['past_1_pl_subjunctive']='rissen auf'
        verb_forms['past_2_pl_indicative2']='aufrisst'
        verb_forms['past_3_sg_subjunctive']='aufrisse'
        verb_forms['past_3_sg_subjunctive3']='risse auf'
        verb_forms['past_2_sg_indicative2']='aufrissest'
        verb_forms['past_3_pl_subjunctive23']='aufrissen'
        verb_forms['past_1_sg_indicative3']='riss auf'
        verb_forms['past_1_sg_subjunctive']='risse auf'
        verb_forms['past_2_pl_indicative3']='risst auf'
        verb_forms['past_2_sg_subjunctive']='risset auf'
    if verb=='gehen':
        for item in sorted(verb_forms):
            if verb_forms[item]=='gehn':
                verb_forms[item]='gehen'
    if verb=='hauen':
        for item in sorted(verb_forms):
            if verb_forms[item]=='haun':
                verb_forms[item]='hauen'
    if verb=='einrennen':
        for item in sorted(verb_forms):
            if 'past' in str(item):
                new_item=re.sub('enn','ann',str(verb_forms[item]))
                verb_forms[item]=new_item        
    return verb_forms