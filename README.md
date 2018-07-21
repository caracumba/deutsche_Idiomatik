# deutsche_Idiomatik

The program analyses corpus data acquired from [DeReKo](https://cosmas2.ids-mannheim.de/cosmas2-web/).
The data contains occurences of German idioms. 
The program searches for **modifications the idioms** undergo and makes statictical data on them.
It is designed for frequent idioms, which the researcher can find thousands of contexts for and therefore their manual processing would be too time-consuming.

## Steps:
1) First download a file from DeReKo, containing an idiom, which usage you want to investigate. Below you can find some examples for queries.
2) The obtained rtf-file must be converted into a txt-file.
The header of the text must be removed, so that the file begins with the first context.
3) Open the program framework.py and enter the verb and the nominal component.
If there are lexical variants, separate searches should be made.

## Notes:

The queries should be made in such a way that possible modifications are not excluded from the results. E.g. the idiom *auf den Grund gehen* ‘to get to the bottom of sth.’. The query looks as follows: (auf / +w2 Grund) / s0 &gehen. It means that gehen can be used in any form and have any position in a sentence, besides, any token can appear between *auf* and *Grund*. The paragraphs where the idioms occur can be exported. DeReKo doesn't allow you to export over 10000 examples, but this number is enough for studying the usage of idioms in written texts.
The queries have not been automated for the following reasons: In every case the researcher should decide how to formulate queries so that the obtained data contain the minimum sentences where idiom’s components are used in direct and not idiomatic meaning, but at the same time don’t exclude possible modifications. For instance, the idiom *sich (D) ins Fäustchen lachen* ‘to laugh in one's sleeve’ contains the noun *Fäustchen*, which is not that frequent. That is why if we just search for sentences, where both components occur together, it will be enough. The situation is different with the idiom *mit den Wölfen heulen* ‘to do in Rome as the Romans do’. If we search for lemmas *Wolf* ‘wolf’ and *heulen* ‘to howl’ which occur in the same sentence, we will find a lot of examples where there is no idiom. Therefore, the query should be restricted. E.g. (mit /+w3 Wölfen) /s0 &heulen, which means that the lemma *heulen* occurs in one sentence with word forms *mit* and *Wölfen*, the maximal distance between them makes two words.
