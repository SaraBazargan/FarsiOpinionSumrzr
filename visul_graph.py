import codecs
import nltk

fp2 = open('Fa_data_small.txt', 'r', encoding= 'utf-8')
txt2 = fp2.readlines()
all_words = []
for line in txt2:
    if line != '\n':
        sent_words = line.split()
        for word in sent_words:
            if word not in all_words:
                all_words.append(word)
print(len(all_words))




matris = []
for i in all_words:
    for j in all_words:
        matris.append((i,j))

for line in txt2:
    if line != '\n':
        sent_words = line.split()
        bigrams = nltk.bigrams(sent_words)
        for bi in bigrams:
            if bi in matris
'''    
            
        
for line in txt2:
    if line != '\n':
        sent_words = line.split()
        bigrams = nltk.bigrams(sent_words)
        for bi in bigrams:
            if bi in 
            
'''
    


fp2.close()
