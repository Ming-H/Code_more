"""单链表的反转可以使用循环，也可以使用递归的方式

#1.循环反转单链表
#循环的方法中，使用pre指向前一个结点，cur指向当前结点，每次把cur->next指向pre即可。

class ListNode:  
    def __init__(self,x):  
        self.val=x;  
        self.next=None;  
  
def nonrecurse(head):              #循环的方法反转链表  
    if head is None or head.next is None:  
        return head;  
    pre=None;  
    cur=head;  
    h=head;  
    while cur:  
        h=cur;  
        tmp=cur.next;  
        cur.next=pre;  
        pre=cur;  
        cur=tmp;  
    return h;  
      
head=ListNode(1);    #测试代码  
p1=ListNode(2);      #建立链表1->2->3->4->None;  
p2=ListNode(3);  
p3=ListNode(4);  
head.next=p1;  
p1.next=p2;  
p2.next=p3;  
p=nonrecurse(head);   #输出链表 4->3->2->1->None  
while p:  
    print p.val;  
    p=p.next;  
  
#2.递归实现单链表反转

class ListNode:  
    def __init__(self,x):  
        self.val=x;  
        self.next=None;  
  
      
def recurse(head,newhead):    #递归，head为原链表的头结点，newhead为反转后链表的头结点  
    if head is None:  
        return ;  
    if head.next is None:  
        newhead=head;  
    else :  
        newhead=recurse(head.next,newhead);  
        head.next.next=head;  
        head.next=None;  
    return newhead;  
      
head=ListNode(1);               #测试代码  
p1=ListNode(2);                 # 建立链表1->2->3->4->None  
p2=ListNode(3);  
p3=ListNode(4);  
head.next=p1;  
p1.next=p2;  
p2.next=p3;  
newhead=None;  
p=recurse(head,newhead);           #输出链表4->3->2->1->None  
while p:  
    print p.val;  
    p=p.next;  

参考文献：http://blog.csdn.net/u011608357/article/details/36933337
