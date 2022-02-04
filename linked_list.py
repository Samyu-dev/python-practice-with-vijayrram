'''docstring'''

# Require `__future__.annotations` to refer to `LinkedList.Node` before fully defining it.
from __future__ import annotations

import typing


class LinkedList:
    '''docstring'''

    class Node:
        '''docstring'''

        def __init__(self, data: typing.Any) -> None:
            self.data = data
            self.next: typing.Optional[LinkedList.Node] = None

        def __str__(self) -> str:
            if self.next:
                return f'({self.data})->{self.next}'

            return f'({self.data})->X'


    def __init__(self) -> None:
        self.head: typing.Optional[LinkedList.Node] = None

    def append(self, data: typing.Any): # Total space comlexity O(1)
        '''docstring'''

        new_node = self.Node(data)  # O(1)
        if self.head is None:
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
