def preOrder(root): # 전위순회
    if root == ".":
        return

    left, right = mydict[root]

    print(root, end = "")
    preOrder(left)
    preOrder(right)

def inOrder(root): # 중위순회
    if root == ".":
        return

    left, right = mydict[root]

    inOrder(left)
    print(root, end = "")
    inOrder(right)

def postOrder(root): # 후위순회
    if root == ".":
        return

    left, right = mydict[root]

    postOrder(left)
    postOrder(right)
    print(root, end = "")

N = int(input())

mydict = {} # 딕셔너리에 저장
for i in range(N):
    root, left, right = input().split() # 루트, 왼쪽자식, 오른쪽자식
    mydict[root] = left, right

preOrder("A")
print()
inOrder("A")
print()
postOrder("A")