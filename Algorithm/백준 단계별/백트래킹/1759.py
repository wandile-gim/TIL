L, C = map(int, input().split())
alphabet = list(input().split())
alphabet.sort()
vowels = 'aeiou'
li = []


def dfs(depth, idx):
    if depth == L:
        vo = 0
        co = 0
        for i in range(L):
            if li[i] in vowels:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print(''.join(li))
        return
    for i in range(idx, C):
        li.append(alphabet[i])
        dfs(depth+1, i+1)
        li.pop()


dfs(0, 0)
