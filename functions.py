import graph as g
graph = g.Graph()
def VSN(node, PRI):
    """ Valid Start Node-VSN: uses positional information
        of a node to determine if it is a VSN. Checks if
        average(PID)< threshold(vsn). threshold could be
        set empirically
    """
    s = 0
    count = 0
    word_pos = node.split('/')
    if len(PRI[node]) > 2 and word_pos[1] in ["N", "ADV", "AJ"]:
        for i in PRI[node]:
            s = s + PRI[node][count][1]
            count += 1
        if s/count < 20:
            return True
    

def VEN(node):
    """ Valid End Node-VEN: uses natural ending points
        such as period, comma and coordinating conjunctions
        to find a VEN.
    """
    word_pos = node.split('/')
    if word_pos[1] in ["V", "AJ"]:
        return True
    else:
        return False


def find_matches(pattern_list, search_list):
    """ finds a path in set of sentence which is redundant
        in the text so yelids sentences that contains an
        anchor.
    """
    cursor_list = []
    found = []
    for element in search_list:
        cursors_to_kill = []
        for cursor_index in range(len(cursor_list)):
            if element == pattern_list[cursor_list[cursor_index]]:
                cursor_list[cursor_index] += 1
                if cursor_list[cursor_index] == len(pattern_list):
                    found.append(pattern_list)
                    cursors_to_kill.append(cursor_index)
            else:
                cursors_to_kill.append(cursor_index)
        cursors_to_kill.reverse()
        for cursor_index in cursors_to_kill:
            cursor_list.pop(cursor_index)
        if element == pattern_list[0]:
            cursor_list.append(1)
    return found

def valid_path(path, PRI):
    """ a path which starts with a VSN and ends with a VEN and
        is connected by a set of directed edges and finally
        satisfies a set of well-formed POS constraints. rules
        are application specific and I ignored this time.
    """
    if VSN(path[0], PRI) and VEN(path[-1]):
        for i in range(len(path)-1):
            if [path[i],path[i+1]] not in graph.edges():
                return False
            else:
                return True
                #s = ''
                #for word in path:
                    #s = s + word + ' '
                #print(s)
                #if re.match(r'.*(/NN)+.*(/VB(\W)*)+.*(/JJ)+.*', s):
                #if find_matches(r'.*(/NN)+.*(/VB(\W)*)+.*(/JJ)+.*', s):
                    #return True
                #elif find_matches(r'.*(/JJ)+.*(/TO)+.*(/VB(\W)*)+.*', s):
                    #return True
                #elif find_matches(r'.*(/RB)+.*(/JJ)+.*(/NN)+.*', s):
                    #return True
                #elif find_matches(r'.*(/RB)+.*(/IN)+.*(/NN)+.*', s):
                    #return True
                #else:
                    #return False
                
'''
def redundancy(path):
    """ returns the number of times a path repeated.
    """
    overall_redundancy = []
    for i in range(len(path)-1): 
        redundancy_of_sents = []
        #print(PRI[path[i]])
        for j in PRI[path[i]]: 
            (SID,PID) = j
            if (SID, PID+1) in PRI[path[i+1]] and SID not in redundancy_of_sents:
                redundancy_of_sents.append(SID)
            elif (SID, PID+2) in PRI[path[i+1]] and SID not in redundancy_of_sents:
                redundancy_of_sents.append(SID)
            #elif (SID, PID+3) in PRI[path[i+1]] and SID not in redundancy_of_sents:
                #redundancy_of_sents.append(SID)
        overall_redundancy.append(redundancy_of_sents)
        #print(overall_redundancy)
    if len(overall_redundancy) > 1:
        for k in range(1,len(overall_redundancy)):
            count = len(set(overall_redundancy[0]).intersection(overall_redundancy[k]))
            #print(count)
    else:
        count = len(overall_redundancy[0])
        #print(count)
    if count > 1:
        return count
    else:
        return 0
   


def path_score(path, red):
    """ returns the score of a path based on its redundancy
        which is computed by the above function.
    """
    sub_path = [path[0]]
    #print(sub_path)
    path.pop(0)
    r = 0
    for i in path:
        sub_path.append(i)
        r = r + (len(red) * len(sub_path))
        #print(r)
    score = float(r) / (len(path)+1)
    return score
'''

def is_collapsible(node):
    """ a node is collapsible if its POS is a verb due to the
        heavy useage of verbs in opinion texts and the ease
        with which the strucures can be combined to form a
        new sentence.
    """
    word_pos = node.split('/')
    if word_pos[1] in ['ADV', 'N']:
        if len(graph.item(node)) > 1:
            #for i in range(len(graph.item(node))):
                #if graph.item(node)[i].endswith('/JJ'):
            return True
    else:
        return False



def jaccard_similarity(x,y):
    """ by this similarity measure we can eliminate similar paths.
        this measure computes the similarity based on the interdection
        of 2 sets divided by union of them.
    """
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return 1-(intersection_cardinality/float(union_cardinality))
    
def my_similarity(x,y):
    """ will be used to eliminate paths that are similar with the start
        words and have extremely near scores.
    """
    flag = 0
    for i in range(2):
        if x[i] == y[i]:
            flag += 1
    if flag == 2:
        return False
    else:
        return True
'''

def stitch_and_score(path):
    """ finds a redundant path which could be an anchor, then finds
        its collapsed candidates and the score of final candidate.
    """
    for i in path:
        if is_collapsible(i):
            cuted = path.index(i)+1
            C = path[:cuted]
            mid = C[-1]
            candidate = path[:cuted]
            for_score_finall = []
            print('before collapse : ', C)
        else:
            return False
    if redundancy(C):
        for h in all_of_text_list:
            #print('sentense: ', h)
            #if list(set(h) & set(C)) == C:
            if find_matches(C,h) == [C]:
                start = h.index(mid)+1
                #print('start : ', start)
                flag = 1
                for n in h:
                    if flag == 1 and VEN(n):
                        end = h.index(n)
                        #print('end : ', end)
                        for_score = candidate[:cuted]
                        s = 0
                        for m in range(len(h[start:end])):
                            candidate.append(h[start+m])
                            s += 1
                            for_score.append(h[start+m])
                            #print('new candidate: ', candidate)
                        flag = 0
                if for_score not in for_score_finall:
                    for_score_finall.append(for_score)
                else:
                    for ss in range(s):
                        candidate.pop(-1)
                candidate.append('and/CC')    
    candidate.pop(-1)
    #print("fore_score_final: ", for_score_finall)
    score = 0
    for candid in for_score_finall:
        score = score + path_score(candid)
        #print(score)
    score_collapsible = score / len(for_score_finall)
    return candidate, score_collapsible



def stiched(tmp, j, new_redundancy, List):
    #print(j, ' is connected to ', len(graph.item(j)))
    for v_x in graph.item(j):
        valid = 0
        for k in PRI[j]:
            (SID,PID) = k
            if SID in new_redundancy and (SID, PID+1) in PRI[v_x]:
                valid += 1
        if valid > 0:
            List.append(v_x)
            if VEN(v_x):
                tmp.append(List)
                List = []
                break
            else:
                i = v_x
                stiched(tmp, i, new_redundancy, List)
    #return tmp

'''


def stiched(C, tmp, candidate, redundancy, PRI, all_of_text_list):
    """ finds the collapsed candidates and returns a "tmp" as a list
        contains the candidates which would be combined with "C" as
        an anchor. we use redundancy to garanty that the upcomming
        words belong to the correct sentences. 
    """
    mid = C[-1]
    for h in all_of_text_list:
            """ here we find the sentenses which contains "C" as an anchor. """
            if find_matches(C,h) == [C]:
                start = h.index(mid)+1
                #print('start : ', start)
                flag = 1
                for n in h:
                    if flag == 1 and VEN(n):
                        end = h.index(n)
                        #print('end : ', end)
                        #for_score = candidate[:cuted]
                        s = 0
                        n = 1
                        r = 0
                        """ we append words of a candidate sentence until we reach an end node
                            and r will contain the redundancy of collapsed candidate. """
                        for m in range(len(h[start:end])):
                            candidate.append(h[start+m])
                            s += 1
                            redundancy_num = 0
                            for k in redundancy:
                                (SID,PID) = k
                                """ these IFs will control the well-formedness of the sentence
                                    and we determined the gap threshold less than 2 (maximum
                                    allowed gaps in discovering redundances)."""
                                if (SID, PID+n) in PRI[h[start+m]]:
                                    redundancy_num += 1
                                elif (SID, PID+n+1) in PRI[h[start+m]]:
                                    redundancy_num += 1
                            n += 1
                            r = r + len(candidate) * redundancy_num ###fekr mikonam in khat bayad birun az halgheye for (m) baashe###3
                            #for_score.append(h[start+m])
                            #print('new candidate: ', candidate)
                        flag = 0
                if candidate not in tmp and len(candidate) > 0:
                    """ by IF we eliminate the duplicates """
                    candidate.append(r)
                    tmp.append(candidate)
                    candidate = []        
    return tmp

def traverse(List, v_k, redundancy, red, sentence, PRI, n, r, all_of_text_list):
    """ this function constructs paths in the graph which are redundant and
        valid. also computes the score of each valid path. then append the
        valid path to the "List". if a node in a path could be collapsible, creates
        a new sentence based on the anchor and collapsed candidates and append
        to the "List". and finally returns the "List".
        """
    if len(redundancy) > 1:
        if VEN(v_k):
            #print('v_k: ', v_k)
            #print(sentence)
            if valid_path(sentence, PRI) and len(sentence) > 1:
                """ if neglects paths which contains only one word """
                score = float(r) / len(sentence) * 2
                sentence.append(score)
                #print('valid sentence: ', sentence)
                if len(List) == 0:
                    List.append(sentence)
                elif my_similarity(sentence, List[-1]):
                    List.append(sentence)
                    
        else:
            """ for a node if it's not a VEN, then we continue to create the path."""
            for j in graph.item(v_k):
                """ FOR each node that is connected to "v_k" we compute redundancy
                    and score.
                    """
                semi_sent = sentence[0:n]
                redundancy_j = []
                for_red_score = []
                for k in redundancy:
                    (SID,PID) = k
                    """ gap threshold = 2 """
                    if (SID, PID+n) in PRI[j]:
                        redundancy_j.append((SID, PID+n))
                        if SID not in for_red_score:
                            for_red_score.append(SID)
                    elif (SID, PID+n+1) in PRI[j]:
                        redundancy_j.append((SID, PID+n+1))
                        if SID not in for_red_score:
                            for_red_score.append(SID)
                    #elif (SID, PID+3) in PRI[j] and SID not in redundancy_j:
                        #redundancy_j.append(SID)
                if len(redundancy_j) > 0:
                    new_red = [val for val in for_red_score if val in red]
                    semi_sent.append(j)
                    r = r + len(semi_sent) * len(new_red)
                    #print('new_redundancy', new_redundancy)  
                    #print('sentence', sentence)
                    if is_collapsible(j):
                    #print("j: ", j)
                        anchor = semi_sent
                        #print('anchor', anchor)
                        L = []
                        """ L is a list to create each collaped candidate in it. "tmp" is a list
                            to put L's in it. """
                        tmp = []
                        """ for a collapsible node we call stiched to find collapsed candidates
                            and calculate their scores: """
                        stiched(anchor, tmp, L, redundancy_j, PRI, all_of_text_list)
                        #traverse(tmp, v_x, new_redundancy, L)
                        #print('L: ', L)
                        #print('tmp: ', tmp)
                        if len(tmp)> 0:
                            stiched_sent = anchor
                            avr_score = 0
                            for cc in tmp:
                                """ the score of a stiched sentence is the average of the individual
                                    sentences assuming that they are not collapsed."""
                                avr_score = avr_score + r + cc[-1]
                                cc.pop(-1)
                                stiched_sent = stiched_sent + cc + ['و/CONJ']
                            stiched_sent.pop(-1)
                            if len(tmp) > 1:
                                stiched_sent.append((avr_score / len(tmp)) ** 2)
                            #else:
                                #stiched_sent.append(avr_score / len(tmp))
                                #print('stiched_sent', stiched_sent)
                                List.append(stiched_sent)
                                #print('List: ', List)
                    else:
                        """ for each node if it's not collapsible, then we continue to create a path
                            by addind connected nodes. so we call "traverse" recursively."""
                        new_j = j
                        traverse(List, new_j, redundancy, new_red, semi_sent, PRI, n+1, r, all_of_text_list)
        



