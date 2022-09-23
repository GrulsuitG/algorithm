import sys

sys.setrecursionlimit(10 ** 6)


class Tree:
    def __init__(self, node):
        self.x = node[0]
        self.idx = node[2]
        self.left = None
        self.right = None
        self.parent = None


def preorder(tree, l):
    if tree is None:
        return l
    l.append(tree.idx)
    preorder(tree.left, l)
    preorder(tree.right, l)


def postorder(tree, l):
    if tree is None:
        return l
    postorder(tree.left, l)
    postorder(tree.right, l)
    l.append(tree.idx)


def solution(nodeinfo):
    root = None
    for idx in range(len(nodeinfo)):
        nodeinfo[idx].append(idx + 1)

    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    for info in nodeinfo:
        node = Tree(info)
        if root == None:
            root = node
        else:
            curRoot = root
            while True:
                if curRoot.x < node.x:
                    if curRoot.right is None:
                        curRoot.right = node
                        node.parent = curRoot
                        break
                    else:
                        curRoot = curRoot.right
                else:
                    if curRoot.left is None:
                        curRoot.left = node
                        node.parent = curRoot
                        break
                    else:
                        curRoot = curRoot.left

    return [preorder(root, []), postorder(root, [])]

a = solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])

