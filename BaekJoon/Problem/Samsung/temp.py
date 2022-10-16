# 완전 탐색 비트 마스크
n=3
arr = [i+1 for i in range(n)]

queue = []
a="LR"


for i in range(2**n):
    tmp = ''
    for j in range(n):
        if i & (2**j):
            tmp += a[1]
        else:
            tmp+=a[0]

    print(tmp)

# l =0
# r = 10000000000
# while l+1<r:
#     x = l+r>>1
#     if 1:
#         x = r
#     else:
#         x = l

# 동서남북 완전탐색

# n = 3
# arr = "LRUD"
# for i in range(4 ** n):
#     tmp = ""
#     for j in range(0, 2 * n, 2):
#         a = i & (1 << j)
#         b = i & (1 << j + 1)
#         if a and b:
#             tmp += arr[3]
#         elif a:
#             tmp += arr[2]
#         elif b:
#             tmp += arr[1]
#         else:
#             tmp += arr[0]
#     print(tmp)
