from collections import defaultdict

def group_anagrams(strs):
    anagram_map = defaultdict(list)
    
    for word in strs:
        key = tuple(sorted(word))
        anagram_map[key].append(word)
    
    return list(anagram_map.values())
