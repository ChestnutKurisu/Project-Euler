N = int(input())
if N == 1:
    print(1)
for i in range(int(10 ** ((N - 1) / N)) + 1, 10):
    print(i ** N)

# projecteuler.net version
# count = 1  # To account for 1^1 = 1
# for N in range(1, 30):
#     for i in range(int(10 ** ((N - 1) / N)) + 1, 10):
#         count += 1
# print(count)
