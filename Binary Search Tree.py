class NodeJS:
  def __init__(self,data) :
    self.Left = None
    self.Right = None
    self.data = data
  def insert(self,data):       
    if self.data:
      if data < self.data:
        if self.Left is None:
          self.Left = NodeJS(data)
        else:
          self.Left.insert(data)
      else:
        if self.Right is None:
          self.Right = NodeJS(data)
        else:
          self.Right.insert(data)
    return self
  def PrintTree(self):
    if self.Left:
      self.Left.PrintTree()
      print(self.data),
    if self.Right:
      self.Right.PrintTree()
  def inorderTraversal(self, root):
    res = []
    if root:
      res = self.inorderTraversal(root.Left)
      res.append(root.data)
      res = res + self.inorderTraversal(root.Right)
    return res

root = NodeJS(2566).insert(2).insert(5).insert(6).insert(6).insert(25).insert(66).insert(20).insert(23).insert(2)
print(root.inorderTraversal(root))