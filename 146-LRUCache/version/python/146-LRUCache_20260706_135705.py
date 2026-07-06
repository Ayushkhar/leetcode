# Last updated: 7/6/2026, 1:57:05 PM
1class Node:
2    def __init__(self, key, value):
3        self.key = key 
4        self.value = value
5        self.prev = None
6        self.next = None 
7
8class LRUCache:
9    def __init__(self, capacity: int):
10        self.capacity = capacity 
11        self.cache = {}
12
13        self.left = Node(0,0)
14        self .right = Node(0,0)
15
16        self.left.next = self.right
17        self.right.prev = self.left 
18    
19    def insert(self, node):
20        prev = self.right.prev 
21        self.right.prev = node
22        node.next = self.right 
23        node.prev = prev 
24        prev.next = node
25
26    def remove(self, node):
27        nxt = node.next 
28        prev = node.prev 
29        prev.next = nxt 
30        nxt.prev = prev 
31
32
33    def get(self, key: int) -> int:
34        if key in self.cache:
35            node = self.cache[key]
36            self.remove(node)
37            self.insert(node)
38            return node.value
39        return -1
40         
41    def put(self, key: int, value: int) -> None:
42        if key in self.cache:
43            self.remove(self.cache[key])
44            del self.cache[key]
45            
46        node = Node(key,value)
47        self.cache[key]= node
48        self.insert(node)
49        if(len(self.cache) > self.capacity):
50            lru = self.left.next
51            self.remove(lru)
52            del self.cache[lru.key]
53
54
55        
56
57
58
59            
60
61        
62
63
64# Your LRUCache object will be instantiated and called as such:
65# obj = LRUCache(capacity)
66# param_1 = obj.get(key)
67# obj.put(key,value)