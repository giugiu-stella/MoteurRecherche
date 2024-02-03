import re

PATTERN_TOKEN = re.compile('[^\\w]+')

"""def tokenarisation(livre : str) -> list[str]:
    mots = livre.lower()
    l = re.split(PATTERN_TOKEN, mots)
    return [mot for mot in l if len(mot) >= 3]
    

def occurences_mots(mots : list[str]) -> dict[str, int]:
    occurrences = {}
    for mot in mots :
        if mot in occurrences:
            occurrences[mot] += 1
        else:
            occurrences[mot] = 1
    return occurrences

def tokenarisation_occurences(livre : str) -> dict[str, int] :
    return occurences_mots(tokenarisation(livre))"""

def jaccard_distance(occurneces_text1 , occurneces_text2 ) -> float :
    numerateur = 0
    denominateur = 0
    for w in occurneces_text1.keys() & occurneces_text2.keys():
        k1 = 0 if w not in occurneces_text1.keys() else occurneces_text1[w]
        k2 = 0 if w not in occurneces_text2.keys() else occurneces_text2[w]
        numerateur += abs(k1 - k2) 
        denominateur += max(k1, k2)
    

    return numerateur / denominateur if denominateur != 0 else 1
    

def jaccard_similarity(text1, text2 ) -> float:
    return 1 - jaccard_distance(text1, text2)
