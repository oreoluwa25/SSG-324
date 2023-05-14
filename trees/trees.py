
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# binary search tree


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return self
        temp = self.root
        while True:
            if newNode.value == temp.value:
                return
            if newNode.value < temp.value:
                if temp.left is None:
                    temp.left = newNode
                    return self
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = newNode
                    return self
                temp = temp.right


    def printTree(self):
        leftValue = self.root.left
        rightValue = self.root.right
        lefts = 'left values: '
        rights = 'right values: '

        while leftValue:
            lefts += str(leftValue.value) + '->'
            leftValue = leftValue.left

        while rightValue:
            rights += str(rightValue.value) + '->'
            rightValue = rightValue.right
        print('root: ' + str(self.root.value) + ' ' + lefts + ' ' + rights)

    def contains(self, value):
        if self.root is None:
            return False

        temp = self.root
        while temp:
            if value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
            else:
                return True
        return False
    
    def minValueNode(self, currentNode):
        if self.root is None:
            return
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode
    
    
    def maxValueNode(self, currentNode):
        if self.root is None:
            return
        while currentNode.right:
            currentNode = currentNode.right
        return currentNode
    
    def traversePreOrder(self, currentNode):
        print(currentNode.value, end=' ')
        if currentNode.left:
            self.traversePreOrder(currentNode.left)
        if currentNode.right:
            self.traversePreOrder(currentNode.right)
    
    def traversePostOrder(self, currentNode):
        if currentNode.left:
            self.traversePostOrder(currentNode.left)
        if currentNode.right:
            self.traversePostOrder(currentNode.right)
        print(currentNode.value, end=' ')
        
        
    def traverseInOrder(self, currentNode):
        if currentNode.left:
            self.traverseInOrder(currentNode.left)
        print(currentNode.value, end=' ')
        if currentNode.right:
            self.traverseInOrder(currentNode.right)
            
            
    def traverseReverseOrder(self, currentNode):
        if currentNode.right:
            self.traverseReverseOrder(currentNode.right)
        print(currentNode.value, end=' ')
        if currentNode.left:
            self.traverseReverseOrder(currentNode.left)
        
        


tree = BST()
tree.insert(8)
tree.insert(18)
tree.insert(6)
tree.insert(60)
tree.insert(4)
tree.insert(7)
tree.insert(14)

tree.printTree()
tree.print()
print(tree.contains(8))
print(tree.minValueNode(tree.root).value)
print(tree.maxValueNode(tree.root).value)
tree.traversePreOrder(tree.root)
print('')
tree.traversePostOrder(tree.root)
print('')
tree.traverseInOrder(tree.root)
print('')
tree.traverseReverseOrder(tree.root)

