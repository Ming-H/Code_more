1、二分查找
def func(L, item):
    i = 0
    j = len(L)-1
    while i<=j:
        mid = int((i+j)/2)
        guess = L[mid]
        if guess>item:
            j = mid - 1
        elif guess < item:
            i = mid + 1
        else:
            return mid
    return False


2、快速排序
def func(L):
    if len(L)<2:
        return L
    else:
        pivot = L[-1]
        less = [item for item in L[:-1] if item <= pivot]
        bigger = [item for item in L[:-1] if item > pivot]
        final = func(less) + [pivot] + func(bigger)
        return final
   
   
3、层序遍历
def lookup(root):
    stack = [root]
    while stack:
        current = stack.pop(0)
        print(current.data)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
            
            
4、深度遍历
def deep(root):
    if not root:
        return
    print(root.data)
    deep(root.left)
    deep(root.right)
    
    
5、前中后序遍历
class Node(object):
    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right

#中序遍历:遍历左子树,访问当前节点,遍历右子树
def mid_travelsal(root):
    if root.left is not None:
        mid_travelsal(root.left)
    #访问当前节点
    print(root.value)
    if root.right is not None:
        mid_travelsal(root.right)

#前序遍历:访问当前节点,遍历左子树,遍历右子树
def pre_travelsal(root):
    print(root.value)
    if root.left is not None:
        pre_travelsal(root.left)
    if root.right is not None:
        pre_travelsal(root.right)

#后续遍历:遍历左子树,遍历右子树,访问当前节点
def post_trvelsal(root):
    if root.left is not None:
        post_trvelsal(root.left)
    if root.right is not None:
        post_trvelsal(root.right)
    print(root.value)


6、求树的最大深度
def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) +1


7、判断两棵树是否相同
def isSameTree(p, q):
    if p == None and q == None:
        return True
    elif p and q :
        return p.val == q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    else :
        return False
    
8、根据前、中序求后序
def rebuild(pre, center):
    if not pre:
        return
    cur = Node(pre[0])
    index = center.index(pre[0])
    cur.left = rebuild(pre[1:index + 1], center[:index])
    cur.right = rebuild(pre[index + 1:], center[index + 1:])
    return cur

def deep(root):
    if not root:
        return
    deep(root.left)
    deep(root.right)
    print(root.data)
    

9、单链表反转
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
	return h

def recurse(head,newhead):    #递归，head为原链表的头结点，newhead为反转后链表的头结点
	if head is None:
		return ;
	if head.next is None:
		newhead=head;
	else :
		newhead=recurse(head.next,newhead);
		head.next.next=head;
		head.next=None;
	return newhead


 
参考文献：
https://github.com/taizilongxu/interview_python#29-super-init
http://www.cnblogs.com/ChenxofHit/archive/2011/03/18/1988431.html
