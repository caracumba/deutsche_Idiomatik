from textblob_de import TextBlobDE as TextBlob
from textblob_de.packages import pattern_de as pd

'''Create lists of modal verbs'''
def conjugate_verb(verb,verb_forms):
    verb_forms.append(pd.conjugate(verb, tense=pd.PRESENT, person=1, number=pd.SG, mood=pd.INDICATIVE))
    verb_forms.append(pd.conjugate(verb, tense=pd.PRESENT, person=2, number=pd.SG, mood=pd.INDICATIVE))
    verb_forms.append(pd.conjugate(verb, tense=pd.PRESENT, person=1, number=pd.PL, mood=pd.INDICATIVE))
    verb_forms.append(pd.conjugate(verb, tense=pd.PRESENT, person=2, number=pd.PL, mood=pd.INDICATIVE))
    verb_forms.append(pd.conjugate(verb, tense=pd.PRESENT, person=1, number=pd.SG, mood=pd.SUBJUNCTIVE))
    verb_forms.append(pd.conjugate(verb, tense=pd.PRESENT, person=2, number=pd.SG, mood=pd.SUBJUNCTIVE))
    verb_forms.append(pd.conjugate(verb, tense=pd.PAST, person=1, number=pd.SG, mood=pd.INDICATIVE))
    verb_forms.append(pd.conjugate(verb, tense=pd.PAST, person=2, number=pd.SG, mood=pd.INDICATIVE))
    verb_forms.append(pd.conjugate(verb, tense=pd.PAST, person=1, number=pd.PL, mood=pd.INDICATIVE))
    verb_forms.append(pd.conjugate(verb, tense=pd.PAST, person=1, number=pd.SG, mood=pd.SUBJUNCTIVE))
    verb_forms.append(pd.conjugate(verb, tense=pd.PAST, person=2, number=pd.SG, mood=pd.SUBJUNCTIVE))
    verb_forms.append(pd.conjugate(verb, tense=pd.PAST, person=1, number=pd.PL, mood=pd.SUBJUNCTIVE))
    verb_forms.append(pd.conjugate(verb, tense=pd.PAST, person=2, number=pd.PL, mood=pd.SUBJUNCTIVE))
    return verb_forms

modal_verbs=['müssen','können','dürfen','sollen','wollen','mögen']
lists=[]
for modal in modal_verbs:
    name=[]
    conjugate_verb(modal,name)
    lists.append(name)
print(lists)
