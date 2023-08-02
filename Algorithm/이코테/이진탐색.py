def binary_search_recursion(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursion(array, target, start, mid-1)
    else:
        return binary_search_recursion(array, target, mid+1, end)


# n, target = list(map(int, input().split()))

# if __name__ == '__main__':
#     n, target = 10, 7
#     array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#     array.sort()
#     result = binary_search(array, target, 0, n-1)
# # array = list(map(int, input().split()))
#     print(f'{result}번 째에 원소가 존재' if result else '원소가 존재하지 않습니다.')

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1


if __name__ == '__main__':
    # n, target = 10, 7
    # array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    # array.sort()
    # result = binary_search(array, target, 0, n-1)
    # array = list(map(int, input().split()))
    # print(f'{result}번 째에 원소가 존재' if result else '원소가 존재하지 않습니다.')

    n = 5
    array = [8, 3, 7, 9, 2]
    m = 3
    x = [5, 7, 9]

    array.sort()
    for i in x:
        result = binary_search_recursion(array, i, 0, n-1)
        print('yes' if result else 'no', end=' ')
