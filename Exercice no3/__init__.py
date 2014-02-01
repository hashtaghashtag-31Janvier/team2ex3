import collections
import time

#Fonctionne avec tous les jeux d'essais, il faut maintenant essayer de dessiner le truc
#Bonne chance Gab

#dictionary?
relations = {}

N = int(input('Entree\n'))
for i in range(N):
    inputString = input()
    X,Y = inputString.split(" ")
    X = int(X)
    Y = int(Y)

    if X in relations:
        relations[X].append(Y)
    else:
        relations[X] = [Y]

max_length = {}

def findMaxLength(i):
    if i in max_length: return max_length[i]
    maximum = 0
    if i in relations:
        for voisin in relations[i]:
            maximum = max(maximum, findMaxLength(voisin))
    max_length[i] = maximum + 1
    return max_length[i]

current_max = 0
current_index = -1

for i in relations.keys():
    if current_max < findMaxLength(i):
        current_max = max_length[i]
        current_index = i
    
print(current_max, current_index)

######CODE DE DESSIN ICI
#exemple pour relation: {2:[3,4]} Cela veut dire qu'il y a un arc de 2 vers 3
#                                   et de 2 vers 4
#max_length contient la longueur maximale d'un chemin qui commence a ce noeurds la
#ex: {2:2,3:1,4:1} le noeud 2 est le commencement d'un chemin de longeur 2


#je vais essayer d'imprimer en console la chaine la plus longue au moins

print("relations: " + str(relations))
print("Max_length: " + str(max_length))
printstr = str(current_index)

for n in range(current_max-1):
    print(current_max, current_index)
    maxv = 0
    maxi = relations[current_index][0]
    for i in relations[current_index][1:]:
        if current_max < findMaxLength(i):
           current_max = max_length[i]
           current_index = i
    current_max = maxv
    current_index = maxi
    printstr += " -> " + str(current_index)

print(printstr)





                      
#exemple linked chain---------
"""
# very lost. such python. so dont know what im doing. wow.
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, self.value)


class LinkedList(collections.MutableSequence):
    def __init__(self, iterable=None):
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.__len = 0
        if iterable is not None:
            self += iterable        

    def get_node(self, index):
        node = sentinel = self.sentinel
        i = 0
        while i <= index:
            node = node.next
            if node == sentinel:
                break
            i += 1
        if node == sentinel:
            node = None
        return node

    def __getitem__(self, index):
        node = self.__get_node(index)
        return node.value
    
    def __len__(self):
        return self.__len

    def __setitem__(self, index, value):
        node = self.get_node(index)
        node.value = value
        
    def __delitem__(self, index):
        node = self.get_node(index)
        if node:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev     
            node.prev = None
            node.next = None
            node.value = None
            self.__len -= 1
                
    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        list_ = [self.__get_node(i).value for i in range(len(self))]
        return '%s(%r)' % (self.__class__.__name__, list_)
    
    def append(self, value):
        sentinel = self.sentinel
        node = Node(value)
        self.insert_between(node, sentinel.prev, sentinel)

    def insert(self, index, value):
        sentinel = self.sentinel
        new_node = Node(value)
        len_ = len(self)
        if len_ == 0:
            self.insert_between(new_node, sentinel, sentinel)
        elif index >= 0 and index < len_:
            node = self.get_node(index)   
            self.insert_between(new_node, node.prev, node)
        elif index == len_:
            self.insert_between(new_node, sentinel.prev, sentinel)
        else:
            raise IndexError
        self.__len += 1
                
    def insert_between(self, node, left_node, right_node):
        if node and left_node and right_node:
            node.prev = left_node
            node.next = right_node
            left_node.next = node
            right_node.prev = node
        else:
            raise IndexError
        
    
class Stopwatch(object):
    def __init__(self):
        self.__start = 0.0
        self.__stop = 0.0
        self.__duration = 0.0
    
    def start(self):
        self.__start = time.time()
        return self
    
    def stop(self):
        self.__stop = time.time()
        self.__duration = self.__stop - self.__start
        return self.__duration
    
    def duration(self):
        return self.__duration   

class Profiler(object):
    def __init__(self, size):
        self.size = size
        self.list = None
        self.linked_list = None
        self.sw_create_list = Stopwatch()
        self.sw_create_linked_list = Stopwatch()
        self.sw_pop_list = Stopwatch()
        self.sw_pop_linked_list = Stopwatch()
        
    def create_list(self):
        self.sw_create_list.start()
        self.list = [i for i in range(self.size)]
        self.sw_create_list.stop()
    
    def create_linked_list(self):
        self.sw_create_linked_list.start()
        self.linked_list = LinkedList()
        for value in self.list:
            self.linked_list.append(value)
        self.sw_create_linked_list.stop()
    
    def pop_list(self):
        self.sw_pop_list.start()
        for i in range(self.size):
            del self.list[0]
        self.sw_pop_list.stop()
    
    def pop_linked_list(self):
        self.sw_pop_linked_list.start()
        for i in range(self.size):
            del self.linked_list[0]
        self.sw_pop_linked_list.stop()
        
    def report(self):
        print("%6s %10d" % ("Size", self.size))
        print("%6s %10s %10s %10s" % ("Type", "Create", "Pop", "Total")) 
        print("%6s %10.2f %10.2f %10.2f" % ("List", self.sw_create_list.duration(), \
                self.sw_pop_list.duration(), self.sw_create_list.duration() + self.sw_pop_list.duration()))
        print("%6s %10.2f %10.2f %10.2f" % ("Linked", self.sw_create_linked_list.duration(), \
                self.sw_pop_linked_list.duration(), self.sw_create_linked_list.duration() + \
                self.sw_pop_linked_list.duration()))
        print
        
    def run(self):
        self.create_list()
        self.pop_list()
        self.create_linked_list()
        self.pop_linked_list()
        self.report()
   
if __name__ == '__main__':
    Profiler(1000).run()
    Profiler(2000).run()
    Profiler(5000).run()
    Profiler(10000).run()
    Profiler(20000).run()
    Profiler(50000).run()
    Profiler(100000).run()
    print "Complete."    
    """
