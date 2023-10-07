# Given a singly-linked list
# Each node contain either 0 or 1
# Calculate decimal value 
# represent the binary

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

# Constraints:
# 1 <= n <=64

class SinglyLinkedListNode:
    def __init__(self, val):
        self.data = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, val):  # added this line, takes a value
        newNode = SinglyLinkedListNode(val)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        return self

    def print_values(self):
        runner = self.head
        print("The Binary is", end=" ")
        while (runner != None):
            print(runner.data, end="")
            runner = runner.next 	# set the runner to its neighbor
        print()
        return self  # once the loop is done, return self to allow for chaining

# Implement this getNumber(binary)
def getNumber(binary):
    # Write your code here
    Bin = []
    ans = 0
    # We have to this since we do not have
    # Concrete information what exactly is the length of binary
    while binary:
        Bin.append(binary.data)
        binary = binary.next
    for i in range(len(Bin)-1, -1,-1):
        ans+=Bin[i]*2**(len(Bin)-i-1)
    return ans
        
if __name__ == '__main__':

    binary_count = int(input().strip())

    binary = SinglyLinkedList()

    for _ in range(binary_count):
        binary_item = int(input().strip())
        binary.insert_node(binary_item)
    binary.print_values()
    
    result = getNumber(binary.head)
    
    print("The Decimal is", result)