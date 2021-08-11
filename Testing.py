# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 02:30:09 2016

@author: Team No.6
"""



import heap
myHeap = heap.heap(100)


class PQueue:
    def __init__(self,element):
        self.element = element
        self.next =0
        self.size=0
    
  

def EmptyQueue():
    address = myHeap.malloc()
    if address != -1:
        myHeap.set_cell(address,PQueue(0))
        return address
    return False    

def dummylist(h):
    l=[]
    for i in range(1,size(h)+1):
        t = myHeap.get_cell(i)
        f=t.element
        l.append(f)     
    return l
            
    
def SwapUp(i):
    while i // 2 > 0:
        t = myHeap.get_cell(i)
        k = myHeap.get_cell(i//2)
        if t.element < k.element :
            k.element,t.element=t.element,k.element 
        i=i//2
        SwapUp(i)
    return True
    
def LastIndex(h):
    m = myHeap.get_cell(h)
    if m.next == 0:
        return h
    return LastIndex(m.next)
    
def insert(k,h):
    current_add = LastIndex(h)
    current_cell = myHeap.get_cell(current_add)
    new_add = myHeap.malloc()
    if new_add != -1:
        myHeap.set_cell(new_add,PQueue(k))
        current_cell.next = new_add
        myHeap.set_cell(current_add,current_cell)
        j=LastIndex(h)
        SwapUp(j)
        return True
    return False   

def size(h):
    count=0
    while h!= 0:
        node = myHeap.get_cell(h)
        if node.element != None:
            count+=1
        h=node.next
    return count
    
def minChild(i,h):
    n=myHeap.get_cell(2*i)
    m=myHeap.get_cell(2*i+1)
    if 2*i>size(h):
        print ("No child")
    else:
        if 2*i+1 > size(h) and 2*i ==size(h):
            return 2*i
        else:
            if n.element < m.element:
                return 2*i
            else:
                return 2*i+1

def swapdown(i,h):
    while  2*i <= size(h):        
        l=myHeap.get_cell(i)
        o=minChild(i,h)
        m=myHeap.get_cell(o)
        if m.element < l.element:
            l.element,m.element=m.element,l.element
        i=o
        swapdown(i,h)

#delete minimum function
def del_min(h):
    t = myHeap.get_cell(1)
    v=t.element
    print('removed element min =' ,v)
    y=size(h)
    k = myHeap.get_cell(y)
    t.element=k.element
    myHeap.set_cell(size(h),PQueue(None))
    swapdown(1,h)
    return v 
                                                    
def index(y,h):
    n = myHeap.get_cell(h)
    if n.element == y:
        return h
    else:
        h = n.next
        return index(y,h)
                    
def printQueue(h):
    while h!= 0:
        node = myHeap.get_cell(h)
        if node.element != None:
            print (node.element)
        h = node.next    
        
def number_sort():
    l = [int(i) for i in input().split()]
    j=EmptyQueue()
    for i in range (len(l)):
        insert(l[i],j)
    del_min(j)
    printQueue(j)
    l=dummylist(j)
    print (l)
    sl=[]
    for i in range(len(l)):
        sl.append(del_min(j))
    print ('The sorted list of l is:',sl)

l=[1,3,5,7,94,8,62,52,44]
number_sort()



    




            
