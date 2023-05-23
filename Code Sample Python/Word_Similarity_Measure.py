import numpy as np
from numpy.linalg import norm
path = r"D:\LT\Python\NLP\Word_Similarity_master\word2vec\W2V_150.txt"


def getVect(word):
    f = open(path, "r", encoding='utf-8')
    for i in f:
        s = i.split()
        if len(s) > 150 and s[0].strip() == word:
            u2 = []
            for j in range(151):
                if j == 0: 
                    continue
                else: u2.append(float(s[j]))
            f.close()
            return u2

def getCosineSimilarity(word1, word2):
    u1 = getVect(word1)
    u2 = getVect(word2)
    sim = np.dot(u1, u2)/(norm(u1)*norm(u2))
    return sim

def K_nearest_word(word , k):
    dicVect = []
    dicWord = {'a': 0}
    f = open(path, "r", encoding='utf-8')
    count = 0
    for i in f:
        if count > 1000:
            break
        s = i.split()
        if len(s) > 150:
            dicVect.append(s[0].strip()) # word 1
            count+=1
        
    f.close()
    for i in dicVect:
        dicWord[i] = getCosineSimilarity(i, word)
    dicWord = dict(sorted(dicWord.items(), key=lambda x:x[1], reverse=True))
    res = []
    count = 0
    for i in dicWord:
        if count == k:
            break
        res.append(i)
        print(dicWord[i])
        count+=1
    return res


print(K_nearest_word("bán", 10))


