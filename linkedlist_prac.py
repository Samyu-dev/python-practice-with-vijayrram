class LinkedList:
    class Node:
        def __init__(self, data) -> None:
            self.data = data
            self.next = None

        def __str__(self) -> str:
            if self.next:
                return f'({self.data})->{self.next}'
            else:
                return f'({self.data})->X'

    def __init__(self) -> None:
        self.head = None

    def append(self, data): # Total space comlexity O(1)
        new_node = self.Node(data)  # O(1)
        if self.head == None:
            self.head = new_node # O(0)
        else:
            curr = self.head  # O(1)
            while curr.next is not None:
                curr = curr.next # O(0)
            curr.next = new_node # O(0)
             
    def __str__(self) -> str:
        return f'{self.head}'


if __name__ == '__main__':
    ll = LinkedList()
    
    for x in range(1, 6):
        ll.append(x)
        print(ll)
   