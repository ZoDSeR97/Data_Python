# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list 
# if there is some node in the list 
# that can be reached again by continuously 
# following the next pointer.

# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
# Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, val):  # added this line, takes a value
        newNode = ListNode(val)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        return self
    
    def make_loop(self):
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = self.head

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.data, end="")
            runner = runner.next 	# set the runner to its neighbor
        print()
        return self  # once the loop is done, return self to allow for chaining
    
class Solution:
    def hasCycle(self, head) -> bool:
        # Floyd’s Cycle Finding Algorithm
        Tortoise = head
        Hare = head
        while Hare and Hare.next:
            Tortoise = Tortoise.next
            Hare = Hare.next.next
            if Tortoise == Hare:
                return True
        return False

if __name__ == '__main__':

    LL = SinglyLinkedList()

    LL.insert_node(-4).insert_node(0).insert_node(2).insert_node(3).make_loop()
    
    result = Solution().hasCycle(LL.head)
    
    print(result)