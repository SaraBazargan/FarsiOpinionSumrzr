""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""
import codecs
class Graph(object):

    def __init__(self, graph_dict={}):
        """ initializes a graph object """
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = edge
        #print(edge)
        vertex1 = edge.pop()
        if edge:
            # not a loop
            vertex2 = edge.pop()
        else:
            # a loop
            vertex2 = vertex1
        if vertex1 in self.__graph_dict:
            if vertex2 not in self.__graph_dict[vertex1]:
                self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if [neighbour, vertex] not in edges:
                    edges.append([vertex, neighbour])
        return edges

    def item(self, vertex):
        """ returns the edges comming after a "vertex"
            by an edge
        """
        #for vertex in self.__graph_dict:
        l = []
        if vertex in self.__graph_dict:
            l = self.__graph_dict[vertex]
            return l
        

    def graf(self):
        """ returns the graph constructed on text
            which is a dictionary. Keys are nodes and
            values are the nodes that connect with an
            arc to the key.
        """
        for k, v in self.__graph_dict.items():
            print (k, v)


if __name__ == "__main__":

    g = {}
    graph = Graph(g)
    PRI = {}
    """ PRI is a dictionary holds the positional information of words """
    i = 0
    ############# reading the annotated file #############
    list1 = []
    all_of_text_list = []
    """ all_of_text_list will contains the list of text sentesec which are
        splited by word
    """
    fp2 = open('Fa_data.txt', 'r', encoding= 'utf-8')
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
