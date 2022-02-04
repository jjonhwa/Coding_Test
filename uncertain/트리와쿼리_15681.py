import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, R, Q = list(map(int, input().split()))
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = list(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)

# tree with root
def tree_with_root(tree, root):
    check = tree[root] # [4, 6]
    for c in check:
        tree[c].remove(root)
        tree_with_root(tree, c)
tree_with_root(tree, R)

# subtree 찾기
size = [0] * (N+1)
def find_subtree(current_node):
    size[current_node] = 1
    for node in tree[current_node]:
        find_subtree(node)
        size[current_node] += size[node]
find_subtree(R)

for _ in range(Q):
    u = int(input())
    print(size[u])
