
strs=["eat","tea","tan","ate","nat","bat"]
Anagrams={}
for word in strs:
    key="".join(sorted(word))
    if key not in Anagrams:
       Anagrams[key]=[]
    Anagrams[key].append(word)
    print(Anagrams)

