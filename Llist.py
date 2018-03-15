#单链表的相关操作
class LNode:
    def __init(self, elem, next=None):
        self.elem = elem
        self.next = next
        
#基本操作
class LList:
    def __init__(self):
        self._head = None
    def is_empty(self):
        return self._head is None
    def prepend(self, elem):
        self._head = LNode(elem, self._head)
    def pop(self):
        if self._head is None:
            raise Error
        e = self._head.elem
        self._head = self._head.next
        return e
        
    #后端操作
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return 
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        if self._head is None:
            raise Error
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e
        
    #查找
    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next
    
    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next




    
