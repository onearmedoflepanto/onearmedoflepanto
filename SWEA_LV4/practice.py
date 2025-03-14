tree = [[1, 2],
        [3, 4],
        [None, 5],
        [],
        [],
        [6, 7],
        [],
        []]

tree_value = [9, 4, 12, 3, 6, 15, 13, 17]


def inorder(now):
    if tree[now]:
        if tree[now][0]:
            inorder(tree[now][0])
    if len(tree[now]) > 1:
        inorder(tree[now][1])
    print(tree_value[now], end=' ')


inorder(0)


# def dfs(path, now):
#     print(tree_value[now], end=' ')
#     for node in tree[now]:
#         path.append(node)
#         dfs(path, node)
#         path.pop()


# dfs([], 0)
