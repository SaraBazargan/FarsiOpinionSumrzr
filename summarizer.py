import codecs
import re
from math import*
import operator
from functions import*
import graph as g
graph = g.Graph()

PRI = {}
""" PRI is a dictionary holds the positional information of words """
i = 0
############# reading the annotated file #############
list1 = []
all_of_text_list = []
""" all_of_text_list will contains the list of text sentesec which are
    splited by word
    """
fp2 = open('Fa_data_small.txt', 'r', encoding= 'utf-8')
txt2 = fp2.readlines()
for line in txt2:
    if line != '\n':
        sent_words = line.split()
        if sent_words not in all_of_text_list:
            all_of_text_list.append(sent_words)
    sent_size = len(sent_words)
    #print(i)
    ########### constructing the graph of text##########
    for j in range(sent_size):
        #PID = j
        #SID = i
        #if sent_words[j] != sent_words[j-1]:
        try:
            #if sent_words[j] in graph.vertices():
            PRI[sent_words[j]].append((i,j))
                #print(PRI)
        #else:
        except:
            graph.add_vertex(sent_words[j])
            PRI[sent_words[j]] = [(i,j)]
            #print(len(graph.vertices()))
        if j != 0:
            if [sent_words[j], sent_words[j-1]] not in graph.edges():
                graph.add_edge([sent_words[j], sent_words[j-1]])
            #print(sent_words[j-1], sent_words[j])      
    i += 1
#print(PRI)
#print(len(graph.edges()))
        
print('number of graph nodes: ', len(graph.vertices()))
fp2.close()
#print(graph.graf())
#print(graph.item("was/VBD"))
'''     

good = []
for i in graph.vertices():
    if len(PRI[i]) > 10:
        good.append(i)
f = []
for i in good:
    e = []
    for k in PRI[i]:
        (SID,PID) = k
        e.append(SID)
    f.append(e)
print(f)
'''


"""to create valid paths, we try to find the VSNs from whole the vertices. """
VSNs = []
for node in graph.vertices():
    if VSN(node, PRI):
        if node not in VSNs and len(PRI[node]) > 1:
            VSNs.append(node)
#print('number of start nodes: ', len(VSNs))
#print('threshold of PID to determine a VSN: 20')
#print('threshold of gap in discovering redundancies: 2')
#print('function to compute scores: Swt-len(W)')
cList = []
""" 'cList' will hold the candidate sentences for summary."""
for vsn in VSNs: 
    path = []
    path.append(vsn)
    #print('path: ', path)
    red = []
    """ red holds the sentences numbers to compute the redundancy."""
    redundancy = []
    """ redundancy holds the positional information -(SID,PID)- to find a valid next node."""
    n = 1
    """ n contains the number of words which added to the first word -VSN-""" 
    r = 0
    """ r contains the length of redundancy to compute scores."""
    #for i in range(len(PRI[vsn])):
    for i in PRI[vsn]:
        if i[0] not in red:
            red.append(i[0])
            redundancy.append(i)
    #print('redundancy: ', redundancy)
    traverse(cList, vsn, redundancy, red, path, PRI, n, r, all_of_text_list)
#print("num of candidate sentences: ", len(cList))
#print()

dic = {}
""" dic is a dictionary to put the candidate sentences and their scores in it.
    keys are sentences in string manner with POS tags were eliminated, and values
    are scores. the threshod for score could be set empirically. we set it to 5."""
for sent in cList:
    s = ''
    if sent[-1] >= 5:
        for word in sent[0: -1]:
            s = s + word.split('/')[0] + ' '
        dic[s] = sent[-1]
""" now we sort the dic by scores -or values of the dictionary-"""
sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
#print(sorted_dic)

'''
dic = {}
for sent in pool:
    s = ''
    for word in sent[0: -1]:
        s = s + word.split('/')[0] + ' '
    dic[s] = sent[-1]
sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
print(sorted_dic)

pool = [sorted_dic[0][0]]
for a in sorted_dic[1:]:
        if jaccard_similarity(a[0],sorted_dic[0][0]) < 0.5:
            pool.append(a[0])
print('len pool: ', len(pool))
#print(pool)
'''

###print('select up to ' , len(sorted_dic), 'sentences for your summary.')
##ss = int(input("enter the threshold for summary size: "))
""" ss is the threshold for summary size."""
##print()
##print()
##print('********** SUMMARY ***********')
##print()
""" up to desiered size of user we will print the high-score summary candidates."""
fp01 = open('kholase.txt', 'w', encoding= 'utf-8')
for i in range(len(sorted_dic)):
    #print(sorted_dic[-1-i][0])
    fp01.write(sorted_dic[-1-i][0])
    fp01.write('\n')

#print("well-done")






fp01.close()
