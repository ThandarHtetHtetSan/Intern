class Node:
    def __init__(self,data):
        self.data= data
        self.sec_data=[]
        self.left: Node = None
        self.right: Node = None

main_tree_data = []
for i in range(1, 26):
    main_tree_data.append(i)

def insertion(alpha, root_tree :Node):
    if root_tree is None:
        return Node(alpha)
    if alpha<root_tree.data:
        root_tree.left = insertion(alpha , root_tree.left)
    else:
        root_tree.right = insertion(alpha,root_tree.right)

    return root_tree

def printing(node):

    if node is not None:
        printing(node.left)
        print(node.data)
        printing(node.right)

length = len(main_tree_data)
mid = int(length/2)
tree = Node(13)

first_part = main_tree_data[0:mid]
sec_part = main_tree_data[mid+1:length]

first_part.reverse()
for i in range(len(first_part)):
    tree = insertion(first_part[i],tree)


for i in range(len(sec_part)):

    tree = insertion(sec_part[i],tree)

#printing(tree)
#
# sec_data=['j','k','c','b']
# c=0
# def change_chr(sec_data, c=None):
#     for i in range(len(sec_data)):
#         for j in sec_data[i]:
#             c += ord('j')
#
# def sort_name(sec_data):
#     for i in range(len(sec_data)):
#         if change_chr(sec_data[i])<= change_chr(sec_data[i+1]):
#
#
#
# def mergesort(sec_data):
#     if len(sec_data)>1:
#         mid= len(sec_data)//2
#         L=sec_data[:mid]
#         R=sec_data[mid:]
#         mergesort(L)
#         mergesort(R)
#         i=j=k=0
#         while i < len(L) and j < len(R):
#             if L[i] <= R[j]:
#                 sec_data[k] = L[i]
#                 i += 1
#             else:
#                 sec_data[k] = R[j]
#                 j += 1
#             k += 1
#
# def get_tree():
#     return tree
#test=[]
#printing(tree)
#for i in range(1,26):
 #   if i==len(name):
 #       test.append(name)





