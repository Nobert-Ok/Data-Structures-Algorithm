class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def appendnode(self,data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        lastnode = self.head
        while lastnode.next is not None:
            lastnode = lastnode.next
        lastnode.next = newnode

    def printll(self):
        currentnode = self.head
        while currentnode is not None:
            print(currentnode.data,end=" => ")
            currentnode = currentnode.next

    def prepend(self,data):
        newnode = Node(data)

        newnode.next = self.head
        self.head = newnode

    def insertnode(self,prevnode,data):
        newnode = Node(data)
        if prevnode is None:
            print("Node inexistence")
            return
        newnode.next = prevnode.next
        prevnode.next = newnode
  
    def deletenode(self,key):
        currentnode = self.head
        if currentnode is not None and currentnode.data == key:
            self.head = currentnode.next
            currentnode = None
            return

        prevnode = None
        while currentnode is not None and currentnode.data != key:
            prevnode = currentnode
            currentnode = currentnode.next
        if prevnode is None:
            print("Node inexitence")
            return
        prevnode.next = currentnode.next
        currentnode = None


    def len_ll(self):
        currentnode = self.head
        count = 0
        while currentnode is not None:
            count += 1
            currentnode = currentnode.next
        return count
        


    def swapnode(self, key1,key2):
        prev1 = None
        cur1 = self.head
        while cur1 is not None and cur1.data != key1:
            prev1 = cur1
            cur1 = cur1.next

        prev2 = None
        cur2 = self.head
        while cur2 is not None and cur2.data != key2:
            prev2 = cur2
            cur2 = cur2.next

        if cur1 is None and cur2 is None:
            return('Nodes inexistence')
        
        if prev1 is not None:
            prev1.next = cur2
        else:
            self.head = cur2

        if prev2 is not None:
            prev2.next = cur1
        else:
            self.head = cur1

        cur1.next,cur2.next = cur2.next,cur1.next
        

    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def merge_sorted(self,llist):
        p = self.head
        q = llist.head
        s = None

        if p is None:
           return q
        if q is None:
            return p

        if p is not None and q is not None:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p is not None and q is not None:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        
        if p is None:
            s.next = q
        if q is None:
            s.next = p
        
        return new_head

    def remove_duplicate(self):
        prev = None
        cur = self.head

        dup_values = {}
        while cur is not None:
            if cur.data in dup_values:
                prev.next = cur.next
                cur = None
            else:
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next 
            


        
    
    def nth_to_last_node(self, n):
        cur = self.head
        # count = 0
        # while cur is not None:
        #     count += 1
        #     cur = cur.next
        total = self.len_ll()
        while cur is not None:
            if total == n:
                print(cur.data)
            total -= 1
            cur = cur.next
        if cur is None:
            return

        

ll = Linkedlist()
ll.appendnode("a")
ll.appendnode("b")
ll.appendnode("c")
ll.appendnode("d")
ll.nth_to_last_node(2)
# ll_1.remove_duplicate()

# ll_2 = Linkedlist()
# ll_1.appendnode(1)
# ll_1.appendnode(5)
# ll_1.appendnode(7)
# ll_1.appendnode(9)
# ll_1.appendnode(10)

# ll_2.appendnode(2)
# ll_2.appendnode(3)
# ll_2.appendnode(4)
# ll_2.appendnode(6)
# ll_2.appendnode(8)
# ll_1.merge_sorted(ll_2)






# ll.appendnode("a")
# ll.appendnode("b")
# ll.appendnode("c")
# ll.appendnode("d")
# ll.insertnode(ll.head,"Abdi") 
# ll.prepend("Okoye")
# ll.deletenode("Okoye")
# ll.deletenode("c")
# ll.len()
# ll.swapnode("a","d")
# ll.reverse()
# ll.printll()