n, m = map(int, input().split())

li = []


def dfs(index):
    if len(li) == m:
        print(' '.join(list(map(str, li))))
        return  # base condition 깊이가 최대일 때 빠져나온다.
    for i in range(index, n+1):  # 넓이 만큼 조합을 만들어 낸다.
        li.append(i)
        dfs(i)
        li.pop()  # 깊이를 만족하고 리턴 될 때 리스트의 길이를 줄여준다.


dfs(1)
