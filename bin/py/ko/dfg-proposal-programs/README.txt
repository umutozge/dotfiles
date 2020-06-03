DFG Project Proposal "Special Indefinites in Discourse"
Python programs list (alphabetical order)


analyzeAgreement.py
-------------------

This program is used to compute chance corrected coefficients of annotator
agreement. It currently works for agreement computation for two annotators.

analyzeAnnotation.py
-------------------

This program takes as input annotated MMAX files (xml) and constructs a table for
each annotation category, which tabulates the responses given by each annotator
to every token in the annotated sample. The output is used as input for
agreement computation.

DepParse.py
----------

This program manages the dependency parsing process. It makes necessary format
conversions (e.g.\ xml to ConLL and back) and constructs an xml coded dependency
treebank from the Maltparse output.


deptools.py
----------

This is a module used by DepParse.py

listMarkables.py
----------------

This program takes as input annotated MMAX files (xml) and constructs a
tabulated report for each markable. 

md2xml.py
---------
This converts the output of the morphological disambiguator (an external
program) to xml.


mergeMarkables.py
----------------
MMAX gets too slow for more than 10 discourses. Therefore the annotation is
carried out in batches of 8-10 discourses.  This program collects together the
output of several annotation batches. 

searchTreeBank.py
----------------
This program is used to run searches over dependency treebanks constructed as
output of DepParse.py.


toMMAXFilter.py
---------------
This program uses searchTreeBank.py to search and filter relevant discourses --
namely discourses with a sentence containing an indefinite direct object. It
brings to the screen each match for the annotator to accept or reject the
discourse for further annotation.


