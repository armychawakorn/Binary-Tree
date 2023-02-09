class Node:
  def __init__(self,myData):
    self.Left = None
    self.Right = None
    self.Data = myData
    
root = Node("P")

root.Left = Node("Q")
root.Left.Left = Node("L")
root.Left.Right = Node("Y")
root.Left.Left.Left = Node("N")
root.Left.Left.Right = Node("T")
root.Left.Right.Left = Node("S")
root.Left.Right.Right = Node("A")

root.Right = Node("L")
root.Right.Left = Node("W")
root.Right.Right = Node("A")
root.Right.Left.Left = Node("C")
root.Right.Left.Right = Node("R")
root.Right.Right.Left = Node("A")
root.Right.Right.Right = Node("C")