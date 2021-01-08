class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None

    def Insert(self, value):
        self.root = self.__Insert(self.root, value)

    def __Insert(self, root, value):
        if root is None:
            root = Node(value)
        elif value > root.value:
            root.right = self.__Insert(root.right, value)
        else:
            root.left = self.__Insert(root.left, value)
        return root

    def InOrder(self):
        return self.__InOrder(self.root)

    def __InOrder(self, root):
        if root:
            self.__InOrder(root.left)
            print(root.value)
            self.__InOrder(root.right)
        return ''

    def PreOrder(self):
        return self.__PreOrder(self.root)

    def __PreOrder(self, root):
        if root:
            print(root.value)
            self.__PreOrder(root.left)
            self.__PreOrder(root.right)
            return ''

    def PostOrder(self):
        return self.__PostOrder(self.root)

    def __PostOrder(self, root):
        if root:
            self.__PostOrder(root.left)
            self.__PostOrder(root.right)
            print(root.value)

    def Height(self):
        return self.__Height(self.root)

    def __Height(self, root):
        # x = root
        # y = root
        if root is None:
            return 0
        else:
          
          return max(self.__Height(root.left), self.__Height(root.right)) + 1
            
    def FindMin(self):
        return self.__FindMin(self.root)

    def __FindMin(self, root):
        if root is None:
            return 0
        elif root.left is None:
            return root.value
        else:
            return self.__FindMin(root.left)

    def FindMax(self):
        return self.__FindMax(self.root)

    def __FindMax(self, root):
        if root is None:
            return 0
        elif root.right is None:
            return root.value
        else:
            return self.__FindMax(root.right)

    def Successor(self):
        return self.__Successor(self.root)

    def __Successor(self, root):
        if root.right is not None:
            return self.__FindMin(root.right)

    def Predeccessor(self):
        return self.__Predeccessor(self.root)

    def __Predeccessor(self, root):
        if root.left is not None:
            return self.__FindMax(root.left)

    def Delete(self,value):
      return self.__Delete(self.root,value)

    def __Delete(self,root,value):
        if root is None:
            return root

        if value < root.value:
            root.left = self.__Delete(root.left,value)

        elif value > root.value:
            root.right = self.__Delete(root.right,value)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.__FindMin(root.right)
            root.value = temp.value
            root.right = self.__Delete(root.right,temp.value)
        return root

ob = BST()
ob.Insert(5)
ob.Insert(50)
ob.Insert(40)
ob.Insert(70)
ob.Insert(100)
ob.Insert(110)
print("---------Inorder-----------")
ob.InOrder()
print("---------Preorder-----------")
ob.PreOrder()
print("---------Postorder-----------")
ob.PostOrder()
print("---------Height-----------")
print(ob.Height())
print("---------Minimum-----------")
ob.FindMin()
print("---------Maximum-----------")
ob.FindMax()
print("---------Successor-----------")
print(ob.Successor())
print("---------Predeccessor-----------")
#print(ob.Predeccessor())
ob.Delete(40)
ob.Delete(100)
print("---------Inorder-----------")
ob.InOrder()
