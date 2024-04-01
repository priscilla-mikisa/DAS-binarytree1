
 #first, we create our tree by creating a node class and assign a root value but with the left child and right child nodes having no values.
class Node:
   def __init__(self, tree):
      self.left = None
      self.right = None
      self.tree = tree  

#Then we insert the new nodes by comparing the new value with the parent node.
   def insert(self, tree):
      if self.tree:
         if tree < self.tree:
            if self.left is None:
               self.left = Node(tree)
            else:
               self.left.insert(tree)
         elif tree > self.tree:
               if self.right is None:
                  self.right = Node(tree)
               else:
                  self.right.insert(tree)
      else:
         self.data = tree(end=",")

# After that, we print the tree from the root node to the inserted nodes.
#If we want to access certain values using the DFS specifically, the in-order algorithm, the steps below are taken.
#1. Using the "def" key word, we define our function "PrintTree".
#2. Then we go to the left child and print it.
#3. Then the node value and lastly, the right node value. 

   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.tree),
      if self.right:
         self.right.PrintTree()

# By the help of the inbuilt function insert, we can now add values.
root = Node(90)
root.insert(45)
root.insert(14)
root.insert(55)
root.insert(67)
#Then print out the tree
"""The tree is organised in a way that all the less numbers to the root node
will be on the left and greater numbers on its right. Hence explainig the definition of
 the term binary tree as a hierachy in slide 1"""

root.PrintTree()
# The result will look more like this.[3,6,12,14].
# The two left values first,3 and 6, then the root node 12 and lastly the right value 14.