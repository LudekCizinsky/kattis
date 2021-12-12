
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:

    def __init__(self):
        self.first = None
        self.N = 0

    def isEmpty(self):
        return self.first is None

    def size(self):
        return self.N

    def push(self, item):

        if self.isEmpty():
            self.first = Node(item)
            self.N += 1
            return

        oldfirst = self.first
        self.first = Node(item)
        self.first.next = oldfirst
        self.N += 1

    def pop(self):
        if self.isEmpty():
            return None

        item = self.first.item
        self.first = self.first.next
        self.N -= 1
        return item


def main():

    # Read the input
    w = input()

    # Initiliaze stack
    stack = Stack()

    # Iterate over the items in input and decide whether w is balanced or not
    for item in w:

        if item == '(' or item == '[':
            stack.push(item)
        elif item == ')':
            corresponding_item = stack.pop()
            if corresponding_item != '(':
                return 0
        elif item == ']':
            corresponding_item = stack.pop()
            if corresponding_item != '[':
                return 0

    if stack.isEmpty():
        return 1
    else:
        return 0


if __name__ == "__main__":
    print(main())
