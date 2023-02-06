def isValid(s):
        stack = Stack()
        brackets = {"]": "[", "}": "{", ")": "("}

        for l in s:
            if l in brackets.values():
                stack.push(l)

            elif l in brackets.keys() and stack.length > 0:
                found = stack.pop(brackets[l])
                if found:
                    continue
                else:
                    return False

            elif l in brackets.keys() and stack.length <= 0:
                return False
                
        stack.print()
        return stack.length == 0



class Stack ():
    def __init__(self):
        self.length = 0
        self.head = None

    def print(self):
        if not self.head:
            return

        list = []
        current = self.head

        while current:
            list.append(current.value)
            current = current.prev

        stdout = " -> ".join(list)
        print(stdout)


    def push (self, value):
        current = Node(value, None)
        self.length += 1
        if not self.head:
            self.head = current
        else: 
            current.prev = self.head
            self.head = current

    def pop (self, value):
        if self.length > 0:
            current = self.head
            if current.value == value:
                self.head = self.head.prev
                current.prev = None
                self.length -= 1
                return current.value

        return False


    def peek(self):
        if not self.head:
            return False

        return self.head.value





class Node ():
    def __init__(self, value, prev):
        self.value = value
        self.prev = prev
        

    
def main():
    s = "[)]"
    print(isValid(s))

if __name__ == "__main__":
    main()