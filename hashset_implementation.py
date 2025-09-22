class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for _ in range(10 ** 4)]

    def hashfunc(self, key: int) -> int:
        return key % len(self.set)
    
    def add(self, key: int) -> None:
        hash_node = self.set[self.hashfunc(key)] #at dummy node
        
        while hash_node.next:
            if hash_node.next.val == key: #no duplicates in hashset
                return
            hash_node = hash_node.next
        
        hash_node.next = ListNode(key)

    def remove(self, key: int) -> None:
        hash_node = self.set[self.hashfunc(key)]
        while hash_node.next:
            if hash_node.next.val == key:
                hash_node.next = hash_node.next.next
                return
            hash_node = hash_node.next

    def contains(self, key: int) -> bool:
        hash_node = self.set[self.hashfunc(key)]
        while hash_node.next:
            if hash_node.next.val == key:
                return True
            hash_node = hash_node.next
        return False
    


#obj = MyHashSet()
#obj.add(key)
#obj.remove(key)
#param_3 = obj.contains(key)