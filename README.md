# deutsche_Idiomatik

The program analyses corpus data acquired from [DeReKo](https://cosmas2.ids-mannheim.de/cosmas2-web/).
The data contains occurences of German idioms. 
The program searches for **modifications the idioms** undergo and makes statictical data on them.
It is designed for **frequent idioms**, for which the researcher can found thousands of contexts 
so that to view them all would be too time-consuming.

## Steps:
1) First you need to obtain a file from DeReKo.
2) The rtf-file must be converted to a txt-file.
The header of the text must be removed, so the file should begin with the first context.
3) Open the program framework.py and enter the verb and the nominal component.
If there are lexical variants, seperate searches should be made.
