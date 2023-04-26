import own_db_tree
import sec_tree
class Node:
    def __init__(self):
        # self.data= data
        self.store=[]
        self.sort=None
        self.left: Node = None
        self.right: Node = None

node=Node()

first_tree = own_db_tree.tree
sec__tree = sec_tree.tree


def printing(node):

    if node is not None:
        printing(node.left)
        if node.sec_data!=None:
            print(node.sec_data)
        printing(node.right)


def connection_test(ftree,name):

    if ftree is not None:
        connection_test(ftree.left, name)
        if ftree.data ==name[0]:
            sec_tree_con_test(sec__tree,len(name),name)

            return


        connection_test(ftree.right,name)

def sec_tree_con_test(sec__tree , length , name ):

    if sec__tree is not None:
        sec_tree_con_test(sec__tree.left,length,name)
        if sec__tree.data == length:
            #sec__tre.sec_data = name
            sec__tree.sec_data.append(name)
            print("We found for third tree")
            print(sec__tree.sec_data)
            res=binary_search(sec__tree.sec_data,)


            return

        sec_tree_con_test(sec__tree.right,length,name)

def ascii_code(node,alph):
    c=0
    for i in alph:
        c+=ord(i)
    node.store.append(c)
    print(node.store)


def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def mergesort(list):
    if len(list) < 2:
        return list

    middle = len(list) //2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left, right)


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1







def printList(test):
    for i in range(len(test)):
        print(test[i], end=" ")
        print()
# def store(first_tree,sec__tree,name):
#     if first_tree != None and sec__tree != None:
#         if first_tree.data==name[0] and  sec__tree==len(name) :
#             Node.store.append(name)
#         print(Node.store)
#def sec_tree_con_test(sec_tree,length,sch):



        



# def change_chr(data):
#
#     c=0
#     for j in name:
#         c += ord('j')
#
#     print(c)
test = []
if __name__ == '__main__':
    while True:
        name = input("Enter name")
        connection_test(first_tree,name)
        ascii_code(node,name)
        print('sorted list', mergesort(node.store))
        sch=input('Enter your name')
        sec_tree_con_test(sec__tree,len(sch),sch)

        print("We found this at ", binary_search(node.store,305))
        # for i in range(6):
        #
        #     change_chr(name)
        #
        # connection_test(first_tree,name)
        #
        # for i in range(1, 26):
        #     if i == len(name):
        #         test.append(name)

        # printing(sec__tree)



