import pprint

String="In this page I collect all easy one string guitar songs and tabs. I think that melodies on one, single string are very useful for beginners!"
dict={}
for ch in String.upper():
    dict.setdefault(ch,0)
    dict[ch]=dict[ch]+1
#pprint.pprint(dict)
tr=pprint.pformat(dict)
print(tr)