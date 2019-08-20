import networkx as nx
import string
import sys
import codecs
import matplotlib.pyplot as plt

dG = nx.DiGraph()

fp2 = open('Fa_data_small.txt', 'r', encoding= 'utf-8')
txt2 = fp2.readlines()
for line in txt2:
    if line != '\n':
        sent_words = line.split()
        for i, word in enumerate(sent_words):
            try:
                next_word = sent_words[i + 1]
                if not dG.has_node(word):
                    dG.add_node(word)
                    dG.node[word]['count'] = 1
                else:
                    dG.node[word]['count'] += 1
                if not dG.has_node(next_word):
                    dG.add_node(next_word)
                    dG.node[next_word]['count'] = 0

                if not dG.has_edge(word, next_word):
                    dG.add_edge(word, next_word, weight=sys.maxsize - 1)
                else:
                    dG.edge[word][next_word]['weight'] -= 1
            except IndexError:
                if not dG.has_node(word):
                    dG.add_node(word)
                    dG.node[word]['count'] = 1
                else:
                    dG.node[word]['count'] += 1
            except:
                raise



fp2.close()
'''
for node in dG.nodes():
    print('%s:%d\n' % (node, dG.node[node]['count']))

for edge in dG.edges():
    print('%s:%d\n' % (edge, sys.maxsize - dG.edge[edge[0]][edge[1]]['weight']))


'''

pos = nx.spring_layout(dG)
 
edge_labels = { (u,v): d['weight'] for u,v,d in dG.edges(data=True) }
 
nx.draw_networkx_nodes(dG,pos,node_size=700)
nx.draw_networkx_edges(dG,pos)
nx.draw_networkx_labels(dG,pos)
nx.draw_networkx_edge_labels(dG,pos,edge_labels=edge_labels)
 
plt.title("Graph of Text")
plt.axis('off')
plt.draw()
#plt.savefig('output.png')
plt.show()
'''
nx.draw(dG, pos=nx.spring_layout(dG))
#nx.draw_network_nodes(dG, pos=nx.spring_layout(dG))
plt.draw()
plt.show()
'''
