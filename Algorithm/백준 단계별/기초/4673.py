# num_list = list(range(0,10001))
# self_list = []

# for i in range(len(num_list)):    
#     for j in str(i):
#         i += int(j)
#     if i <= 10000:
#         self_list.append(i)

# for i in set(self_list):
#     num_list.remove(i)
# for i in num_list:
#     print(i)

num_list = set(range(1,10001))
self_list = set()

for origin_num in num_list:
    for target_num in str(origin_num):
        origin_num += int(target_num)
    if origin_num <= 10000:
        self_list.add(origin_num)

self_list = sorted(num_list - self_list)
for i in self_list:
    print(i)